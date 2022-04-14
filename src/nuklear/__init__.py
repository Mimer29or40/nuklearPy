from __future__ import annotations

from nuklear import color
from nuklear import types

# ==============================================================
#
#                          CONSTANTS
#
# ==============================================================

UNDEFINED = types.UNDEFINED
UTF_INVALID = types.UTF_INVALID
UTF_SIZE = types.UTF_SIZE
INPUT_MAX = types.INPUT_MAX
MAX_NUMBER_BUFFER = types.MAX_NUMBER_BUFFER
SCROLLBAR_HIDING_TIMEOUT = types.SCROLLBAR_HIDING_TIMEOUT

# ==============================================================================
#
#                                    BASIC
#
# ==============================================================================

Char = types.Char
uChar = types.UChar
Byte = types.Byte
Short = types.Short
uShort = types.UShort
Int = types.Int
uInt = types.UInt
Size = types.Size
Ptr = types.Ptr
Bool = types.Bool

Hash = types.Hash
Flags = types.Flags
Rune = types.Rune

# ==============================================================================
#
#                                  API
#
# ==============================================================================

false = types.false
true = types.true
Color = types.Color
Colorf = types.Colorf
Vec2 = types.Vec2
Vec2i = types.Vec2i
Rect = types.Rect
Recti = types.Recti
Glyph = types.Glyph
Handle = types.Handle
Image = types.Image
NineSlice = types.NineSlice
Cursor = types.Cursor
Scroll = types.Scroll

Heading = types.Heading
UP, RIGHT, DOWN, LEFT = Heading

ButtonBehavior = types.ButtonBehavior
DEFAULT, REPEATER = ButtonBehavior

Modify = types.Modify
FIXED, MODIFIABLE = Modify

Orientation = types.Orientation
VERTICAL, HORIZONTAL = Orientation

CollapseStates = types.CollapseStates
MINIMIZED, MAXIMIZED = CollapseStates

ShowStates = types.ShowStates
HIDDEN, SHOWN = ShowStates

ChartType = types.ChartType
CHART_LINES, CHART_COLUMN, CHART_MAX = ChartType

ChartEvent = types.ChartEvent
CHART_HOVERING, CHART_CLICKED = ChartEvent

ColorFormat = types.ColorFormat
RGB, RGBA = ColorFormat

PopupType = types.PopupType
POPUP_STATIC, POPUP_DYNAMIC = PopupType

LayoutFormat = types.LayoutFormat
DYNAMIC, STATIC = LayoutFormat

TreeType = types.TreeType
TREE_NODE, TREE_TAB = TreeType

PluginAlloc = types.PluginAlloc
PluginFree = types.PluginFree

Allocator = types.Allocator

SymbolType = types.SymbolType
(
    SYMBOL_NONE,
    SYMBOL_X,
    SYMBOL_UNDERSCORE,
    SYMBOL_CIRCLE_SOLID,
    SYMBOL_CIRCLE_OUTLINE,
    SYMBOL_RECT_SOLID,
    SYMBOL_RECT_OUTLINE,
    SYMBOL_TRIANGLE_UP,
    SYMBOL_TRIANGLE_DOWN,
    SYMBOL_TRIANGLE_LEFT,
    SYMBOL_TRIANGLE_RIGHT,
    SYMBOL_PLUS,
    SYMBOL_MINUS,
    SYMBOL_MAX,
) = SymbolType


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
#         nk_bool nk_init_fixed(struct nk_context*, void#   memory, nk_size size, const struct nk_user_font*);
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
#         nk_bool nk_init_custom(struct nk_context*, struct nk_buffer#   cmds, struct nk_buffer#   pool, const struct nk_user_font*);
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


# ==============================================================================
#
#                                     INPUT
#
# ==============================================================================


# ==============================================================================
#
#                                    DRAWING
#
# ==============================================================================


# ==============================================================================
#
#                                    WINDOW
#
# ==============================================================================


# ==============================================================================
#
#                                    LAYOUT
#
# ==============================================================================


# ==============================================================================
#
#                                    GROUP
#
# ==============================================================================


# ==============================================================================
#
#                                    TREE
#
# ==============================================================================


# ==============================================================================
#
#                                   LIST VIEW
#
# ==============================================================================


# ==============================================================================
#
#                                    WIDGET
#
# ==============================================================================


# ==============================================================================
#
#                                     TEXT
#
# ==============================================================================


# ==============================================================================
#
#                                    BUTTON
#
# ==============================================================================


# ==============================================================================
#
#                                    CHECKBOX
#
# ==============================================================================


# ==============================================================================
#
#                                  RADIO BUTTON
#
# ==============================================================================


# ==============================================================================
#
#                                   SELECTABLE
#
# ==============================================================================


# ==============================================================================
#
#                                     SLIDER
#
# ==============================================================================


# ==============================================================================
#
#                                   PROGRESSBAR
#
# ==============================================================================


# ==============================================================================
#
#                                   COLOR PICKER
#
# ==============================================================================


# ==============================================================================
#
#                                   PROPERTIES
#
#    =============================================================================


# ==============================================================================
#
#                                    TEXT EDIT
#
# ==============================================================================


# ==============================================================================
#
#                                     CHART
#
# ==============================================================================


# ==============================================================================
#
#                                     POPUP
#
# ==============================================================================


# ==============================================================================
#
#                                    COMBOBOX
#
# ==============================================================================


# ==============================================================================
#
#                                ABSTRACT COMBOBOX
#
# ==============================================================================


# ==============================================================================
#
#                                    CONTEXTUAL
#
# ==============================================================================


# ==============================================================================
#
#                                    TOOLTIP
#
# ==============================================================================


# ==============================================================================
#
#                                     MENU
#
# ==============================================================================


# ==============================================================================
#
#                                     STYLE
#
# ==============================================================================


# ==============================================================================
#
#                                     COLOR
#
# ==============================================================================

rgb = color.rgb
rgb_f = color.rgb_f
rgb_iv = color.rgb_iv
rgb_bv = color.rgb_bv
rgb_fv = color.rgb_fv
rgb_cf = color.rgb_cf

rgba = color.rgba
rgba_f = color.rgba_f
rgba_u32 = color.rgba_u32
rgba_iv = color.rgba_iv
rgba_bv = color.rgba_bv
rgba_fv = color.rgba_fv
rgba_cf = color.rgba_cf

rgb_hex = color.rgb_hex
rgba_hex = color.rgba_hex
color_hex_rgb = color.color_hex_rgb
color_hex_rgba = color.color_hex_rgba

hsv = color.hsv
hsv_f = color.hsv_f
hsv_iv = color.hsv_iv
hsv_bv = color.hsv_bv
hsv_fv = color.hsv_fv

hsva = color.hsva
hsva_f = color.hsva_f
hsva_iv = color.hsva_iv
hsva_bv = color.hsva_bv
hsva_fv = color.hsva_fv

hsva_colorf = color.hsva_colorf
hsva_colorfv = color.hsva_colorfv

color_f = color.color_f
color_d = color.color_d
color_u32 = color.color_u32
color_fv = color.color_fv
color_dv = color.color_dv
color_cf = color.color_cf

color_hsv_i = color.color_hsv_i
color_hsv_b = color.color_hsv_b
color_hsv_f = color.color_hsv_f
color_hsv_iv = color.color_hsv_iv
color_hsv_bv = color.color_hsv_bv
color_hsv_fv = color.color_hsv_fv

color_hsva_i = color.color_hsva_i
color_hsva_b = color.color_hsva_b
color_hsva_f = color.color_hsva_f
color_hsva_iv = color.color_hsva_iv
color_hsva_bv = color.color_hsva_bv
color_hsva_fv = color.color_hsva_fv

colorf_hsva_f = color.colorf_hsva_f
colorf_hsva_fv = color.colorf_hsva_fv

# ==============================================================================
#
#                                     IMAGE
#
# ==============================================================================


# ==============================================================================
#
#                                    9-SLICE
#
# ==============================================================================


# ==============================================================================
#
#                                     MATH
#
# ==============================================================================


# ==============================================================================
#
#                                     STRING
#
# ==============================================================================


# ==============================================================================
#
#                                     UTF-8
#
# ==============================================================================


# ==============================================================================
#
#                                      FONT
#
# ==============================================================================


# ==============================================================================
#
#                                  MEMORY BUFFER
#
# ==============================================================================


# ==============================================================================
#
#                                     STRING
#
# ==============================================================================


# ==============================================================================
#
#                                   TEXT EDITOR
#
# ==============================================================================


# ==============================================================================
#
#                                     DRAWING
#
# ==============================================================================


# ==============================================================================
#
#                                      INPUT
#
# ==============================================================================


# ==============================================================================
#
#                                    DRAW LIST
#
# ==============================================================================


# ==============================================================================
#
#                                       GUI
#
# ==============================================================================


# ==============================================================================
#
#                                     PANEL
#
# ==============================================================================


# ==============================================================================
#
#                                     WINDOW
#
# ==============================================================================


# ==============================================================================
#
#                                     STACK
#
# ==============================================================================


# ==============================================================================
#
#                                    CONTEXT
#
# ==============================================================================


# ==============================================================================
#
#                                     MATH
#
# ==============================================================================


# ==============================================================================
#
#                                   ALIGNMENT
#
# ==============================================================================
