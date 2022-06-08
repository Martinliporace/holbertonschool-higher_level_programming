#!/usr/bin/python3
"""Unittest for rectangle"""

import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):


    """test width int"""
    def test_width_is_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    """test width not int"""
    def test_width_not_int_str(self):
        r1 = Rectangle("H", 2)
        self.assertRaises(TypeError)

    """test width not int"""
    def test_width_not_int_flt(self):
        r1 = Rectangle(1.5, 2)
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
