#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """test for positive numbers"""
    def test_PositiveNumbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    """test for disorder list"""
    def test_DisorderList(self):
        self.assertEqual(max_integer([8, 2, 9, 120]), 120)

    """test for negative numbers"""
    def test_NegativeNumbers(self):
        self.assertEqual(max_integer([-8, -2, -9, -120]), -2)

    """test for one -number"""
    def test_OneNNumber(self):
        self.assertEqual(max_integer([-9]), -9)

    """test for empty list"""
    def test_EmptyList(self):
        self.assertEqual(max_integer([]), None)

    """test for same values"""
    def test_SameValues(self):
        self.assertEqual(max_integer([8, 8, 8, 8]), 8)

    """test for medium max"""
    def test_SameValues(self):
        self.assertEqual(max_integer([8, 8, 10, 8, 8]), 10)

    """test for same and different values"""
    def test_SameAndDifferentVal(self):
        self.assertEqual(max_integer([8, 120, 9, 120]), 120)

if __name__ == '__main__':
    unittest.main()
