#!/usr/bin/python3
'''
    Module that supplies State class
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''
        Definition of the State class
    '''
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initializes class objects
        """
        super().__init__(*args, **kwargs)
