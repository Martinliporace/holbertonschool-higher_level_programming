#!/usr/bin/python3
"""Unittest for base"""

import unittest
import pep8
from models.base import Base


class Test_base(unittest.TestCase):

    """test id None"""
    def test_id_not_None(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_id_None(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_type_error_str(self):
        b2 = Base("Holberton")
        self.assertRaises(TypeError)

    def test_type_error_float(self):
        b2 = Base(3.5)
        self.assertRaises(TypeError)

    def test_type_error_empty_list(self):
        b2 = Base([])
        self.assertRaises(TypeError)

    def test_type_error_list(self):
        b2 = Base([1, 2, 68])
        self.assertRaises(TypeError)

class TestCodeFormat(unittest.TestCase):
    """pep8"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files('models/base.py')
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()