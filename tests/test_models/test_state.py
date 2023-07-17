#!/usr/bin/python3
""" test module for User """


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ test cases for State """

    def test_init(self):
        b = State()

        self.assertIsInstance(b, State)
