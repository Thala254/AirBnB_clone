#!/usr/bin/python3
''' Test suite for the console'''


import sys
import os
import pep8
import inspect
import models
import unittest
from io import StringIO
import console
from console import HBNBCommand
from unittest.mock import patch


class TestConsoleDocs(unittest.TestCase):
    """Tests to check the documentation and style of HBNBCommand class"""
    def test_pep8_style_base(self):
        """Test that console.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
                                        'tests/test_console.py'
                                      ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the BaseModel class docstring"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.default_exec.__doc__)


class TestHBNBCommand(unittest.TestCase):
    ''' Test the console module'''
    @classmethod
    def setUp(self):
        '''setup for all tests of the console'''
        self.console = HBNBCommand()

    @classmethod
    def tearDown(self):
        '''Revert to the default state after all tests'''
        try:
            os.remove('file.json')
        except Exception:
            pass
        del self.console

    def teardown(self):
        '''Removes temporary JSON file created'''
        try:
            os.remove('file.json')
        except Exception:
            pass
        del self.console

    def test_quit(self):
        ''' Test that command quit exits the console'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_EOF(self):
        ''' Test that command EOF works'''
        self.assertTrue(self.console.onecmd("EOF"))

    def test_show(self):
        '''
            Test that command show works
        '''
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show School")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Amenity 1234-abc")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            user_id = f.getvalue()
        user_id = user_id[user_id.find('(') + 1: user_id.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {user_id}")
            self.assertEqual("[User]", f.getvalue()[:6])

    def test_create(self):
        '''
        test that command create works
        '''
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Babayao")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User name='Kim'")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertEqual("[[User]", f.getvalue()[:7])

    def test_all(self):
        ''' Test that command all works'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Brick")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Review")
            self.assertEqual("[]\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("all User")
            self.assertTrue(len(f.getvalue()) >= 2)
            self.console.onecmd("all")
            self.assertTrue(len(f.getvalue()) >= 1)

    def test_update(self):
        '''Test that command update works'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Chick")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Place")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Place 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            user_id = f.getvalue()
        ob_id = user_id[user_id.find('(') + 1: user_id.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User " + ob_id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User " + ob_id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())

    def test_destroy(self):
        '''Test that command {destroy class_name id} works'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Tree")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Review")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Place 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_count(self):
        '''Test that command {count class_name} works'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count Pigs")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count Place")
            self.assertEqual('0\n', f.getvalue())
