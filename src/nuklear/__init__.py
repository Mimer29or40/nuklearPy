from __future__ import annotations

import ctypes
import os

from nuklear.library import CEnum
from nuklear.library import c_func
from nuklear.library import nuklear as _nk
from nuklear.types import *

if _nk is None:
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

# Python 3 compatibility:
# try:
#     _getcwd = os.getcwdu
# except AttributeError:
#     _getcwd = os.getcwd
# if sys.version_info.major > 2:
#     _to_char_p = lambda s: s.encode('utf-8')
#     def _reraise(exception, traceback):
#         raise exception.with_traceback(traceback)
# else:
#     _to_char_p = lambda s: s
#     def _reraise(exception, traceback):
#         # wrapped in exec, as python 3 does not support this variant of raise
#         exec("raise exception, None, traceback")

# support for CFFI pointers for Vulkan objects
try:
    from cffi import FFI
except ImportError:
    FFI = None

    def _cffi_to_ctypes_void_p(ptr):
        return ptr

else:
    ffi = FFI()

    def _cffi_to_ctypes_void_p(ptr):
        if isinstance(ptr, ffi.CData):
            return ctypes.cast(Int(ffi.cast("uintptr_t", ptr)), ctypes.c_void_p)
        return ptr


# ==============================================================================
#
#                                    CONTEXT
#
# ==============================================================================


# @c_func(_nk.nk_init_default, (ctypes.POINTER(Context), ctypes.POINTER(UserFont)), Bool)
# def init_default(ctx: Context, font: UserFont) -> bool:
#     """
#     Initializes a `Context` struct with a default standard library allocator.
#     Should be used if you don't want to be bothered with memory management in nuklear.
#     Wrapper for:
#         nk_bool nk_init_default(struct nk_context*, const struct nk_user_font*);
#     """
#     return _nk.nk_init_default(ctx, font)
#
#
# @c_func(
#     _nk.nk_init_fixed,
#     (
#             ctypes.POINTER(Context),
#             ctypes.c_void_p,
#             Size,
#             ctypes.POINTER(UserFont),
#     ),
#     Bool
# )
# def init_fixed(ctx: Context, memory: int, size: int, font: UserFont) -> bool:
#     """
#     Initializes a `Context` struct from single fixed size memory block
#     Should be used if you want complete control over nuklear's memory management.
#     Especially recommended for system with little memory or systems with virtual memory.
#     For the later case you can just allocate for example 16MB of virtual memory
#     and only the required amount of memory will actually be committed.
#     Wrapper for:
#         nk_bool nk_init_fixed(struct nk_context*, void *memory, nk_size size, const struct nk_user_font*);
#     """
#     memory_ptr = ctypes.c_void_p(memory)
#     size_value = ctypes.c_int(size)
#     return _nk.nk_init_fixed(ctx, memory_ptr, size_value, font)
#
#
# @c_func(
#     _nk.nk_init,
#     (
#             ctypes.POINTER(Context),
#             ctypes.POINTER(Allocator),
#             ctypes.POINTER(UserFont),
#     ),
#     Bool
# )
# def init(ctx: Context, alloc: Allocator, font: UserFont) -> bool:
#     """
#     Initializes a `Context` struct with memory allocation callbacks for nuklear to allocate
#     memory from. Used internally for `init_default` and provides a kitchen sink allocation
#     interface to nuklear. Can be useful for cases like monitoring memory consumption.
#     Wrapper for:
#         nk_bool nk_init(struct nk_context*, struct nk_allocator*, const struct nk_user_font*);
#     """
#     return _nk.nk_init(ctx, alloc, font)
#
#
# @c_func(
#     _nk.nk_init_custom,
#     (
#             ctypes.POINTER(Context),
#             ctypes.POINTER(Buffer),
#             ctypes.POINTER(Buffer),
#             ctypes.POINTER(UserFont),
#     ),
#     Bool
# )
# def init_custom(ctx: Context, cmds: Buffer, pool: Buffer, font: UserFont) -> bool:
#     """
#     Initializes a `Context` struct from two different either fixed or growing
#     buffers. The first buffer is for allocating draw commands while the second buffer is
#     used for allocating windows, panels and state tables.
#     Wrapper for:
#         nk_bool nk_init_custom(struct nk_context*, struct nk_buffer *cmds, struct nk_buffer *pool, const struct nk_user_font*);
#     """
#     return _nk.nk_init_custom(ctx, cmds, pool, font)
#
#
# @c_func(_nk.nk_clear, (ctypes.POINTER(Context),), None)
# def clear(ctx: Context) -> None:
#     """
#     Resets the context state at the end of the frame. This includes mostly
#     garbage collector tasks like removing windows or table not called and therefore
#     used anymore.
#     Wrapper for:
#         void nk_clear(struct nk_context*);
#     """
#     _nk.nk_clear(ctx)
#
#
# @c_func(_nk.nk_free, (ctypes.POINTER(Context),), None)
# def free(ctx: Context) -> None:
#     """
#     Frees all memory allocated by nuklear. Not needed if context was
#     initialized with `init_fixed`.
#     Wrapper for:
#         void nk_free(struct nk_context*);
#     """
#     _nk.nk_free(ctx)
#
#
# if hasattr(_nk, "nk_set_user_data"):
#     @c_func(_nk.nk_set_user_data, (ctypes.POINTER(Context), Handle), None)
#     def set_user_data(ctx: Context, handle: Handle) -> None:
#         """
#         Frees all memory allocated by nuklear. Not needed if context was
#         initialized with `init_fixed`.
#         Wrapper for:
#             void nk_set_user_data(struct nk_context*, nk_handle handle);
#         """
#         _nk.nk_set_user_data(ctx, handle)
#
# else:
#     def set_user_data(ctx: Context, handle: Handle) -> None:
#         pass
