#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Unit test for max_integer function"""

    def test_int(self):
        self.assertEqual(max_integer([9, 7, 5, 11]), 11)

    def test_negative_number(self):
        self.assertEqual(max_integer([-4, -6, -5, -2]), -2)

    def test_duplicate_number(self):
        self.assertEqual(max_integer([3, 8, 3, 8]), 8)

    def test_float_number(self):
        self.assertEqual(max_integer([10, 9, 11.5, 7]), 11.5)

    def test_strings(self):
        self.assertEqual(max_integer(["HI", "hi"]), "hi")

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_with_forloop(self):
        my_list = [2, 4, 6, 8]
        self.assertEqual(max_integer([el * 2 for el in my_list]), 16)

    def test_one_item(self):
        self.assertEqual(max_integer([11]), 11)

    def test_forzero(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_str_num(self):
        with self.assertRaises(TypeError):
            max_integer([12, '12'])

    def test_tuple(self):
        with self.asserRaises(TypeError):
            max_integer([11, (9, 8)])

    def test_dict(self):
        with self.assertRaises(KeyError):
            max_integer({'S1': 102, 'S2': 105})

    def test_num(self):
        with self.assertRaises(TypeError):
            max_integer(3)

if __name__ == '__main__':
    unittest.main()
