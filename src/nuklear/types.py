from __future__ import annotations

import ctypes
from abc import ABC
from dataclasses import dataclass
from dataclasses import field
from typing import Callable, List, Optional

from nuklear.library import CEnum
from nuklear.library import StructWrapper

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
UChar = ctypes.c_uint8
Byte = ctypes.c_uint8
Short = ctypes.c_int16
UShort = ctypes.c_uint16
Int = ctypes.c_int32
UInt = ctypes.c_uint32
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

false = 0  # _nk.nk_false
true = 1  # _nk.nk_true


@dataclass(eq=True, order=True)
class Color(StructWrapper):
    """
    Wrapper for:
        struct nk_color {nk_byte r,g,b,a;};
    """

    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("r", Byte),
            ("g", Byte),
            ("b", Byte),
            ("a", Byte),
        ]
        __slots__ = ("r", "g", "b", "a")

        def __init__(self):
            super().__init__()
            self.r = 0
            self.g = 0
            self.b = 0
            self.a = 0

    def to_c(self) -> Color.Struct:
        """Converts to C struct."""
        struct = Color.Struct()
        struct.r = self.r
        struct.g = self.g
        struct.b = self.b
        struct.a = self.a
        return struct

    @classmethod
    def from_c(cls, struct: Color.Struct) -> Color:
        """Converts from C struct."""
        return cls(struct.r, struct.g, struct.b, struct.a)


@dataclass(eq=True, order=True)
class Colorf(StructWrapper):
    """
    Wrapper for:
        struct nk_colorf {float r,g,b,a;};
    """

    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 0.0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("r", ctypes.c_float),
            ("g", ctypes.c_float),
            ("b", ctypes.c_float),
            ("a", ctypes.c_float),
        ]
        __slots__ = ("r", "g", "b", "a")

        def __init__(self):
            super().__init__()
            self.r = 0.0
            self.g = 0.0
            self.b = 0.0
            self.a = 0.0

    def to_c(self) -> Colorf.Struct:
        """Converts to C struct."""
        struct = Colorf.Struct()
        struct.r = self.r
        struct.g = self.g
        struct.b = self.b
        struct.a = self.a
        return struct

    @classmethod
    def from_c(cls, struct: Colorf.Struct) -> Colorf:
        """Converts from C struct."""
        return cls(struct.r, struct.g, struct.b, struct.a)


@dataclass(eq=True, order=True)
class Vec2(StructWrapper):
    """
    Wrapper for:
        struct nk_vec2 {float x,y;};
    """

    x: float = 0.0
    y: float = 0.0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("x", ctypes.c_float),
            ("y", ctypes.c_float),
        ]
        __slots__ = ("x", "y")

        def __init__(self):
            super().__init__()
            self.x = 0.0
            self.y = 0.0

    def to_c(self) -> Vec2.Struct:
        """Converts to C struct."""
        struct = Vec2.Struct()
        struct.x = self.x
        struct.y = self.y
        return struct

    @classmethod
    def from_c(cls, struct: Vec2.Struct) -> Vec2:
        """Converts from C struct."""
        return cls(struct.x, struct.y)


@dataclass(eq=True, order=True)
class Vec2i(StructWrapper):
    """
    Wrapper for:
        struct nk_vec2i {short x,y;};
    """

    x: int = 0
    y: int = 0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("x", ctypes.c_short),
            ("y", ctypes.c_short),
        ]
        __slots__ = ("x", "y")

        def __init__(self):
            super().__init__()
            self.x = 0
            self.y = 0

    def to_c(self) -> Vec2i.Struct:
        """Converts to C struct."""
        struct = Vec2i.Struct()
        struct.x = self.x
        struct.y = self.y
        return struct

    @classmethod
    def from_c(cls, struct: Vec2i.Struct) -> Vec2i:
        """Converts from C struct."""
        return cls(struct.x, struct.y)


@dataclass(eq=True, order=True)
class Rect(StructWrapper):
    """
    Wrapper for:
        struct nk_rect {float x,y,w,h;};
    """

    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    h: float = 0.0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("x", ctypes.c_float),
            ("y", ctypes.c_float),
            ("w", ctypes.c_float),
            ("h", ctypes.c_float),
        ]
        __slots__ = ("x", "y", "w", "h")

        def __init__(self):
            super().__init__()
            self.x = 0.0
            self.y = 0.0
            self.w = 0.0
            self.h = 0.0

    def to_c(self) -> Rect.Struct:
        """Converts to C struct."""
        struct = Rect.Struct()
        struct.x = self.x
        struct.y = self.y
        struct.w = self.w
        struct.h = self.h
        return struct

    @classmethod
    def from_c(cls, struct: Rect.Struct) -> Rect:
        """Converts from C struct."""
        return cls(struct.x, struct.y, struct.w, struct.h)


@dataclass(eq=True, order=True)
class Recti(StructWrapper):
    """
    Wrapper for:
        struct nk_recti {short x,y,w,h;};
    """

    x: int = 0
    y: int = 0
    w: int = 0
    h: int = 0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("x", ctypes.c_short),
            ("y", ctypes.c_short),
            ("w", ctypes.c_short),
            ("h", ctypes.c_short),
        ]
        __slots__ = ("x", "y", "w", "h")

        def __init__(self):
            super().__init__()
            self.x = 0
            self.y = 0
            self.w = 0
            self.h = 0

    def to_c(self) -> Recti.Struct:
        """Converts to C struct."""
        struct = Recti.Struct()
        struct.x = self.x
        struct.y = self.y
        struct.w = self.w
        struct.h = self.h
        return struct

    @classmethod
    def from_c(cls, struct: Recti.Struct) -> Recti:
        """Converts from C struct."""
        return cls(struct.x, struct.y, struct.w, struct.h)


class Glyph(StructWrapper.Struct):
    """
    Wrapper for:
        typedef char nk_glyph[NK_UTF_SIZE];
    """

    _fields_ = [("dummy", ctypes.c_char * UTF_SIZE)]


@dataclass(eq=True, order=True)
class Handle(StructWrapper):
    """
    Wrapper for:
        typedef union {void *ptr; int id;} nk_handle;
    """

    ptr: int = 0
    id: int = 0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("ptr", ctypes.c_void_p),
            ("id", ctypes.c_int),
        ]
        __slots__ = ("ptr", "id")

        def __init__(self):
            super().__init__()
            self.ptr = 0
            self.id = 0

    def to_c(self) -> Handle.Struct:
        """Converts to C struct."""
        struct = Handle.Struct()
        struct.ptr = self.ptr
        struct.id = self.id
        return struct

    @classmethod
    def from_c(cls, struct: Handle.Struct) -> Handle:
        """Converts from C struct."""
        return cls(struct.ptr, struct.id)


@dataclass(eq=True, order=True)
class Image(StructWrapper):
    """
    Wrapper for:
        struct nk_image {nk_handle handle; nk_ushort w, h; nk_ushort region[4];};
    """

    handle: Handle = field(default_factory=Handle)
    w: int = 0
    h: int = 0
    # region: Annotated[List[int], 4] = field(default_factory=lambda: [0, 0, 0, 0])
    region: List[int] = field(default_factory=lambda: [0, 0, 0, 0])

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("handle", Handle.Struct),
            ("w", UShort),
            ("h", UShort),
            ("region", UShort * 4),
        ]
        __slots__ = ("handle", "w", "h", "region")

        def __init__(self):
            super().__init__()
            self.handle = Handle.Struct()
            self.w = 0
            self.h = 0
            self.region = (UShort * 4)()

    def to_c(self) -> Image.Struct:
        """Converts to C struct."""
        struct = Image.Struct()
        struct.handle = self.handle.to_c()
        struct.w = self.w
        struct.h = self.h
        for i, r in enumerate(self.region):
            struct.region[i] = r
        return struct

    @classmethod
    def from_c(cls, struct: Image.Struct) -> Image:
        """Converts from C struct."""
        handle = Handle.from_c(struct.handle)
        region = [int(r) for r in struct.region]
        return cls(handle, struct.w, struct.h, region)


@dataclass(eq=True, order=True)
class NineSlice(StructWrapper):
    """
    Wrapper for:
        struct nk_nine_slice {struct nk_image img; nk_ushort l, t, r, b;};
    """

    img: Image = field(default_factory=Image)
    l: int = 0
    t: int = 0
    r: int = 0
    b: int = 0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("img", Image.Struct),
            ("l", UShort),
            ("t", UShort),
            ("r", UShort),
            ("b", UShort),
        ]
        __slots__ = ("img", "l", "t", "r", "b")

        def __init__(self):
            super().__init__()
            self.img = Image.Struct()
            self.l = 0
            self.t = 0
            self.r = 0
            self.b = 0

    def to_c(self) -> NineSlice.Struct:
        """Converts to C struct."""
        struct = NineSlice.Struct()
        struct.img = self.img.to_c()
        struct.l = self.l
        struct.t = self.t
        struct.r = self.r
        struct.b = self.b
        return struct

    @classmethod
    def from_c(cls, struct: NineSlice.Struct) -> NineSlice:
        """Converts from C struct."""
        img = Image.from_c(struct.image)
        return cls(img, struct.l, struct.t, struct.r, struct.b)


@dataclass(eq=True, order=True)
class Cursor(StructWrapper):
    """
    Wrapper for:
        struct nk_cursor {struct nk_image img; struct nk_vec2 size, offset;};
    """

    img: Image = field(default_factory=Image)
    size: Vec2 = field(default_factory=Vec2)
    offset: Vec2 = field(default_factory=Vec2)

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("img", Image.Struct),
            ("size", Vec2.Struct),
            ("offset", Vec2.Struct),
        ]

        def __init__(self):
            super().__init__()
            self.img = Image.Struct()
            self.size = Vec2.Struct()
            self.offset = Vec2.Struct()

    def to_c(self) -> Cursor.Struct:
        """Converts to C struct."""
        struct = Cursor.Struct()
        struct.img = self.img.to_c()
        struct.size = self.size.to_c()
        struct.offset = self.offset.to_c()
        return struct

    @classmethod
    def from_c(cls, struct: Cursor.Struct) -> Cursor:
        """Converts from C struct."""
        img = Image.from_c(struct.img)
        size = Vec2.from_c(struct.size)
        offset = Vec2.from_c(struct.offset)
        return cls(img, size, offset)


@dataclass(eq=True, order=True)
class Scroll(StructWrapper):
    """
    Wrapper for:
        struct nk_scroll {nk_uint x, y;};
    """

    x: int = 0
    y: int = 0

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("x", UInt),
            ("y", UInt),
        ]

        def __init__(self):
            super().__init__()
            self.x = 0
            self.y = 0

    def to_c(self) -> Scroll.Struct:
        """Converts to C struct."""
        struct = Scroll.Struct()
        struct.x = self.x
        struct.y = self.y
        return struct

    @classmethod
    def from_c(cls, struct: Scroll.Struct) -> Scroll:
        """Converts from C struct."""
        return cls(struct.x, struct.y)


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


PluginAlloc = Callable[[Handle, int, int], int]
PluginAlloc.CFunc = ctypes.CFUNCTYPE(
    ctypes.c_void_p, Handle.Struct, ctypes.c_void_p, Size
)

PluginFree = Callable[[Handle, int], None]
PluginFree.CFunc = ctypes.CFUNCTYPE(None, Handle.Struct, ctypes.c_void_p)


@dataclass(eq=True, order=True)
class Allocator(StructWrapper):
    """
    Wrapper for:
        struct nk_allocator {
            nk_handle userdata;
            nk_plugin_alloc alloc;
            nk_plugin_free free;
        };
    """

    userdata: Handle = field(default_factory=Handle)
    alloc: Optional[PluginAlloc] = None
    free: Optional[PluginFree] = None

    class Struct(StructWrapper.Struct):
        _fields_ = [
            ("userdata", Handle.Struct),
            ("alloc", PluginAlloc.CFunc),
            ("free", PluginFree.CFunc),
        ]

        def __init__(self):
            super().__init__()
            self.userdata = Handle.Struct()
            self.alloc = None
            self.free = None

    def to_c(self) -> Allocator.Struct:
        """Converts to C struct."""
        struct = Allocator.Struct()
        struct.userdata = self.userdata.to_c()
        struct.alloc = self.alloc
        struct.free = self.free
        return struct

    @classmethod
    def from_c(cls, struct: Allocator.Struct) -> Allocator:
        """Converts from C struct."""
        userdata = Handle.from_c(struct.userdata)
        return cls(userdata, struct.alloc, struct.free)


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


# TODO - Move this to where TextEdit is defined


@dataclass(eq=True, order=True)
class TextEdit(StructWrapper, ABC):
    """
    Forward declaration for:
        struct nk_text_edit;
    """

    class Struct(StructWrapper.Struct):
        pass


PluginFilter = Callable[[TextEdit, int], bool]
PluginFilter.CFunc = ctypes.CFUNCTYPE(Bool, ctypes.POINTER(TextEdit.Struct), Rune)

PluginPaste = ctypes.CFUNCTYPE(None, Handle.Struct, ctypes.POINTER(TextEdit.Struct))
PluginPaste.PluginPaste = Callable[[Handle, TextEdit], None]

PluginCopy = ctypes.CFUNCTYPE(None, Handle.Struct, ctypes.c_char_p, ctypes.c_int)
PluginCopy.PluginCopy = Callable[[Handle, int, int], None]
