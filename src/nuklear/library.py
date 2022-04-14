"""
Python bindings for Nuklear.
"""

from __future__ import annotations

import ctypes
import glob
import os
import subprocess
import sys
import textwrap
from abc import ABC
from abc import abstractmethod
from dataclasses import astuple
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional, Type, TypeVar, Union

from nuklear import metadata


def _find_library_candidates(
    library_names, library_file_extensions, library_search_paths
):
    """
    Finds and returns filenames which might be the library you are looking for.
    """
    candidates = set()
    for library_name in library_names:
        for search_path in library_search_paths:
            glob_query = os.path.join(search_path, "*" + library_name + "*")
            for filename in glob.iglob(glob_query):
                filename = os.path.realpath(filename)
                if filename in candidates:
                    continue
                basename = os.path.basename(filename)
                if basename.startswith("lib" + library_name):
                    basename_end = basename[len("lib" + library_name) :]
                elif basename.startswith(library_name):
                    basename_end = basename[len(library_name) :]
                else:
                    continue
                for file_extension in library_file_extensions:
                    if basename_end.startswith(file_extension):
                        if basename_end[len(file_extension) :][:1] in ("", "."):
                            candidates.add(filename)
                    if basename_end.endswith(file_extension):
                        basename_middle = basename_end[: -len(file_extension)]
                        if all(c in "0123456789." for c in basename_middle):
                            candidates.add(filename)
    return candidates


def _load_library(
    library_names, library_file_extensions, library_search_paths, version_check_callback
):
    """
    Finds, loads and returns the most recent version of the library.
    """
    candidates = _find_library_candidates(
        library_names, library_file_extensions, library_search_paths
    )
    library_versions = []
    for filename in candidates:
        version = version_check_callback(filename)
        if version is not None and version >= (3, 0, 0):
            library_versions.append((version, filename))

    if not library_versions:
        return None
    library_versions.sort()
    return ctypes.CDLL(library_versions[-1][1])


def _nuklear_get_version(filename):
    """
    Queries and returns the library version tuple or None by using a
    subprocess.
    """
    version_checker_source = '''
        import sys
        import ctypes
        def get_version(library_handle):
            """
            Queries and returns the library version tuple or None.
            """
            major_value = ctypes.c_int(0)
            major = ctypes.pointer(major_value)
            minor_value = ctypes.c_int(0)
            minor = ctypes.pointer(minor_value)
            rev_value = ctypes.c_int(0)
            rev = ctypes.pointer(rev_value)
            if hasattr(library_handle, 'glfwGetVersion'):
                library_handle.glfwGetVersion(major, minor, rev)
                version = (major_value.value,
                           minor_value.value,
                           rev_value.value)
                return version
            else:
                return None
        try:
            input_func = raw_input
        except NameError:
            input_func = input
        filename = input_func().strip()
        try:
            library_handle = ctypes.CDLL(filename)
        except OSError:
            pass
        else:
            version = get_version(library_handle)
            print(version)
    '''

    args = [sys.executable, "-c", textwrap.dedent(version_checker_source)]
    process = subprocess.Popen(
        args, universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    out = process.communicate(filename)[0]
    out = out.strip()
    if out:
        return eval(out)
    else:
        return None


def _get_library_search_paths():
    """
    Returns a list of library search paths, considering of the current working
    directory, default paths and paths from environment variables.
    """
    package_path = os.path.abspath(os.path.dirname(__file__))
    search_paths = [
        "",
        package_path,
        sys.prefix + "/lib",
        "/usr/lib64",
        "/usr/local/lib64",
        "/usr/lib",
        "/usr/local/lib",
        "/opt/homebrew/lib",
        "/run/current-system/sw/lib",
        "/usr/lib/x86_64-linux-gnu/",
        "/usr/lib/aarch64-linux-gnu/",
        "/usr/lib/arm-linux-gnueabihf",
    ]

    if sys.platform != "darwin":
        # manylinux2014 wheels contain libraries built for X11 and Wayland
        if os.environ.get("XDG_SESSION_TYPE") == "wayland":
            search_paths.insert(1, os.path.join(package_path, "wayland"))
        else:
            # X11 is the default, even if XDG_SESSION_TYPE is not set
            search_paths.insert(1, os.path.join(package_path, "x11"))

    if sys.platform == "darwin":
        path_environment_variable = "DYLD_LIBRARY_PATH"
    else:
        path_environment_variable = "LD_LIBRARY_PATH"
    if path_environment_variable in os.environ:
        search_paths.extend(os.environ[path_environment_variable].split(":"))
    return search_paths


# noinspection PyTypeChecker
class EnumerationType(type(ctypes.c_uint)):
    def __new__(cls, name, bases, dict):
        if "_members_" not in dict:
            _members_ = {}
            for key, value in dict.items():
                if not key.startswith("_"):
                    _members_[key] = value

            dict["_members_"] = _members_
        else:
            _members_ = dict["_members_"]

        dict["_reverse_map_"] = {v: k for k, v in _members_.items()}
        cls = type(ctypes.c_uint).__new__(cls, name, bases, dict)
        for key, value in cls._members_.items():
            globals()[key] = value
        return cls

    def __repr__(self):
        return f"<Enumeration {self.__name__}>"

    def __iter__(self):
        return iter(self._members_.values())

    def __len__(self):
        return len(self._members_)


# noinspection PyUnresolvedReferences
class CEnum(ctypes.c_uint, metaclass=EnumerationType):
    def __repr__(self):
        value = self.value
        return (
            f"<{self.__class__.__name__}."
            f"{self._reverse_map_.get(value, '(unknown)')}: {value:d}>"
        )

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other

        return type(self) == type(other) and self.value == other.value


T = TypeVar("T", bound="StructWrapper")


@dataclass
class StructWrapper(ABC):
    def __iter__(self):
        return iter(astuple(self))

    def __len__(self):
        return len(astuple(self))

    @abstractmethod
    def to_c(self) -> T.Struct:
        ...

    @classmethod
    @abstractmethod
    def from_c(cls, color: T.Struct) -> T:
        ...


# Python 3 compatibility:
# try:
#     _getcwd = os.getcwdu
# except AttributeError:
#     _getcwd = os.getcwd
if sys.version_info.major > 2:

    def to_char_p(s):
        return s.encode("utf-8")

    def from_char_p(b):
        return b.decode()

    def _reraise(exception, traceback):
        raise exception.with_traceback(traceback)

else:

    def to_char_p(s):
        return s

    def from_char_p(b):
        return b

    def _reraise(exception, traceback):
        # wrapped in exec, as python 3 does not support this variant of raise
        exec("raise exception, None, traceback")


nuklear: Optional[ctypes.CDLL] = None
if os.environ.get("NUKLEAR_PY_LIBRARY", ""):
    try:
        nuklear = ctypes.CDLL(os.environ["NUKLEAR_PY_LIBRARY"])
    except OSError:
        nuklear = None
elif sys.platform == "win32":
    # try Windows default search path
    try:
        # TODO - Check for proper name on all dll's
        nuklear = ctypes.CDLL("nuklear.dll")
    except OSError:
        pass

    # try package directory
    if nuklear is None:
        try:
            if sys.maxsize > 2**32:
                # load Microsoft Visual C++ 2012 runtime on 64-bit systems
                msvcr = ctypes.CDLL(str(metadata.__bin_dir__ / "msvcr110.dll"))
            else:
                # load Microsoft Visual C++ 2010 runtime on 32-bit systems
                msvcr = ctypes.CDLL(str(metadata.__bin_dir__ / "msvcr100.dll"))
            nuklear = ctypes.CDLL(str(metadata.__bin_dir__ / "nuklear.dll"))
        except OSError:
            pass

    # try conda's default location on Windows
    if nuklear is None:
        try:
            nuklear = ctypes.CDLL(
                str(Path(sys.prefix) / "Library" / "bin" / "nuklear.dll")
            )
        except OSError:
            pass
else:
    nuklear = _load_library(
        ["nuklear"],
        [".so", ".dylib"],
        _get_library_search_paths(),
        _nuklear_get_version,
    )

if nuklear is None:
    raise ImportError("Failed to load Nuklear shared library.")


# By default, pyGLFW will only provide functionality from released GLFW
# versions, as using the development version may lead to changing behavior or
# missing functions. If the environment variable PYGLFW_PREVIEW is set or the
# glfw_preview package can be imported, macros and functions from the current
# developtment version of GLFW will be provided. Note that there will still be
# a delay between them getting added to GLFW and being wrapped by pyGLFW, and
# further delay until they are included in a pyGLFW release.
_PREVIEW = bool(os.environ.get("NUKLEAR_PY_PREVIEW", False))
if _PREVIEW is None:
    try:
        import nuklear_preview

        _PREVIEW = True
    except ImportError:
        _PREVIEW = False
