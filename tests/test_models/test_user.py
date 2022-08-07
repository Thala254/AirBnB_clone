#!/usr/bin/python3
"""test module for BaseModel class"""

import unittest
import pep8
import sys
import inspect
from datetime import datetime
from io import StringIO
from models import user, User, BaseModel


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that models/user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'tests/test_models/test_user.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(user.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the User class docstring"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestUser(unittest.TestCase):
    """Tests for User class"""

    def setUp(self):
        """ seting up BaseModel instance to be used for tests """
        self.test_user = User()
        self.test_user.first_name = "John"
        self.test_user.last_name = "Doe"
        self.test_user.email = "johndoe@mail.com"
        self.test_user.password = "pass123"

    def TearDown(self):
        """Remove an instance of the class"""
        del self.test_user

    def test_str(self):
        """
            checks that the correct string representation of the instance is
            printed
        """
        test_id = self.test_user.id
        output = sys.stdout
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.test_user)
        printed = capture_out.getvalue().split(" ")
        self.assertEqual(printed[0], "[User]")
        self.assertEqual(printed[1], f"({test_id})")
        sys.stdout = output

    def test_to_dict(self):
        """
            checks the dictionary representation of the class instance
        """
        dictionary = self.test_user.to_dict()
        self.assertEqual("<class 'str'>", str(type(dictionary["first_name"])))
        self.assertEqual("<class 'str'>", str(type(dictionary["last_name"])))
        self.assertEqual("<class 'str'>", str(type(dictionary["email"])))
        self.assertEqual("<class 'str'>", str(type(dictionary["password"])))

    def test_user_inheritence(self):
        '''
            Test that User class inherits from BaseModel.
        '''
        self.assertIsInstance(self.test_user, BaseModel)

    def test_user_attributes(self):
        '''
            Test that User class contains the attribute name.
        '''
        self.assertTrue("first_name" in self.test_user.__dir__())
        self.assertTrue("last_name" in self.test_user.__dir__())
        self.assertTrue("email" in self.test_user.__dir__())
        self.assertTrue("password" in self.test_user.__dir__())

    def test_user_attributes_type(self):
        '''
            Test for User class attributes.
        '''
        fname = getattr(self.test_user, "first_name")
        lname = getattr(self.test_user, "last_name")
        email = getattr(self.test_user, "email")
        passwd = getattr(self.test_user, "password")
        self.assertIsInstance(fname, str)
        self.assertIsInstance(lname, str)
        self.assertIsInstance(email, str)
        self.assertIsInstance(passwd, str)
