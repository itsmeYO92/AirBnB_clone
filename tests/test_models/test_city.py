#!/usr/bin/python3
""" test module for City """


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ test cases for User """

    def test_init(self):
        b = City()

        self.assertIsInstance(b, City)
