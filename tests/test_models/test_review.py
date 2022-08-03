#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
import pep8
import sys
import inspect
from models import review, BaseModel
from models.review import Review


class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and style of Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that models/review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'tests/test_models/test_review.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(review.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Review class docstring"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''

    def setUp(self):
        """ seting up BaseModel instance to be used for tests """
        self.test_review = Review()

    def TearDown(self):
        """Remove an instance of the class"""
        del self.test_review

    def test_review_inheritance(self):
        '''
            tests that the Review class Inherits from BaseModel
        '''
        self.assertIsInstance(self.test_review, BaseModel)

    def test_review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        self.assertTrue("place_id" in self.test_review.__dir__())
        self.assertTrue("user_id" in self.test_review.__dir__())
        self.assertTrue("text" in self.test_review.__dir__())

    def test_review_attributes_types(self):
        '''
            Test of types of the class instance attributes place_id,
            user_id and text.
        '''
        place_id = getattr(self.test_review, "place_id")
        user_id = getattr(self.test_review, "user_id")
        text = getattr(self.test_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
