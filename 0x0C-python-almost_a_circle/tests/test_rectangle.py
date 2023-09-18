#!/usr/bin/python3
"""

Unitest for Rectangle Class

"""


import unittest
import io
import sys
import models.rectangle import Rectangle
import models.base import Base


class test_instantation(unittest.Testcase):
    """ Test for __init__ method """
    def test_isrectangle_abase(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_argmt(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_for_one_argmt(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_for_two_argmt(self):
        r1 = Rectangle(10, 2)
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_for_three_argmt(self):
        r1 = Rectangle(2, 2, 4)
        r1 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_for_four_argmt(self):
        r1 = Rectangle(1, 2, 3, 4)
        r1 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_for_five_argmt(self):
        self.assertEqual(12, Rectangle(10, 2, 0, 0, 12).id)

    def test_more_than_five_argmt(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)
