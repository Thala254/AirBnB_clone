#!/usr/bin/env python3
""" base_model module """

import uuid
from datetime import datetime

class BaseModel:
    """ class to be used as the base class for other nodels in th project"""
    def __init__(self, *args, **kwargs):
        """initializes all instances of the BaseModel class"""
        if kwargs:
            for key in kwargs.keys():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class"""
        return f"[{type(self).__name__}]({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.__dict__["updated_at"] = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all key/values of __dict__ of the instance"""
        instance  = self.__dict__
        instance["created_at"] = self.__dict__["created_at"].isoformat(timespec='microseconds')
        instance["updated_at"] = self.__dict__["updated_at"].isoformat(timespec='microseconds')
        instance["__class__"] = type(self).__name__
        return instance
