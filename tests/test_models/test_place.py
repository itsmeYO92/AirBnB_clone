#!/usr/bin/python3
""" test module for Place """


import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    """ test cases for Place """

    def test_init(self):
        b = Place()

        self.assertIsInstance(b, Place)
