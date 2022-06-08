#!/usr/bin/python3
"""Unittest for base"""

import unittest
from models.base import Base


class Test_base(unittest.TestCase):

    """test id 89"""
    def test_id_not_89(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

        b2 = Base()
        self.assertEqual(b2.id, 1)

        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_str_id(self):
        b = Base("Holberton")
        self.assertEqual(b.id, "Holberton")

if __name__ == '__main__':
    unittest.main()
