#!/usr/bin/python3
"""

Unittest for Max_Integer Module

"""


class TestMaxInteger(unittest.TestCase):
    """Unit test for max_integer function"""

    def test_int(self):
        self.assertEqual(max_integer([9, 7, 5, 11), 11)

    def test_negative_number(self):
        self.assertEqual(max_integer([-4, -6, -5, -2]), -2)

    def test_duplicate_number(self):
        self.assertEqual(max_integer([3, 8, 3, 8]), 8)

    def test_float_number(self):
        self.assertEqual(max_integer([10, 9, 11.5, 7), 11.5)

    def test_strings(self):
        self.assertEqual(max_integer(["HI", "hi"), "hi")

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_with_forloop(self):
        my_list = [2, 4, 6, 8]
        self.assertEqual(max_integer([el * 2 for el in my_list]), 16)

    def test_one_item(self):
        self.assertEqual(max_integer([11]), 11)

    def test_		
