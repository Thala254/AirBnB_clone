#!/usr/bin/python3
'''
    Module that supplies Review class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
        Definition of the Review class
    '''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        initializes class objects
        """
        super().__init__(*args, **kwargs)
