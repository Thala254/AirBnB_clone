#!/usr/bin/python3
"""test module for BaseModel class"""

import unittest
import pep8
import sys
import inspect
from datetime import datetime
from io import StringIO
from models import base_model, BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """Test that tests/test_models/test_base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
                                        'tests/test_models/test_base_model.py'
                                      ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the BaseModel class docstring"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def setUp(self):
        """ seting up BaseModel instance to be used for tests """
        self.test_model = BaseModel()
        self.test_model.name = "My_test_model"

    def TearDown(self):
        """Remove an instance of the class"""
        del self.test_model

    def test_id_type(self):
        """checks if the type of attribute id is string"""
        self.assertEqual("<class 'str'>", str(type(self.test_model.id)))

    def test_id_unique(self):
        """
            check whether each instance of the BaseModel class has a unique id
        """
        new_instance = BaseModel()
        self.assertNotEqual(new_instance.id, self.test_model.id)

    def test_created_at_and_updated_at_attribute_type(self):
        """ checks the type for the created at attribute """
        self.assertTrue(isinstance(self.test_model.created_at, datetime))
        self.assertTrue(isinstance(self.test_model.updated_at, datetime))

    def test_new_attributes(self):
        """check if new attributes can be added"""
        self.assertEqual(self.test_model.name, "My_test_model")

    def test_update_attributes(self):
        """check if instance attributes can be updated"""
        old_update_time = self.test_model.updated_at
        self.test_model.save()
        new_update_time = self.test_model.updated_at
        self.assertNotEqual(old_update_time, new_update_time)

    def test_new_instance_created_at_equals_updated_at(self):
        """
           checks that the date of the attributes created_at and updated_at
           are similar for a new instance before updation
        """
        new_model = BaseModel()
        self.assertEqual(new_model.created_at.day, new_model.updated_at.day)

    def test_str(self):
        """
            checks that the correct string representation of the instance is
            printed
        """
        test_id = self.test_model.id
        output = sys.stdout
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.test_model)
        printed = capture_out.getvalue().split(" ")
        self.assertEqual(printed[0], "[BaseModel]")
        self.assertEqual(printed[1], f"({test_id})")
        sys.stdout = output

    def test_to_dict(self):
        """
            checks the dictionary representation of the class instance
        """
        dictionary = self.test_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(dictionary["created_at"])))
        self.assertEqual("<class 'str'>", str(type(dictionary["updated_at"])))
        self.assertEqual("<class 'str'>", str(type(dictionary["id"])))

    def test_to_dict_class(self):
        """
            checks to see if __class__ exists in the class dictionary
        """
        dictionary = self.test_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(dictionary["__class__"])))
        self.assertEqual("BaseModel", dictionary["__class__"])

    def test_save(self):
        """
            checks that updated_at attribute changes upon saving an instance
        """
        old_update_time = self.test_model.updated_at
        self.test_model.save()
        new_update_time = self.test_model.updated_at
        self.assertNotEqual(old_update_time, new_update_time)
