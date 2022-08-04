#!/usr/bin/python3
'''
    Contain tests for the state module.
'''
import unittest
import pep8
import inspect
from models import state, BaseModel
from models.state import State


class TestStateDocs(unittest.TestCase):
    """Tests to check the documentation and style of State class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that models/state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'tests/test_models/test_state.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(state.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the State class docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestState(unittest.TestCase):
    '''
        Test the State class.
    '''

    def setUp(self):
        """ seting up BaseModel instance to be used for tests """
        self.test_state = State()

    def TearDown(self):
        """Remove an instance of the class"""
        del self.test_state

    def test_state_inheritence(self):
        '''
            Test that State class inherits from BaseModel.
        '''
        self.assertIsInstance(self.test_state, BaseModel)

    def test_state_attributes(self):
        '''
            Test that State class contains the attribute name.
        '''
        self.assertTrue("name" in self.test_state.__dir__())

    def test_state_attributes_type(self):
        '''
            Test that State class attribute name is class type str.
        '''
        name = getattr(self.test_state, "name")
        self.assertIsInstance(name, str)
