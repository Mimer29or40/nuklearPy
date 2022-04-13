import os
import shutil
import subprocess
import sys
from pathlib import Path

project_dir = Path(os.getcwd()).resolve()

build_dir = project_dir / "build"

bin_dir = project_dir / "src" / "nuklear" / "bin"

os.chdir(build_dir)


def clean() -> None:
    """Cleans the build directory"""
    for file_or_dir in build_dir.glob("*"):
        if file_or_dir.is_dir():
            shutil.rmtree(file_or_dir)
        else:
            file_or_dir.unlink()


def setup_files() -> None:
    """Setup the files needed to build the library"""
    header = project_dir / "Nuklear" / "nuklear.h"
    contents = header.read_text()

    h_file: Path = build_dir / "nuklear.h"
    h_file.write_text(contents)

    contents = os.linesep.join(
        (
            "#define NK_API __declspec(dllexport)",
            "#define NK_INCLUDE_FIXED_TYPES",
            "#define NK_INCLUDE_DEFAULT_ALLOCATOR",
            "#define NK_INCLUDE_STANDARD_IO",
            "#define NK_INCLUDE_STANDARD_VARARGS",
            "#define NK_INCLUDE_DEFAULT_ALLOCATOR",
            "#define NK_INCLUDE_VERTEX_BUFFER_OUTPUT",
            "#define NK_INCLUDE_FONT_BAKING",
            "#define NK_INCLUDE_DEFAULT_FONT",
            "#define NK_IMPLEMENTATION",
            '#include "nuklear.h"',
        )
    )
    c_file: Path = build_dir / "nuklear.c"
    c_file.write_text(contents)


def build() -> None:
    """Builds the library files"""
    if sys.platform == "win32":
        # TODO - Support for different Visual Studio compilers
        args = [
            r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat",
            "&&",
            "cl", "/LD", f"{build_dir / 'nuklear.c'}"
        ]
    else:
        # TODO - Non-Window builds
        args = []

    subprocess.run(args)


def install() -> None:
    """Copies the build files into the package folder"""

    if sys.platform == "win32":
        dll_file = build_dir / "nuklear.dll"
        shutil.copy(dll_file, bin_dir)
    else:
        pass


if __name__ == "__main__":
    clean()
    setup_files()
    build()
    install()
