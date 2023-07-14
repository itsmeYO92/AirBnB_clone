#!/usr/bin/python3
""" storage engine unittest module """


import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class FileStorageTests(unittest.TestCase):
    """ test for the file storage engine """

    def testFileStorage(self):
        model1 = BaseModel()

        key = type(model1).__name__ + "." + model1.id

        self.assertIn(key, storage.all().keys())
