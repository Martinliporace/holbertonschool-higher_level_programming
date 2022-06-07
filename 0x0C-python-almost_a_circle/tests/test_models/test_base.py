#!/usr/bin/python3
"""Unittest for base"""

import unittest
from models.base import Base


class Test_base(unittest.TestCase):

    """test id None"""
    def test_id_not_None(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_id_not_None(self):
        b1 = Base(90)
        self.assertEqual(b1.id, 90)


    def test_id_None(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)



if __name__ == '__main__':
    unittest.main()