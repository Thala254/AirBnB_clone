#!/usr/bin/python3
'''
    Module that supplies Amenity class
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
        Definition of the Amenity class
    '''
    name = ""

    def __init__(self, *args, **kwargs):
        '''
        initializes class objects
        '''
        super().__init__(*args, **kwargs)
