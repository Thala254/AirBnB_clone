#!/usr/bin/python3
"""test module for BaseModel class"""

import unittest
import pep8
import inspect
from models import city, BaseModel
from models.city import City


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that models/city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'tests/test_models/test_city.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(city.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the City class docstring"""
        self.assertTrue(len(City.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestCity(unittest.TestCase):
    '''
        Testing City class
    '''

    def setUp(self):
        """ seting up BaseModel instance to be used for tests """
        self.test_city = City()
        self.test_city.name = "Karachi"

    def TearDown(self):
        """Remove an instance of the class"""
        del self.test_city

    def test_city_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''
        self.assertIsInstance(self.test_city, BaseModel)

    def test_city_attributes(self):
        self.assertTrue("state_id" in self.test_city.__dir__())
        self.assertTrue("name" in self.test_city.__dir__())

    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.test_city, "name")
        self.assertIsInstance(name, str)

    def test_type_state_id(self):
        '''
            Test the type of attribute state_id
        '''
        name = getattr(self.test_city, "state_id")
        self.assertIsInstance(name, str)
