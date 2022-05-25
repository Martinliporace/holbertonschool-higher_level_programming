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

        if __name__ == '__main__':
    unittest.main()
