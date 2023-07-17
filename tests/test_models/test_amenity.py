#!/usr/bin/python3
""" test module for amenity """


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ test cases for Amenity """

    def test_init(self):
        b = Amenity()

        self.assertIsInstance(b, Amenity)
