#!/usr/bin/env python3
"""test module for BaseModel class"""

import unittest
import sys
import datetime
from io import StringIO
from models.base_model import BaseModel


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
        """check whether each instance of the BaseModel class has a unique id"""
        new_instance = BaseModel()
        self.assertNotEqual(new_instance.id, self.test_model.id)

    def test_created_at_and_updated_at_attribute_type(self):
        """ checks the type for the created at attribute """
        self.assertTrue(isinstance(self.test_model.created_at, datetime.datetime))
        self.assertTrue(isinstance(self.test_model.updated_at, datetime.datetime))

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

    def test_instantiation(self):
        """
            checks if the class instance can be instantiated with or without
            key_word args (**kwargs)
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        test_model_dict = self.test_model.to_dict()
        new_model = BaseModel(**test_model_dict)
        self.assertEqual(new_model.id, self.test_model.id)

    def test_compare_model_dict(self):
        """
            checks that the dictionaries of a model created by an instance's
            dictionary will be same
        """
        test_model_dict = self.test_model.to_dict()
        model_a = BaseModel(**test_model_dict)
        model_a_dict = model_a.to_dict()
        self.assertEqual(test_model_dict, model_a_dict)
