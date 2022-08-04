#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''

import unittest
import pep8
import inspect
from models import amenity, BaseModel
from models.amenity import Amenity


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'tests/test_models/test_amenity.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(amenity.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Amenity class docstring"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestAmenity(unittest.TestCase):
    '''
        Testing Amenity class
    '''

    def setUp(self):
        """ seting up BaseModel instance to be used for tests """
        self.test_amenity = Amenity()
        self.test_amenity.name = "My_test_model"

    def TearDown(self):
        """Remove an instance of the class"""
        del self.test_amenity

    def test_amenity_inheritence(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        self.assertIsInstance(self.test_amenity, BaseModel)

    def test_amenity_attributes(self):
        '''
            Test that Amenity class has name attribute.
        '''
        self.assertTrue("name" in self.test_amenity.__dir__())

    def test_amenity_attribute_type(self):
        '''
            Test that amenity class has name attribute's type.
        '''
        name = getattr(self.test_amenity, "name")
        self.assertIsInstance(name, str)
