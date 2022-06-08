#!/usr/bin/python3
"""Unittest for rectangle"""

import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):

    """test width int"""
    def test_width_is_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    """test height int"""
    def test_height_is_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)


    """test id"""
    def test_id(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)


if __name__ == '__main__':
    unittest.main()
