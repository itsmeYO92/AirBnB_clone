#!/usr/bin/python3
""" test module for review"""


import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    """ test cases for Review """

    def test_init(self):
        b = Review()

        self.assertIsInstance(b, Review)
