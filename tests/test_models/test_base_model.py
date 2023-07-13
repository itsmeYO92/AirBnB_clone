#!/usr/bin/python3
""" Unittests module """


import unittest
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """ tests for the base model module """
    def testbasemodelcreation(self):
        """ check if the id is unique """
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertIsInstance(model1.id, str)
        self.assertNotEqual(model1.id, model2.id)
        self.assertEqual(model1.updated_at, model1.created_at)
        self.assertNotEqual(model2.updated_at, model1.created_at)

    def testsave(self):
        """ test save  method of the base model """
        model1 = BaseModel()
        updated_at = model1.updated_at
        model1.save()

        self.assertNotEqual(updated_at, model1.updated_at)
