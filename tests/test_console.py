#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage as stortage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):

    """Tests HBNBCommand console."""

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")

        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(s, f.getvalue())

    def test_do_EFO(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), "\n")


    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), "\n")

    def test_create(self):

        for _class in HBNBCommand.classes.keys():
            command = "create " + _class
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(command)
            self.assertNotEqual(f.getvalue(), "")
            _id = f.getvalue().strip("\n")
            
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all")
            self.assertTrue(_id in f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip("\n"), "** class name missing **")
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create foo")
            self.assertEqual(f.getvalue().strip("\n"), "** class doesn't exist **")
    
