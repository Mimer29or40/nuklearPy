import unittest

import nuklear as nk


class ColorModule(unittest.TestCase):
    def test_rgb(self):
        r, g, b = 100, -1, 256

        color = nk.rgb(r, g, b)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_rgb_f(self):
        r, g, b = 100.0 / 255.0, -0.1, 1.1

        color = nk.rgb_f(r, g, b)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_rgb_iv(self):
        rgb = 100, -1, 256

        color = nk.rgb_iv(rgb)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

        self.assertRaises(AssertionError, lambda: nk.rgb_iv((1, 2, 3, 4)))

    def test_rgb_bv(self):
        rgb = 100, -1, 256

        color = nk.rgb_bv(rgb)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 255)
        self.assertEqual(color.b, 0)

        self.assertRaises(AssertionError, lambda: nk.rgb_bv((1, 2, 3, 4)))

    def test_rgb_fv(self):
        rgb = 100.0 / 255.0, -0.1, 1.1

        color = nk.rgb_fv(rgb)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

        self.assertRaises(AssertionError, lambda: nk.rgb_fv((1.0, 2.0, 3.0, 4.0)))

    def test_rgb_cf(self):
        colorf = nk.Colorf(100.0 / 255.0, -0.1, 1.1, 1.0)

        color = nk.rgb_cf(colorf)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_rgba(self):
        r, g, b, a = 100, -1, 256, 200

        color = nk.rgba(r, g, b, a)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_rgba_f(self):
        r, g, b, a = 100.0 / 255.0, -0.1, 1.1, 200.0 / 255.0

        color = nk.rgba_f(r, g, b, a)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_rgba_u32(self):
        rgba = 0xC8FF0064

        color = nk.rgba_u32(rgba)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_rgba_iv(self):
        rgba = 100, -1, 256, 200

        color = nk.rgba_iv(rgba)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_rgba_bv(self):
        rgba = 100, -1, 256, 200

        color = nk.rgba_bv(rgba)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 255)
        self.assertEqual(color.b, 0)
        self.assertEqual(color.a, 200)

    def test_rgba_fv(self):
        rgba = 100.0 / 255.0, -0.1, 1.1, 200.0 / 255.0

        color = nk.rgba_fv(rgba)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_rgba_cf(self):
        colorf = nk.Colorf(100.0 / 255.0, -0.1, 1.1, 200.0 / 255.0)

        color = nk.rgba_cf(colorf)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_rgb_hex(self):
        hex = "6400FF"

        color = nk.rgb_hex(hex)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_rgba_hex(self):
        hex = "6400FFC8"

        color = nk.rgba_hex(hex)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_color_hex_rgb(self):
        color = nk.Color(100, 0, 255, 200)

        hex = nk.color_hex_rgb(color)
        self.assertEqual(hex, "6400FF")

    def test_color_hex_rgba(self):
        color = nk.Color(100, 0, 255, 200)

        hex = nk.color_hex_rgba(color)
        self.assertEqual(hex, "6400FFC8")

    def test_hsv(self):
        h, s, v = 187, 255, 255

        color = nk.hsv(h, s, v)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_hsv_f(self):
        h, s, v = 264 / 360, 1.0, 1.0

        color = nk.hsv_f(h, s, v)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_hsv_iv(self):
        hsv = 187, 255, 255

        color = nk.hsv_iv(hsv)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_hsv_bv(self):
        hsv = 187, 255, 255

        color = nk.hsv_bv(hsv)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_hsv_fv(self):
        hsv = 264 / 360, 1.0, 1.0

        color = nk.hsv_fv(hsv)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)

    def test_hsva(self):
        h, s, v, a = 187, 255, 255, 200

        color = nk.hsva(h, s, v, a)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_hsva_f(self):
        h, s, v, a = 264 / 360, 1.0, 1.0, 200 / 255

        color = nk.hsva_f(h, s, v, a)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_hsva_iv(self):
        hsva = 187, 255, 255, 200

        color = nk.hsva_iv(hsva)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_hsva_bv(self):
        hsva = 187, 255, 255, 200

        color = nk.hsva_bv(hsva)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_hsva_fv(self):
        hsva = 264 / 360, 1.0, 1.0, 200 / 255

        color = nk.hsva_fv(hsva)
        self.assertIsInstance(color, nk.Color)

        self.assertEqual(color.r, 102)
        self.assertEqual(color.g, 0)
        self.assertEqual(color.b, 255)
        self.assertEqual(color.a, 200)

    def test_hsva_colorf(self):
        h, s, v, a = 264 / 360, 1.0, 1.0, 200 / 255

        color = nk.hsva_colorf(h, s, v, a)
        self.assertIsInstance(color, nk.Colorf)

        self.assertAlmostEqual(color.r, 102 / 255, 4)
        self.assertAlmostEqual(color.g, 0 / 255, 4)
        self.assertAlmostEqual(color.b, 255 / 255, 4)
        self.assertAlmostEqual(color.a, 200 / 255, 4)

    def test_hsva_colorfv(self):
        hsva = 264 / 360, 1.0, 1.0, 200 / 255

        color = nk.hsva_colorfv(hsva)
        self.assertIsInstance(color, nk.Colorf)

        self.assertAlmostEqual(color.r, 102 / 255, 4)
        self.assertAlmostEqual(color.g, 0 / 255, 4)
        self.assertAlmostEqual(color.b, 255 / 255, 4)
        self.assertAlmostEqual(color.a, 200 / 255, 4)

    def test_color_f(self):
        color = nk.Color(100, 0, 255, 200)

        r, g, b, a = nk.color_f(color)

        self.assertAlmostEqual(r, 100 / 255, 4)
        self.assertAlmostEqual(g, 0 / 255, 4)
        self.assertAlmostEqual(b, 255 / 255, 4)
        self.assertAlmostEqual(a, 200 / 255, 4)

    def test_color_d(self):
        color = nk.Color(100, 0, 255, 200)

        r, g, b, a = nk.color_d(color)

        self.assertAlmostEqual(r, 100 / 255, 4)
        self.assertAlmostEqual(g, 0 / 255, 4)
        self.assertAlmostEqual(b, 255 / 255, 4)
        self.assertAlmostEqual(a, 200 / 255, 4)

    def test_color_u32(self):
        color = nk.Color(100, 0, 255, 200)

        u32 = nk.color_u32(color)
        self.assertEqual(u32, 0xC8FF0064)

    def test_color_fv(self):
        color = nk.Color(100, 0, 255, 200)

        r, g, b, a = nk.color_fv(color)

        self.assertAlmostEqual(r, 100 / 255, 4)
        self.assertAlmostEqual(g, 0 / 255, 4)
        self.assertAlmostEqual(b, 255 / 255, 4)
        self.assertAlmostEqual(a, 200 / 255, 4)

    def test_color_dv(self):
        color = nk.Color(100, 0, 255, 200)

        r, g, b, a = nk.color_dv(color)

        self.assertAlmostEqual(r, 100 / 255, 4)
        self.assertAlmostEqual(g, 0 / 255, 4)
        self.assertAlmostEqual(b, 255 / 255, 4)
        self.assertAlmostEqual(a, 200 / 255, 4)

    def test_color_cf(self):
        c = nk.Color(100, 0, 255, 200)

        color = nk.color_cf(c)
        self.assertIsInstance(color, nk.Colorf)

        self.assertAlmostEqual(color.r, 100 / 255, 4)
        self.assertAlmostEqual(color.g, 0 / 255, 4)
        self.assertAlmostEqual(color.b, 255 / 255, 4)
        self.assertAlmostEqual(color.a, 200 / 255, 4)

    def test_color_hsv_i(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v = nk.color_hsv_i(color)

        self.assertEqual(h, 186)
        self.assertEqual(s, 255)
        self.assertEqual(v, 255)

    def test_color_hsv_b(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v = nk.color_hsv_b(color)

        self.assertEqual(h, 186)
        self.assertEqual(s, 255)
        self.assertEqual(v, 255)

    def test_color_hsv_f(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v = nk.color_hsv_f(color)

        self.assertAlmostEqual(h, 187 / 255, 4)
        self.assertAlmostEqual(s, 255 / 255, 4)
        self.assertAlmostEqual(v, 255 / 255, 4)

    def test_color_hsv_iv(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v = nk.color_hsv_iv(color)

        self.assertEqual(h, 186)
        self.assertEqual(s, 255)
        self.assertEqual(v, 255)

    def test_color_hsv_bv(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v = nk.color_hsv_bv(color)

        self.assertEqual(h, 186)
        self.assertEqual(s, 255)
        self.assertEqual(v, 255)

    def test_color_hsv_fv(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v = nk.color_hsv_fv(color)

        self.assertAlmostEqual(h, 187 / 255, 4)
        self.assertAlmostEqual(s, 255 / 255, 4)
        self.assertAlmostEqual(v, 255 / 255, 4)

    def test_color_hsva_i(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v, a = nk.color_hsva_i(color)

        self.assertEqual(h, 186)
        self.assertEqual(s, 255)
        self.assertEqual(v, 255)
        self.assertEqual(a, 200)

    def test_color_hsva_b(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v, a = nk.color_hsva_b(color)

        self.assertEqual(h, 186)
        self.assertEqual(s, 255)
        self.assertEqual(v, 255)
        self.assertEqual(a, 200)

    def test_color_hsva_f(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v, a = nk.color_hsva_f(color)

        self.assertAlmostEqual(h, 187 / 255, 4)
        self.assertAlmostEqual(s, 255 / 255, 4)
        self.assertAlmostEqual(v, 255 / 255, 4)
        self.assertAlmostEqual(a, 200 / 255, 4)

    def test_color_hsva_iv(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v, a = nk.color_hsva_iv(color)

        self.assertEqual(h, 186)
        self.assertEqual(s, 255)
        self.assertEqual(v, 255)
        self.assertEqual(a, 200)

    def test_color_hsva_bv(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v, a = nk.color_hsva_bv(color)

        self.assertEqual(h, 186)
        self.assertEqual(s, 255)
        self.assertEqual(v, 255)
        self.assertEqual(a, 200)

    def test_color_hsva_fv(self):
        color = nk.Color(102, 0, 255, 200)

        h, s, v, a = nk.color_hsva_fv(color)

        self.assertAlmostEqual(h, 187 / 255, 4)
        self.assertAlmostEqual(s, 255 / 255, 4)
        self.assertAlmostEqual(v, 255 / 255, 4)
        self.assertAlmostEqual(a, 200 / 255, 4)

    def test_colorf_hsva_f(self):
        color = nk.Colorf(102 / 255, 0 / 255, 255 / 255, 200 / 255)

        h, s, v, a = nk.colorf_hsva_f(color)

        self.assertAlmostEqual(h, 187 / 255, 4)
        self.assertAlmostEqual(s, 255 / 255, 4)
        self.assertAlmostEqual(v, 255 / 255, 4)
        self.assertAlmostEqual(a, 200 / 255, 4)

    def test_colorf_hsva_fv(self):
        color = nk.Colorf(102 / 255, 0 / 255, 255 / 255, 200 / 255)

        h, s, v, a = nk.colorf_hsva_fv(color)

        self.assertAlmostEqual(h, 187 / 255, 4)
        self.assertAlmostEqual(s, 255 / 255, 4)
        self.assertAlmostEqual(v, 255 / 255, 4)
        self.assertAlmostEqual(a, 200 / 255, 4)


if __name__ == "__main__":
    unittest.main()
