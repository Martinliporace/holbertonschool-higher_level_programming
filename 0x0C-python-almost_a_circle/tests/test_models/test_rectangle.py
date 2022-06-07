#!/usr/bin/python3
"""Unittest for rectangle"""

import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):


    """test width not int"""
    def test_width_is_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)



if __name__ == '__main__':
    unittest.main()
