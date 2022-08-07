#!/usr/bin/python3
"""module that tests file_storage module"""

import unittest
import pep8
import json
import sys
import os
import inspect
from io import StringIO
from models import file_storage, BaseModel

FileStorage = file_storage.FileStorage


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """
            Test that tests/test_models/test_engine/test_file_storage.py
            conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
                 'tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the BaseModel class docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""
    def setUp(self):
        """
            seting up FileStorage and BaseModel instances to be used for tests
        """
        self.storage = FileStorage()
        self.test_model = BaseModel()

    def tearDown(self):
        """ clean up """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        """ test to check the return type of the all method """
        store = self.storage.all()
        self.assertIsInstance(store, dict)

    def test_new_method(self):
        """
            Tests that a new instance is stored in the class
            attribute __object with correct key value pairs
        """
        self.storage.new(self.test_model)
        key = f"{self.test_model.__class__.__name__}.{self.test_model.id}"
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_object_type(self):
        """
            Tests that the type for the object stored in __objects is same
            to that of obj.__class__.__name__
        """
        self.storage.new(self.test_model)
        key = f"{self.test_model.__class__.__name__}.{self.test_model.id}"
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.test_model, type(val))

    def test_reload_without_file(self):
        """
            Tests that nothing happens when file.json does not exists
        """
        try:
            self.storage.reload()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)
