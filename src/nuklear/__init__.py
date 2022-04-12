from __future__ import annotations

import ctypes
import importlib.metadata
import importlib.resources
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Final, List, Optional

from .library import CEnum, nuklear as _nk

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

__dll_dir__: Final[Path] = (Path(__file__).parent / "dll").resolve()

if _nk is None:
    raise ImportError("Failed to load Nuklear shared library.")

# By default, pyGLFW will only provide functionality from released GLFW
# versions, as using the development version may lead to changing behavior or
# missing functions. If the environment variable PYGLFW_PREVIEW is set or the
# glfw_preview package can be imported, macros and functions from the current
# developtment version of GLFW will be provided. Note that there will still be
# a delay between them getting added to GLFW and being wrapped by pyGLFW, and
# further delay until they are included in a pyGLFW release.
_PREVIEW = os.environ.get("NUKLEAR_PY_PREVIEW")
if _PREVIEW is None:
    try:
        import nuklear_preview
        
        _PREVIEW = True
    except ImportError:
        _PREVIEW = False
else:
    _PREVIEW = bool(_PREVIEW)

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

UNDEFINED = _nk.NK_UNDEFINED
UTF_INVALID = _nk.NK_UTF_INVALID
UTF_SIZE = _nk.NK_UTF_SIZE
INPUT_MAX = _nk.NK_INPUT_MAX
MAX_NUMBER_BUFFER = _nk.NK_MAX_NUMBER_BUFFER
SCROLLBAR_HIDING_TIMEOUT = _nk.NK_SCROLLBAR_HIDING_TIMEOUT

# ==============================================================
#
#                          HELPER
#
# ===============================================================

# ifndef NK_API
# ifdef NK_PRIVATE
# if (defined(__STDC_VERSION__) && (__STDC_VERSION__ >= 199409L))
# define NK_API static inline
# elif defined(__cplusplus)
# define NK_API static inline
# else
# define NK_API static
# endif
# else
# define NK_API extern
# endif
# endif
# ifndef NK_LIB
# ifdef NK_SINGLE_FILE
# define NK_LIB static
# else
# define NK_LIB extern
# endif
# endif

# define NK_INTERN static
# define NK_STORAGE static
# define NK_GLOBAL static

# define NK_FLAG(x) (1 << (x))
# define NK_STRINGIFY(x) #x
# define NK_MACRO_STRINGIFY(x) NK_STRINGIFY(x)
# define NK_STRING_JOIN_IMMEDIATE(arg1, arg2) arg1 ## arg2
# define NK_STRING_JOIN_DELAY(arg1, arg2) NK_STRING_JOIN_IMMEDIATE(arg1, arg2)
# define NK_STRING_JOIN(arg1, arg2) NK_STRING_JOIN_DELAY(arg1, arg2)

# ifdef _MSC_VER
# define NK_UNIQUE_NAME(name) NK_STRING_JOIN(name,__COUNTER__)
# else
# define NK_UNIQUE_NAME(name) NK_STRING_JOIN(name,__LINE__)
# endif

# ifndef NK_STATIC_ASSERT
# define NK_STATIC_ASSERT(exp) typedef char NK_UNIQUE_NAME(_dummy_array)[(exp)?1:-1]
# endif

# ifndef NK_FILE_LINE
# ifdef _MSC_VER
# define NK_FILE_LINE __FILE__ ":" NK_MACRO_STRINGIFY(__COUNTER__)
# else
# define NK_FILE_LINE __FILE__ ":" NK_MACRO_STRINGIFY(__LINE__)
# endif
# endif

# define NK_MIN(a,b) ((a) < (b) ? (a) : (b))
# define NK_MAX(a,b) ((a) < (b) ? (b) : (a))
# define NK_CLAMP(i,v,x) (NK_MAX(NK_MIN(v,x), i))

# ifdef NK_INCLUDE_STANDARD_VARARGS
# include <stdarg.h>
# if defined(_MSC_VER) && (_MSC_VER >= 1600) /* VS 2010 and above */
# include <sal.h>
# define NK_PRINTF_FORMAT_STRING _Printf_format_string_
# else
# define NK_PRINTF_FORMAT_STRING
# endif
# if defined(__GNUC__)
# define NK_PRINTF_VARARG_FUNC(fmtargnumber) __attribute__((format(__printf__, fmtargnumber, fmtargnumber+1)))
# define NK_PRINTF_VALIST_FUNC(fmtargnumber) __attribute__((format(__printf__, fmtargnumber, 0)))
# else
# define NK_PRINTF_VARARG_FUNC(fmtargnumber)
# define NK_PRINTF_VALIST_FUNC(fmtargnumber)
# endif
# endif

# ==============================================================================
#
#                                    BASIC
#
# ==============================================================================

INT8 = _nk.NK_INT8
UINT8 = _nk.NK_UINT8
INT16 = _nk.NK_INT16
UINT16 = _nk.NK_UINT16
INT32 = _nk.NK_INT32
UINT32 = _nk.NK_UINT32
SIZE_TYPE = _nk.NK_SIZE_TYPE
POINTER_TYPE = _nk.NK_POINTER_TYPE
BOOL = _nk.NK_BOOL

Char = _nk.nk_char
uChar = _nk.nk_uchar
Byte = _nk.nk_byte
Short = _nk.nk_short
uShort = _nk.nk_ushort
Int = _nk.nk_int
uInt = _nk.nk_uint
Size = _nk.nk_size
Ptr = _nk.nk_ptr
Bool = _nk.nk_bool

Hash = _nk.nk_hash
Flags = _nk.nk_flags
Rune = _nk.nk_rune


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


false = _nk.nk_false
true = _nk.nk_true


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
    UP = _nk.NK_UP
    RIGHT = _nk.NK_RIGHT
    DOWN = _nk.NK_DOWN
    LEFT = _nk.NK_LEFT


class ButtonBehavior(CEnum):
    DEFAULT = _nk.NK_BUTTON_DEFAULT
    REPEATER = _nk.NK_BUTTON_REPEATER


class Modify(CEnum):
    FIXED = _nk.NK_FIXED
    MODIFIABLE = _nk.NK_MODIFIABLE


class Orientation(CEnum):
    VERTICAL = _nk.NK_VERTICAL
    HORIZONTAL = _nk.NK_HORIZONTAL


class CollapseStates(CEnum):
    MINIMIZED = _nk.NK_MINIMIZED
    MAXIMIZED = _nk.NK_MAXIMIZED


class ShowStates(CEnum):
    HIDDEN = _nk.NK_HIDDEN
    SHOWN = _nk.NK_SHOWN


class ChartType(CEnum):
    CHART_LINES = _nk.NK_CHART_LINES
    CHART_COLUMN = _nk.NK_CHART_COLUMN
    CHART_MAX = _nk.NK_CHART_MAX


class ChartEvent(CEnum):
    CHART_HOVERING = _nk.NK_CHART_HOVERING
    CHART_CLICKED = _nk.NK_CHART_CLICKED


class ColorFormat(CEnum):
    RGB = _nk.NK_RGB
    RGBA = _nk.NK_RGBA


class PopupType(CEnum):
    POPUP_STATIC = _nk.NK_POPUP_STATIC
    POPUP_DYNAMIC = _nk.NK_POPUP_DYNAMIC


class LayoutFormat(CEnum):
    DYNAMIC = _nk.NK_DYNAMIC
    STATIC = _nk.NK_STATIC


class TreeType(CEnum):
    TREE_NODE = _nk.NK_TREE_NODE
    TREE_TAB = _nk.NK_TREE_TAB


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
    SYMBOL_NONE = _nk.NK_SYMBOL_NONE
    SYMBOL_X = _nk.NK_SYMBOL_X
    SYMBOL_UNDERSCORE = _nk.NK_SYMBOL_UNDERSCORE
    SYMBOL_CIRCLE_SOLID = _nk.NK_SYMBOL_CIRCLE_SOLID
    SYMBOL_CIRCLE_OUTLINE = _nk.NK_SYMBOL_CIRCLE_OUTLINE
    SYMBOL_RECT_SOLID = _nk.NK_SYMBOL_RECT_SOLID
    SYMBOL_RECT_OUTLINE = _nk.NK_SYMBOL_RECT_OUTLINE
    SYMBOL_TRIANGLE_UP = _nk.NK_SYMBOL_TRIANGLE_UP
    SYMBOL_TRIANGLE_DOWN = _nk.NK_SYMBOL_TRIANGLE_DOWN
    SYMBOL_TRIANGLE_LEFT = _nk.NK_SYMBOL_TRIANGLE_LEFT
    SYMBOL_TRIANGLE_RIGHT = _nk.NK_SYMBOL_TRIANGLE_RIGHT
    SYMBOL_PLUS = _nk.NK_SYMBOL_PLUS
    SYMBOL_MINUS = _nk.NK_SYMBOL_MINUS
    SYMBOL_MAX = _nk.NK_SYMBOL_MAX
