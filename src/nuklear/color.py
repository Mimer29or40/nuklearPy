import ctypes
from typing import Collection, Tuple

from nuklear.library import from_char_p
from nuklear.library import nuklear as nk
from nuklear.library import to_char_p
from nuklear.types import Byte
from nuklear.types import Color
from nuklear.types import Colorf
from nuklear.types import UInt

# ==============================================================================
#
#                                    COLOR
#
# ==============================================================================

nk.nk_rgb.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
nk.nk_rgb.restype = Color.Struct


def rgb(r: int, g: int, b: int) -> Color:
    return Color.from_c(nk.nk_rgb(r, g, b))


nk.nk_rgb_f.argtypes = (ctypes.c_float, ctypes.c_float, ctypes.c_float)
nk.nk_rgb_f.restype = Color.Struct


def rgb_f(r: float, g: float, b: float) -> Color:
    return Color.from_c(nk.nk_rgb_f(r, g, b))


nk.nk_rgb_iv.argtypes = (ctypes.POINTER(ctypes.c_int),)
nk.nk_rgb_iv.restype = Color.Struct


def rgb_iv(rgb: Collection[int]) -> Color:
    assert len(rgb) == 3
    array = (ctypes.c_int * 3)()
    for i, v in enumerate(rgb):
        array[i] = v
    return Color.from_c(nk.nk_rgb_iv(array))


nk.nk_rgb_bv.argtypes = (ctypes.POINTER(Byte),)
nk.nk_rgb_bv.restype = Color.Struct


def rgb_bv(rgb: Collection[int]) -> Color:
    assert len(rgb) == 3
    array = (Byte * 3)()
    for i, v in enumerate(rgb):
        array[i] = v
    return Color.from_c(nk.nk_rgb_bv(array))


nk.nk_rgb_fv.argtypes = (ctypes.POINTER(ctypes.c_float),)
nk.nk_rgb_fv.restype = Color.Struct


def rgb_fv(rgb: Collection[float]) -> Color:
    assert len(rgb) == 3
    array = (ctypes.c_float * 3)()
    for i, v in enumerate(rgb):
        array[i] = v
    return Color.from_c(nk.nk_rgb_fv(array))


nk.nk_rgb_cf.argtypes = (Colorf.Struct,)
nk.nk_rgb_cf.restype = Color.Struct


def rgb_cf(c: Colorf) -> Color:
    return Color.from_c(nk.nk_rgb_cf(c.to_c()))


nk.nk_rgba.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
nk.nk_rgba.restype = Color.Struct


def rgba(r: int, g: int, b: int, a: int) -> Color:
    return Color.from_c(nk.nk_rgba(r, g, b, a))


nk.nk_rgba_f.argtypes = (ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)
nk.nk_rgba_f.restype = Color.Struct


def rgba_f(r: float, g: float, b: float, a: float) -> Color:
    return Color.from_c(nk.nk_rgba_f(r, g, b, a))


nk.nk_rgba_u32.argtypes = (UInt,)
nk.nk_rgba_u32.restype = Color.Struct


def rgba_u32(rgba: int) -> Color:
    return Color.from_c(nk.nk_rgba_u32(rgba))


nk.nk_rgba_iv.argtypes = (ctypes.POINTER(ctypes.c_int),)
nk.nk_rgba_iv.restype = Color.Struct


def rgba_iv(rgba: Collection[int]) -> Color:
    assert len(rgba) == 4
    array = (ctypes.c_int * 4)()
    for i, v in enumerate(rgba):
        array[i] = v
    return Color.from_c(nk.nk_rgba_iv(array))


nk.nk_rgba_bv.argtypes = (ctypes.POINTER(Byte),)
nk.nk_rgba_bv.restype = Color.Struct


def rgba_bv(rgba: Collection[int]) -> Color:
    assert len(rgba) == 4
    array = (Byte * 4)()
    for i, v in enumerate(rgba):
        array[i] = v
    return Color.from_c(nk.nk_rgba_bv(array))


nk.nk_rgba_fv.argtypes = (ctypes.POINTER(ctypes.c_float),)
nk.nk_rgba_fv.restype = Color.Struct


def rgba_fv(rgba: Collection[float]) -> Color:
    assert len(rgba) == 4
    array = (ctypes.c_float * 4)()
    for i, v in enumerate(rgba):
        array[i] = v
    return Color.from_c(nk.nk_rgba_fv(array))


nk.nk_rgba_cf.argtypes = (Colorf.Struct,)
nk.nk_rgba_cf.restype = Color.Struct


def rgba_cf(c: Colorf) -> Color:
    return Color.from_c(nk.nk_rgba_cf(c.to_c()))


nk.nk_rgb_hex.argtypes = (ctypes.c_char_p,)
nk.nk_rgb_hex.restype = Color.Struct


def rgb_hex(rgb: str) -> Color:
    return Color.from_c(nk.nk_rgb_hex(to_char_p(rgb)))


nk.nk_rgba_hex.argtypes = (ctypes.c_char_p,)
nk.nk_rgba_hex.restype = Color.Struct


def rgba_hex(rgba: str) -> Color:
    return Color.from_c(nk.nk_rgba_hex(to_char_p(rgba)))


nk.nk_color_hex_rgb.argtypes = (ctypes.c_char_p, Color.Struct)
nk.nk_color_hex_rgb.restype = None


def color_hex_rgb(color: Color) -> str:
    output = ctypes.c_char_p(to_char_p("000000"))

    nk.nk_color_hex_rgb(output, color.to_c())
    return from_char_p(output.value)


nk.nk_color_hex_rgba.argtypes = (ctypes.c_char_p, Color.Struct)
nk.nk_color_hex_rgba.restype = None


def color_hex_rgba(color: Color) -> str:
    output = ctypes.c_char_p(to_char_p("00000000"))

    nk.nk_color_hex_rgba(output, color.to_c())
    return from_char_p(output.value)


nk.nk_hsv.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
nk.nk_hsv.restype = Color.Struct


def hsv(h: int, s: int, v: int) -> Color:
    return Color.from_c(nk.nk_hsv(h, s, v))


nk.nk_hsv_f.argtypes = (ctypes.c_float, ctypes.c_float, ctypes.c_float)
nk.nk_hsv_f.restype = Color.Struct


def hsv_f(h: float, s: float, v: float) -> Color:
    return Color.from_c(nk.nk_hsv_f(h, s, v))


nk.nk_hsv_iv.argtypes = (ctypes.POINTER(ctypes.c_int),)
nk.nk_hsv_iv.restype = Color.Struct


def hsv_iv(hsv: Collection[int]) -> Color:
    assert len(hsv) == 3
    array = (ctypes.c_int * 3)()
    for i, v in enumerate(hsv):
        array[i] = v
    return Color.from_c(nk.nk_hsv_iv(array))


nk.nk_hsv_bv.argtypes = (ctypes.POINTER(Byte),)
nk.nk_hsv_bv.restype = Color.Struct


def hsv_bv(hsv: Collection[int]) -> Color:
    assert len(hsv) == 3
    array = (Byte * 3)()
    for i, v in enumerate(hsv):
        array[i] = v
    return Color.from_c(nk.nk_hsv_bv(array))


nk.nk_hsv_fv.argtypes = (ctypes.POINTER(ctypes.c_float),)
nk.nk_hsv_fv.restype = Color.Struct


def hsv_fv(hsv: Collection[float]) -> Color:
    assert len(hsv) == 3
    array = (ctypes.c_float * 3)()
    for i, v in enumerate(hsv):
        array[i] = v
    return Color.from_c(nk.nk_hsv_fv(array))


nk.nk_hsva.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
nk.nk_hsva.restype = Color.Struct


def hsva(h: int, s: int, v: int, a: int) -> Color:
    return Color.from_c(nk.nk_hsva(h, s, v, a))


nk.nk_hsva_f.argtypes = (ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)
nk.nk_hsva_f.restype = Color.Struct


def hsva_f(h: float, s: float, v: float, a: float) -> Color:
    return Color.from_c(nk.nk_hsva_f(h, s, v, a))


nk.nk_hsva_iv.argtypes = (ctypes.POINTER(ctypes.c_int),)
nk.nk_hsva_iv.restype = Color.Struct


def hsva_iv(hsva: Collection[int]) -> Color:
    assert len(hsva) == 4
    array = (ctypes.c_int * 4)()
    for i, v in enumerate(hsva):
        array[i] = v
    return Color.from_c(nk.nk_hsva_iv(array))


nk.nk_hsva_bv.argtypes = (ctypes.POINTER(Byte),)
nk.nk_hsva_bv.restype = Color.Struct


def hsva_bv(hsva: Collection[int]) -> Color:
    assert len(hsva) == 4
    array = (Byte * 4)()
    for i, v in enumerate(hsva):
        array[i] = v
    return Color.from_c(nk.nk_hsva_bv(array))


nk.nk_hsva_fv.argtypes = (ctypes.POINTER(ctypes.c_float),)
nk.nk_hsva_fv.restype = Color.Struct


def hsva_fv(hsv: Collection[float]) -> Color:
    assert len(hsv) == 4
    array = (ctypes.c_float * 4)()
    for i, v in enumerate(hsv):
        array[i] = v
    return Color.from_c(nk.nk_hsva_fv(array))


nk.nk_hsva_colorf.argtypes = (
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
)
nk.nk_hsva_colorf.restype = Colorf.Struct


def hsva_colorf(r: float, g: float, b: float, a: float) -> Colorf:
    return Colorf.from_c(nk.nk_hsva_colorf(r, g, b, a))


nk.nk_hsva_colorfv.argtypes = (ctypes.POINTER(ctypes.c_float),)
nk.nk_hsva_colorfv.restype = Colorf.Struct


def hsva_colorfv(hsva: Collection[float]) -> Colorf:
    assert len(hsva) == 4
    array = (ctypes.c_float * 4)()
    for i, v in enumerate(hsva):
        array[i] = v
    return Colorf.from_c(nk.nk_hsva_colorfv(array))


nk.nk_color_f.argtypes = (
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    Color.Struct,
)
nk.nk_color_f.restype = None


def color_f(color: Color) -> Tuple[float, float, float, float]:
    out_r = ctypes.c_float(0.0)
    out_g = ctypes.c_float(0.0)
    out_b = ctypes.c_float(0.0)
    out_a = ctypes.c_float(0.0)

    nk.nk_color_f(
        ctypes.pointer(out_r),
        ctypes.pointer(out_g),
        ctypes.pointer(out_b),
        ctypes.pointer(out_a),
        color.to_c(),
    )
    return out_r.value, out_g.value, out_b.value, out_a.value


nk.nk_color_d.argtypes = (
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    Color.Struct,
)
nk.nk_color_d.restype = None


def color_d(color: Color) -> Tuple[float, float, float, float]:
    out_r = ctypes.c_double(0.0)
    out_g = ctypes.c_double(0.0)
    out_b = ctypes.c_double(0.0)
    out_a = ctypes.c_double(0.0)

    nk.nk_color_d(
        ctypes.pointer(out_r),
        ctypes.pointer(out_g),
        ctypes.pointer(out_b),
        ctypes.pointer(out_a),
        color.to_c(),
    )
    return out_r.value, out_g.value, out_b.value, out_a.value


nk.nk_color_u32.argtypes = (Color.Struct,)
nk.nk_color_u32.restype = UInt


def color_u32(color: Color) -> int:
    return nk.nk_color_u32(color.to_c())


nk.nk_color_fv.argtypes = (ctypes.POINTER(ctypes.c_float), Color.Struct)
nk.nk_color_fv.restype = None


def color_fv(color: Color) -> Tuple[float, float, float, float]:
    rgba = (ctypes.c_float * 4)()

    nk.nk_color_fv(rgba, color.to_c())
    return rgba[0], rgba[1], rgba[2], rgba[3]


nk.nk_color_dv.argtypes = (ctypes.POINTER(ctypes.c_double), Color.Struct)
nk.nk_color_dv.restype = None


def color_dv(color: Color) -> Tuple[float, float, float, float]:
    rgba = (ctypes.c_double * 4)()

    nk.nk_color_dv(rgba, color.to_c())
    return rgba[0], rgba[1], rgba[2], rgba[3]


nk.nk_color_cf.argtypes = (Color.Struct,)
nk.nk_color_cf.restype = Colorf.Struct


def color_cf(color: Color) -> Colorf:
    return Colorf.from_c(nk.nk_color_cf(color.to_c()))


nk.nk_color_hsv_i.argtypes = (
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    Color.Struct,
)
nk.nk_color_hsv_i.restype = None


def color_hsv_i(color: Color) -> Tuple[int, int, int]:
    out_h = ctypes.c_int(0)
    out_s = ctypes.c_int(0)
    out_v = ctypes.c_int(0)

    nk.nk_color_hsv_i(
        ctypes.pointer(out_h),
        ctypes.pointer(out_s),
        ctypes.pointer(out_v),
        color.to_c(),
    )
    return out_h.value, out_s.value, out_v.value


nk.nk_color_hsv_b.argtypes = (
    ctypes.POINTER(Byte),
    ctypes.POINTER(Byte),
    ctypes.POINTER(Byte),
    Color.Struct,
)
nk.nk_color_hsv_b.restype = None


def color_hsv_b(color: Color) -> Tuple[int, int, int]:
    out_h = Byte(0)
    out_s = Byte(0)
    out_v = Byte(0)

    nk.nk_color_hsv_b(
        ctypes.pointer(out_h),
        ctypes.pointer(out_s),
        ctypes.pointer(out_v),
        color.to_c(),
    )
    return out_h.value, out_s.value, out_v.value


nk.nk_color_hsv_f.argtypes = (
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    Color.Struct,
)
nk.nk_color_hsv_f.restype = None


def color_hsv_f(color: Color) -> Tuple[float, float, float]:
    out_h = ctypes.c_float(0)
    out_s = ctypes.c_float(0)
    out_v = ctypes.c_float(0)

    nk.nk_color_hsv_f(
        ctypes.pointer(out_h),
        ctypes.pointer(out_s),
        ctypes.pointer(out_v),
        color.to_c(),
    )
    return out_h.value, out_s.value, out_v.value


nk.nk_color_hsv_iv.argtypes = (ctypes.POINTER(ctypes.c_int), Color.Struct)
nk.nk_color_hsv_iv.restype = None


def color_hsv_iv(color: Color) -> Tuple[int, int, int]:
    hsv = (ctypes.c_int * 3)()

    nk.nk_color_hsv_iv(hsv, color.to_c())
    return hsv[0], hsv[1], hsv[2]


nk.nk_color_hsv_bv.argtypes = (ctypes.POINTER(Byte), Color.Struct)
nk.nk_color_hsv_bv.restype = None


def color_hsv_bv(color: Color) -> Tuple[int, int, int]:
    hsv = (Byte * 3)()

    nk.nk_color_hsv_bv(hsv, color.to_c())
    return hsv[0], hsv[1], hsv[2]


nk.nk_color_hsv_fv.argtypes = (ctypes.POINTER(ctypes.c_float), Color.Struct)
nk.nk_color_hsv_fv.restype = None


def color_hsv_fv(color: Color) -> Tuple[float, float, float]:
    hsv = (ctypes.c_float * 3)()

    nk.nk_color_hsv_fv(hsv, color.to_c())
    return hsv[0], hsv[1], hsv[2]


nk.nk_color_hsva_i.argtypes = (
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    Color.Struct,
)
nk.nk_color_hsva_i.restype = None


def color_hsva_i(color: Color) -> Tuple[int, int, int, int]:
    out_h = ctypes.c_int(0)
    out_s = ctypes.c_int(0)
    out_v = ctypes.c_int(0)
    out_a = ctypes.c_int(0)

    nk.nk_color_hsva_i(
        ctypes.pointer(out_h),
        ctypes.pointer(out_s),
        ctypes.pointer(out_v),
        ctypes.pointer(out_a),
        color.to_c(),
    )
    return out_h.value, out_s.value, out_v.value, out_a.value


nk.nk_color_hsva_b.argtypes = (
    ctypes.POINTER(Byte),
    ctypes.POINTER(Byte),
    ctypes.POINTER(Byte),
    ctypes.POINTER(Byte),
    Color.Struct,
)
nk.nk_color_hsva_b.restype = None


def color_hsva_b(color: Color) -> Tuple[int, int, int, int]:
    out_h = Byte(0)
    out_s = Byte(0)
    out_v = Byte(0)
    out_a = Byte(0)

    nk.nk_color_hsva_b(
        ctypes.pointer(out_h),
        ctypes.pointer(out_s),
        ctypes.pointer(out_v),
        ctypes.pointer(out_a),
        color.to_c(),
    )
    return out_h.value, out_s.value, out_v.value, out_a.value


nk.nk_color_hsva_f.argtypes = (
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    Color.Struct,
)
nk.nk_color_hsva_f.restype = None


def color_hsva_f(color: Color) -> Tuple[float, float, float, float]:
    out_h = ctypes.c_float(0)
    out_s = ctypes.c_float(0)
    out_v = ctypes.c_float(0)
    out_a = ctypes.c_float(0)

    nk.nk_color_hsva_f(
        ctypes.pointer(out_h),
        ctypes.pointer(out_s),
        ctypes.pointer(out_v),
        ctypes.pointer(out_a),
        color.to_c(),
    )
    return out_h.value, out_s.value, out_v.value, out_a.value


nk.nk_color_hsva_iv.argtypes = (ctypes.POINTER(ctypes.c_int), Color.Struct)
nk.nk_color_hsva_iv.restype = None


def color_hsva_iv(color: Color) -> Tuple[int, int, int, int]:
    hsva = (ctypes.c_int * 4)()

    nk.nk_color_hsva_iv(hsva, color.to_c())
    return hsva[0], hsva[1], hsva[2], hsva[3]


nk.nk_color_hsva_bv.argtypes = (ctypes.POINTER(Byte), Color.Struct)
nk.nk_color_hsva_bv.restype = None


def color_hsva_bv(color: Color) -> Tuple[int, int, int, int]:
    hsva = (Byte * 4)()

    nk.nk_color_hsva_bv(hsva, color.to_c())
    return hsva[0], hsva[1], hsva[2], hsva[3]


nk.nk_color_hsva_fv.argtypes = (ctypes.POINTER(ctypes.c_float), Color.Struct)
nk.nk_color_hsva_fv.restype = None


def color_hsva_fv(color: Color) -> Tuple[float, float, float, float]:
    hsva = (ctypes.c_float * 4)()

    nk.nk_color_hsva_fv(hsva, color.to_c())
    return hsva[0], hsva[1], hsva[2], hsva[3]


nk.nk_colorf_hsva_f.argtypes = (
        ctypes.POINTER(ctypes.c_float),
        ctypes.POINTER(ctypes.c_float),
        ctypes.POINTER(ctypes.c_float),
        ctypes.POINTER(ctypes.c_float),
        Colorf.Struct,
    )
nk.nk_colorf_hsva_f.restype = None


def colorf_hsva_f(color: Colorf) -> Tuple[float, float, float, float]:
    out_h = ctypes.c_float(0.0)
    out_s = ctypes.c_float(0.0)
    out_v = ctypes.c_float(0.0)
    out_a = ctypes.c_float(0.0)

    nk.nk_colorf_hsva_f(
        ctypes.pointer(out_h),
        ctypes.pointer(out_s),
        ctypes.pointer(out_v),
        ctypes.pointer(out_a),
        color.to_c(),
    )
    return out_h.value, out_s.value, out_v.value, out_a.value


nk.nk_colorf_hsva_fv.argtypes = (ctypes.POINTER(ctypes.c_float), Colorf.Struct)
nk.nk_colorf_hsva_fv.restype = None


def colorf_hsva_fv(color: Colorf) -> Tuple[float, float, float, float]:
    hsva = (ctypes.c_float * 4)()

    nk.nk_colorf_hsva_fv(hsva, color.to_c())
    return hsva[0], hsva[1], hsva[2], hsva[3]
