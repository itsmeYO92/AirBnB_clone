#!/usr/bin/python3
""" test module for User """


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ test cases for User """

    def test_init(self):
        b = User()

        self.assertIsInstance(b, User)
