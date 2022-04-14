import unittest

import nuklear as nk
from nuklear.types import Color


class StructTests(unittest.TestCase):
    def test_Color(self):
        color = Color(0, 1, -1, 256)
        print(color, repr(color))
        print(color.r, type(color.r))
        _color = color.to_c()
        print(_color, repr(_color))
        print(_color.r, type(_color.r))
        __color = Color.from_c(_color)
        print(__color, repr(__color))
        print(__color.r, type(__color.r))

        c = nk.rgb_hex("AABB55")
        r = nk.color_hex_rgba(c)
        print(r, type(r))


if __name__ == "__main__":
    unittest.main()
