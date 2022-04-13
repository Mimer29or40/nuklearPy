from __future__ import annotations

import ctypes
import importlib.metadata
import importlib.resources
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Final, List, Optional

from nuklear.library import CEnum, nuklear as _nk

_metadata = importlib.metadata.metadata(__name__)

__metadata_version__: Final[Optional[str]] = _metadata.get("metadata-version", None)

__title__: Final[Optional[str]] = _metadata.get("name", None)
__version__: Final[Optional[str]] = _metadata.get("version", None)
__summary__: Final[Optional[str]] = _metadata.get("summary", None)
__author__: Final[Optional[str]] = _metadata.get("author", None)
__maintainer__: Final[Optional[str]] = _metadata.get("maintainer", __author__)
__license__: Final[Optional[str]] = _metadata.get("license", None)
__url__: Final[Optional[str]] = _metadata.get("home-page", None)
__download_url__: Final[Optional[str]] = _metadata.get("download-url", None)
__project_urls__: Final[Dict[str, str]] = {
    values[0].strip(): values[1].strip()
    for url_str in _metadata.get_all("project-url", tuple())
    if (values := url_str.split(","))
}

__copyright__: Final[str] = f"Copyright 2022 {__author__}"

__bin_dir__: Final[Path] = (Path(__file__).parent / "bin").resolve()

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

# ==============================================================
#
#                          CONSTANTS
#
# ==============================================================

UNDEFINED = -1.0
UTF_INVALID = 0xFFFD  # internal invalid utf8 rune
UTF_SIZE = 4  # describes the number of bytes a glyph consists of
INPUT_MAX = 16
MAX_NUMBER_BUFFER = 64
SCROLLBAR_HIDING_TIMEOUT = 4.0

# ==============================================================================
#
#                                    BASIC
#
# ==============================================================================

Char = ctypes.c_int8
uChar = ctypes.c_uint8
Byte = ctypes.c_uint8
Short = ctypes.c_int16
uShort = ctypes.c_uint16
Int = ctypes.c_int32
uInt = ctypes.c_uint32
Size = ctypes.c_size_t
Ptr = ctypes.c_void_p
Bool = ctypes.c_bool

Hash = ctypes.c_uint
Flags = ctypes.c_uint
Rune = ctypes.c_uint


# ==============================================================================
#
#                                  API
#
# ==============================================================================


class Buffer(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_buffer;
    """

    class Buffer:
        pass


class Allocator(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_allocator;
    """

    class Allocator:
        pass


class CommandBuffer(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_command_buffer;
    """

    class CommandBuffer:
        pass


class DrawCommand(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_draw_command;
    """

    class DrawCommand:
        pass


class ConvertConfig(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_convert_config;
    """

    class ConvertConfig:
        pass


class StyleItem(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_item;
    """

    class StyleItem:
        pass


class TextEdit(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_text_edit;
    """

    class TextEdit:
        pass


class DrawList(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_draw_list;
    """

    class DrawList:
        pass


class UserFont(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_user_font;
    """

    class UserFont:
        pass


class Panel(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_panel;
    """

    class Panel:
        pass


class Context(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_context;
    """

    class Context:
        pass


class DrawVertexLayoutElement(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_draw_vertex_layout_element;
    """

    class DrawVertexLayoutElement:
        pass


class StyleButton(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_button;
    """

    class StyleButton:
        pass


class StyleToggle(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_toggle;
    """

    class StyleToggle:
        pass


class StyleSelectable(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_selectable;
    """

    class StyleSelectable:
        pass


class StyleSlide(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_slide;
    """

    class StyleSlide:
        pass


class StyleProgress(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_progress;
    """

    class StyleProgress:
        pass


class StyleScrollbar(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_scrollbar;
    """

    class StyleScrollbar:
        pass


class StyleEdit(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_edit;
    """

    class StyleEdit:
        pass


class StyleProperty(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_property;
    """

    class StyleProperty:
        pass


class StyleChart(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_chart;
    """

    class StyleChart:
        pass


class StyleCombo(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_combo;
    """

    class StyleCombo:
        pass


class StyleTab(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_tab;
    """

    class StyleTab:
        pass


class StyleWindowHeader(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_window_header;
    """

    class StyleWindowHeader:
        pass


class StyleWindow(ctypes.Structure):
    """
    Forward declaration for:
        struct nk_style_window;
    """

    class StyleWindow:
        pass


false = 0  # _nk.nk_false
true = 1  # _nk.nk_true


class Color(ctypes.Structure):
    """
    Wrapper for:
        struct nk_color {nk_byte r,g,b,a;};
    """

    _fields_ = [
        ("r", Byte),
        ("g", Byte),
        ("b", Byte),
        ("a", Byte),
    ]

    @dataclass
    class Color:
        r: int
        g: int
        b: int
        a: int

    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 0

    def wrap(self, color) -> None:
        """
        Wraps a nested python sequence.
        """
        self.r, self.g, self.b, self.a = color

    def unwrap(self) -> Color:
        """
        Returns a Color object.
        """
        return self.Color(self.r, self.g, self.b, self.a)


class Colorf(ctypes.Structure):
    """
    Wrapper for:
        struct nk_colorf {float r,g,b,a;};
    """

    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float),
        ("a", ctypes.c_float),
    ]

    @dataclass
    class Colorf:
        r: float
        g: float
        b: float
        a: float

    def __init__(self):
        super().__init__()
        self.r = 0.0
        self.g = 0.0
        self.b = 0.0
        self.a = 0.0

    def wrap(self, colorf) -> None:
        """
        Wraps a nested python sequence.
        """
        self.r, self.g, self.b, self.a = colorf

    def unwrap(self) -> Colorf:
        """
        Returns a Colorf object.
        """
        return self.Colorf(self.r, self.g, self.b, self.a)


class Vec2(ctypes.Structure):
    """
    Wrapper for:
        struct nk_vec2 {float x,y;};
    """

    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
    ]

    @dataclass
    class Vec2:
        x: float
        y: float

    def __init__(self):
        super().__init__()
        self.x = 0.0
        self.y = 0.0

    def wrap(self, vec2) -> None:
        """
        Wraps a nested python sequence.
        """
        self.x, self.y = vec2

    def unwrap(self) -> Vec2:
        """
        Returns a Vec2 object.
        """
        return self.Vec2(self.x, self.y)


class Vec2i(ctypes.Structure):
    """
    Wrapper for:
        struct nk_vec2 {float x,y;};
    """

    _fields_ = [
        ("x", Short),
        ("y", Short),
    ]

    @dataclass
    class Vec2i:
        x: int
        y: int

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def wrap(self, vec2i) -> None:
        """
        Wraps a nested python sequence.
        """
        self.x, self.y = vec2i

    def unwrap(self) -> Vec2i:
        """
        Returns a Vec2i object.
        """
        return self.Vec2i(self.x, self.y)


class Rect(ctypes.Structure):
    """
    Wrapper for:
        struct nk_rect {float x,y,w,h;};
    """

    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("w", ctypes.c_float),
        ("h", ctypes.c_float),
    ]

    @dataclass
    class Rect:
        x: float
        y: float
        w: float
        h: float

    def __init__(self):
        super().__init__()
        self.x = 0.0
        self.y = 0.0
        self.w = 0.0
        self.h = 0.0

    def wrap(self, nk_rect) -> None:
        """
        Wraps a nested python sequence.
        """
        self.x, self.y, self.w, self.h = nk_rect

    def unwrap(self) -> Rect:
        """
        Returns a Rect object.
        """
        return self.Rect(self.x, self.y, self.w, self.h)


class Recti(ctypes.Structure):
    """
    Wrapper for:
        struct nk_recti {float x,y,w,h;};
    """

    _fields_ = [
        ("x", Short),
        ("y", Short),
        ("w", Short),
        ("h", Short),
    ]

    @dataclass
    class Recti:
        x: int
        y: int
        w: int
        h: int

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

    def wrap(self, recti) -> None:
        """
        Wraps a nested python sequence.
        """
        self.x, self.y, self.w, self.h = recti

    def unwrap(self) -> Recti:
        """
        Returns a Recti object.
        """
        return self.Recti(self.x, self.y, self.w, self.h)


class Glyph(ctypes.Structure):
    """
    Wrapper for:
        typedef char nk_glyph[NK_UTF_SIZE];
    """

    _fields_ = [("dummy", ctypes.c_char * UTF_SIZE)]


class Handle(ctypes.Union):
    """
    Wrapper for:
        typedef union {void *ptr; int id;} nk_handle;
    """

    _fields_ = [
        ("ptr", ctypes.c_void_p),
        ("id", ctypes.c_int),
    ]

    @dataclass
    class Handle:
        Ptr: int
        id: int

    def __init__(self):
        super().__init__()
        self.ptr = 0
        self.id = 0

    def wrap(self, handle) -> None:
        """
        Wraps a nested python sequence.
        """
        self.ptr, self.id = handle

    def unwrap(self) -> Handle:
        """
        Returns a Handle object.
        """
        return self.Handle(self.ptr, self.id)


class Image(ctypes.Structure):
    """
    Wrapper for:
        struct nk_image {nk_handle handle; nk_ushort w, h; nk_ushort region[4];};
    """

    _fields_ = [
        ("handle", Handle),
        ("w", uShort),
        ("h", uShort),
        ("region", uShort * 4),
    ]

    @dataclass
    class Image:
        handle: Handle.Handle
        w: int
        h: int
        region: List[int]

    def __init__(self):
        super().__init__()
        self.handle = None
        self.w = 0
        self.h = 0
        self.region = None

    def wrap(self, image) -> None:
        """
        Wraps a nested python sequence.
        """
        handle, self.w, self.h, region = image

        self.handle = Handle()
        self.handle.wrap(handle)

        self.region = (uShort * 4)()
        for i, r in enumerate(region):
            self.region[i] = r

    def unwrap(self) -> Image:
        """
        Returns an Image object.
        """
        handle = self.handle.unwrap()
        region = [int(r) for r in self.region]
        return self.Image(handle, self.w, self.h, region)


class NineSlice(ctypes.Structure):
    """
    Wrapper for:
        struct nk_nine_slice {struct nk_image img; nk_ushort l, t, r, b;};
    """

    _fields_ = [
        ("img", Image),
        ("l", uShort),
        ("t", uShort),
        ("r", uShort),
        ("b", uShort),
    ]

    @dataclass
    class NineSlice:
        img: Image.Image
        l: int
        t: int
        r: int
        b: int

    def __init__(self):
        super().__init__()
        self.image = None
        self.l = 0
        self.t = 0
        self.r = 0
        self.b = 0

    def wrap(self, cursor) -> None:
        """
        Wraps a nested python sequence.
        """
        image, self.l, self.t, self.r, self.b = cursor

        self.image = Image()
        self.image.wrap(image)

    def unwrap(self) -> NineSlice:
        """
        Returns a NineSlice object.
        """
        image = self.image.unwrap()
        return self.Cursor(image, self.l, self.t, self.r, self.b)


class Cursor(ctypes.Structure):
    """
    Wrapper for:
        struct nk_cursor {struct nk_image img; struct nk_vec2 size, offset;};
    """

    _fields_ = [
        ("img", Image),
        ("size", Vec2),
        ("offset", Vec2),
    ]

    @dataclass
    class Cursor:
        img: Image.Image
        size: Vec2.Vec2
        offset: Vec2.Vec2

    def __init__(self):
        super().__init__()
        self.image = None
        self.size = None
        self.offset = None

    def wrap(self, cursor) -> None:
        """
        Wraps a nested python sequence.
        """
        image, size, offset = cursor

        self.image = Image()
        self.image.wrap(image)

        self.size = Vec2()
        self.size.wrap(size)

        self.offset = Vec2()
        self.offset.wrap(offset)

    def unwrap(self) -> Cursor:
        """
        Returns a Cursor object.
        """
        image = self.image.unwrap()
        size = self.size.unwrap()
        offset = self.offset.unwrap()
        return self.Cursor(image, size, offset)


class Scroll(ctypes.Structure):
    """
    Wrapper for:
        struct nk_scroll {nk_uint x, y;};
    """

    _fields_ = [
        ("x", uInt),
        ("y", uInt),
    ]

    @dataclass
    class Scroll:
        x: int
        y: int

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def wrap(self, scroll) -> None:
        """
        Wraps a nested python sequence.
        """
        self.x, self.y = scroll

    def unwrap(self) -> Scroll:
        """
        Returns a Scroll object.
        """
        return self.Scroll(self.x, self.y)


class Heading(CEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class ButtonBehavior(CEnum):
    DEFAULT = 0
    REPEATER = 1


class Modify(CEnum):
    FIXED = 0
    MODIFIABLE = 1


class Orientation(CEnum):
    VERTICAL = 0
    HORIZONTAL = 1


class CollapseStates(CEnum):
    MINIMIZED = 0
    MAXIMIZED = 1


class ShowStates(CEnum):
    HIDDEN = 0
    SHOWN = 1


class ChartType(CEnum):
    CHART_LINES = 0
    CHART_COLUMN = 1
    CHART_MAX = 2


class ChartEvent(CEnum):
    CHART_HOVERING = 0x01
    CHART_CLICKED = 0x02


class ColorFormat(CEnum):
    RGB = 0
    RGBA = 1


class PopupType(CEnum):
    POPUP_STATIC = 0
    POPUP_DYNAMIC = 1


class LayoutFormat(CEnum):
    DYNAMIC = 0
    STATIC = 1


class TreeType(CEnum):
    TREE_NODE = 0
    TREE_TAB = 1


PluginAlloc = ctypes.CFUNCTYPE(ctypes.c_void_p, Handle, ctypes.c_void_p, Size)
PluginAlloc.PluginAlloc = Callable[[Handle.Handle, int, int], int]

PluginFree = ctypes.CFUNCTYPE(None, Handle, ctypes.c_void_p)
PluginFree.PluginFree = Callable[[Handle.Handle, int], None]

PluginFilter = ctypes.CFUNCTYPE(Bool, ctypes.POINTER(TextEdit), Rune)
PluginFilter.PluginFilter = Callable[[TextEdit.TextEdit, int], bool]

PluginPaste = ctypes.CFUNCTYPE(None, Handle, ctypes.POINTER(TextEdit))
PluginPaste.PluginPaste = Callable[[Handle.Handle, TextEdit.TextEdit], None]

PluginCopy = ctypes.CFUNCTYPE(None, Handle, ctypes.c_char_p, ctypes.c_int)
PluginCopy.PluginCopy = Callable[[Handle.Handle, int, int], None]


# noinspection PyRedeclaration
class Allocator(ctypes.Structure):
    """
    Wrapper for:
        struct nk_allocator {
            nk_handle userdata;
            nk_plugin_alloc alloc;
            nk_plugin_free free;
        };
    """

    _fields_ = [
        ("userdata", Handle),
        ("alloc", PluginAlloc),
        ("free", PluginFree),
    ]

    @dataclass
    class Allocator:
        userdata: Handle.Handle
        alloc: PluginAlloc.PluginAlloc
        free: PluginFree.PluginFree


class SymbolType(CEnum):
    SYMBOL_NONE = 0
    SYMBOL_X = 1
    SYMBOL_UNDERSCORE = 2
    SYMBOL_CIRCLE_SOLID = 3
    SYMBOL_CIRCLE_OUTLINE = 4
    SYMBOL_RECT_SOLID = 5
    SYMBOL_RECT_OUTLINE = 6
    SYMBOL_TRIANGLE_UP = 7
    SYMBOL_TRIANGLE_DOWN = 8
    SYMBOL_TRIANGLE_LEFT = 9
    SYMBOL_TRIANGLE_RIGHT = 10
    SYMBOL_PLUS = 11
    SYMBOL_MINUS = 12
    SYMBOL_MAX = 13


# ==============================================================================
#
#                                    CONTEXT
#
# ==============================================================================

_nk.nk_init_default.restype = Bool
_nk.nk_init_default.argtypes = [ctypes.POINTER(Context), ctypes.POINTER(UserFont)]


def init_default(ctx: Context, font: UserFont) -> bool:
    """
    Initializes a `Context` struct with a default standard library allocator.
    Should be used if you don't want to be bothered with memory management in nuklear.
    Wrapper for:
        nk_bool nk_init_default(struct nk_context*, const struct nk_user_font*);
    """
    return _nk.nk_init_default(ctx, font)


_nk.nk_init_fixed.restype = Bool
_nk.nk_init_fixed.argtypes = [
    ctypes.POINTER(Context),
    ctypes.c_void_p,
    Size,
    ctypes.POINTER(UserFont),
]


def init_fixed(ctx: Context, memory: int, size: int, font: UserFont) -> bool:
    """
    Initializes a `Context` struct from single fixed size memory block
    Should be used if you want complete control over nuklear's memory management.
    Especially recommended for system with little memory or systems with virtual memory.
    For the later case you can just allocate for example 16MB of virtual memory
    and only the required amount of memory will actually be committed.
    Wrapper for:
        nk_bool nk_init_fixed(struct nk_context*, void *memory, nk_size size, const struct nk_user_font*);
    """
    memory_ptr = ctypes.c_void_p(memory)
    size_value = ctypes.c_int(size)
    return _nk.nk_init_fixed(ctx, memory_ptr, size_value, font)


_nk.nk_init.restype = Bool
_nk.nk_init.argtypes = [
    ctypes.POINTER(Context),
    ctypes.POINTER(Allocator),
    ctypes.POINTER(UserFont),
]


def init(ctx: Context, alloc: Allocator, font: UserFont) -> bool:
    """
    Initializes a `Context` struct with memory allocation callbacks for nuklear to allocate
    memory from. Used internally for `init_default` and provides a kitchen sink allocation
    interface to nuklear. Can be useful for cases like monitoring memory consumption.
    Wrapper for:
        nk_bool nk_init(struct nk_context*, struct nk_allocator*, const struct nk_user_font*);
    """
    return _nk.nk_init(ctx, alloc, font)


_nk.nk_init_custom.restype = Bool
_nk.nk_init_custom.argtypes = [
    ctypes.POINTER(Context),
    ctypes.POINTER(Buffer),
    ctypes.POINTER(Buffer),
    ctypes.POINTER(UserFont),
]


def init_custom(ctx: Context, cmds: Buffer, pool: Buffer, font: UserFont) -> bool:
    """
    Initializes a `Context` struct from two different either fixed or growing
    buffers. The first buffer is for allocating draw commands while the second buffer is
    used for allocating windows, panels and state tables.
    Wrapper for:
        nk_bool nk_init_custom(struct nk_context*, struct nk_buffer *cmds, struct nk_buffer *pool, const struct nk_user_font*);
    """
    return _nk.nk_init_custom(ctx, cmds, pool, font)


_nk.nk_clear.restype = None
_nk.nk_clear.argtypes = [ctypes.POINTER(Context)]


def clear(ctx: Context) -> None:
    """
    Resets the context state at the end of the frame. This includes mostly
    garbage collector tasks like removing windows or table not called and therefore
    used anymore.
    Wrapper for:
        void nk_clear(struct nk_context*);
    """
    _nk.nk_clear(ctx)


_nk.nk_free.restype = None
_nk.nk_free.argtypes = [ctypes.POINTER(Context)]


def free(ctx: Context) -> None:
    """
    Frees all memory allocated by nuklear. Not needed if context was
    initialized with `init_fixed`.
    Wrapper for:
        void nk_free(struct nk_context*);
    """
    _nk.nk_free(ctx)


if hasattr(_nk, "nk_set_user_data"):
    _nk.nk_set_user_data.restype = None
    _nk.nk_set_user_data.argtypes = [ctypes.POINTER(Context), Handle]


    def set_user_data(ctx: Context, handle: Handle) -> None:
        """
        Frees all memory allocated by nuklear. Not needed if context was
        initialized with `init_fixed`.
        Wrapper for:
            void nk_set_user_data(struct nk_context*, nk_handle handle);
        """
        _nk.nk_set_user_data(ctx, handle)
else:
    def set_user_data(ctx: Context, handle: Handle) -> None:
        pass
