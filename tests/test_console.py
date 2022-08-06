#!/usr/bin/python3
''' Test suite for the console'''


import sys
import pep8
import inspect
import models
import unittest
from io import StringIO
import console
from console import HBNBCommand
from unittest.mock import create_autospec


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


class TestHBNBCommand(unittest.TestCase):
    ''' Test the console module'''
    def setUp(self):
        '''setup for all tests of the console'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        '''Revert to the default state after all tests'''
        sys.stdout = self.backup

    def create(self):
        ''' create an instance of the HBNBCommand class'''
        return HBNBCommand()

    def test_quit(self):
        ''' Test that command quit exits the console'''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        ''' Test that command EOF works'''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_show(self):
        '''
            Test that command show works
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        self.assertTrue(str is type(x))

    def test_show_no_class_name(self):
        '''
            Test that command show returns error message if class
            name argument is missing.
        '''
        console = self.create()
        console.onecmd("show")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_show_class_name_does_not_exist(self):
        '''
            Testing that show wrong_class_name command returns error
            message if wrong class name argument is passed.
        '''
        console = self.create()
        console.onecmd("show Tricky")
        x = (self.capt_out.getvalue())
        self.assertTrue("** class doesn't exist **\n", x)

    def test_show_no_id(self):
        '''
            Test that command show returns message error if id argument
            is missing
        '''
        console = self.create()
        console.onecmd("show User")
        x = (self.capt_out.getvalue())
        self.assertEqual("** instance id missing **\n", x)

    def test_show_no_instance(self):
        '''
            Test that command show returns error message if instance
            is missing
        '''
        console = self.create()
        console.onecmd("show User 124356876")
        x = (self.capt_out.getvalue())
        self.assertEqual("** no instance found **\n", x)

    def test_create(self):
        '''
            Test that command create works
        '''
        console = self.create()
        console.onecmd("create Place")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_create_no_class_name(self):
        '''
            Test that command create returns error messages if class name
            argument is missing.
        '''
        console = self.create()
        console.onecmd("create")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_create_class_name_does_not_exist(self):
        '''
            Testing that create command returns error message if wrong
            class name argument is passed.
        '''
        console = self.create()
        console.onecmd("create Partey")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)

    def test_all(self):
        ''' Test that command all works'''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_all_class_name(self):
        '''
            Test that command all class_name returns a list of objects
            of type class_name
        '''
        console = self.create()
        console.onecmd("all User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_all_class_name_does_not_exist(self):
        '''
            Test that command all class_name returns a list of objects
            of type class_name
        '''
        console = self.create()
        console.onecmd("all Brick")
        x = (self.capt_out.getvalue())
        self.assertTrue("** class doesn't exist **\n", x)

    def test_update(self):
        '''Test that command update works'''
        console = self.create()
        console.onecmd("create State")
        state_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd(f"update State {state_id} id 123456")
        console.onecmd(f"show State {state_id}")
        x = (self.capt_out.getvalue())
        self.assertEqual("123456", x[9:15])

    def test_update_class_name_does_not_exist(self):
        '''
            Test that command update wrong class_name returns an error
        '''
        console = self.create()
        console.onecmd("update Brick")
        x = (self.capt_out.getvalue())
        self.assertTrue("** class doesn't exist **\n", x)

    def test_update_no_id(self):
        '''
            Test that command update returns error message
            if instance id is missing
        '''
        console = self.create()
        console.onecmd("update State")
        x = (self.capt_out.getvalue())
        self.assertTrue("** instance id missing **\n", x)

    def test_update_wrong_id(self):
        '''
            Test that command {update class_name id} returns error message
            if instance id is wrong
        '''
        console = self.create()
        console.onecmd("update State 123456")
        x = (self.capt_out.getvalue())
        self.assertTrue("** no instance found **\n", x)

    def test_update_no_attribute_name(self):
        '''
            Test that command update returns error message
            if attribute name is missing
        '''
        console = self.create()
        console.onecmd("create State")
        state_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd(f"update State {state_id}")
        x = (self.capt_out.getvalue())
        self.assertTrue("** attribute name missing **\n", x)

    def test_update_no_attribute_value(self):
        '''
            Test that command update returns error message
            if attribute value is missing
        '''
        console = self.create()
        console.onecmd("create State")
        state_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd(f"update State {state_id} id")
        x = (self.capt_out.getvalue())
        self.assertTrue("** value missing **\n", x)

    def test_destroy(self):
        '''Test that command {destroy class_name id} works'''
        console = self.create()
        console.onecmd("create State")
        state_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd(f"destroy State {state_id}")
        console.onecmd(f"show State {state_id}")
        x = (self.capt_out.getvalue())
        self.assertTrue("** no instance found **\n", x)

    def test_destroy_class_name_does_not_exist(self):
        '''
            Test that command {destroy wrong class_name} returns an error
        '''
        console = self.create()
        console.onecmd("destroy Chuck")
        x = (self.capt_out.getvalue())
        self.assertTrue("** class doesn't exist **\n", x)

    def test_destroy_no_class_name(self):
        '''
            Test that command {destroy} returns error message
            if instance id is missing
        '''
        console = self.create()
        console.onecmd("destroy")
        x = (self.capt_out.getvalue())
        self.assertTrue("** class name missing **\n", x)

    def test_destroy_no_id(self):
        '''
            Test that command {destroy class_name} returns error message
            if instance id is missing
        '''
        console = self.create()
        console.onecmd("destroy State")
        x = (self.capt_out.getvalue())
        self.assertTrue("** instance id missing **\n", x)

    def test_destroy_wrong_id(self):
        '''
            Test that command {destroy class_name id} returns error message
            if instance id is wrong
        '''
        console = self.create()
        console.onecmd("destroy State 123456")
        x = (self.capt_out.getvalue())
        self.assertTrue("** no instance found **\n", x)

    def test_count(self):
        '''Test that command {count class_name} works'''
        console = self.create()
        console.onecmd("create State")
        console.onecmd("create State")
        console.onecmd("create Place")
        console.onecmd("count State")
        x = (self.capt_out.getvalue())
        self.assertTrue("2", x)

    def test_count_no_class_name_arg(self):
        '''
            Test that command {count} returns an error
        '''
        console = self.create()
        console.onecmd("count")
        x = (self.capt_out.getvalue())
        self.assertTrue("** class doesn't exist **\n", x)

    def test_count_wrong_class_name_arg(self):
        '''
            Test that command {count wrong class_name} returns an error
        '''
        console = self.create()
        console.onecmd("count Cherry")
        x = (self.capt_out.getvalue())
        self.assertTrue("** class doesn't exist **\n", x)
