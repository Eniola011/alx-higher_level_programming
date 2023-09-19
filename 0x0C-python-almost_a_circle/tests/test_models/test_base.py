#!/usr/bin/python3
"""

Unittest for Base class

"""


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ Test Base class """
    def setUp(self):
        """ Invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_one(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_id_two(self):
        """ Test string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_privateattr(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_one(self):
        Square.save_to_file(None)
        jslist = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), jslist)

        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_two(self):
        Rectangle.save_to_file(None)
        jlist = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), jlist)
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")