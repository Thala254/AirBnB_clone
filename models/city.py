#!/usr/bin/python3
'''
    Module that supplies City class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        Definition of the City class
    '''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initializes class objects
        """
        super().__init__(*args, **kwargs)

