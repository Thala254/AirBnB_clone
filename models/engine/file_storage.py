#!/usr/bin/python3
"""
module that supplies the class FileStorage
"""

import json
import models


class FileStorage:
    """
    class that serializes instances to a JSON file and deserializes JSON file
    to instances
    it stores objects in a file in a json format

    **Class Attributes**
        __file_path: private, the path/to/file
        __objects: private, a dictionary of all the objects
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Instantiate the class"""
        self.reload()


    def all(self):
        """ returns dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj  classname>.id """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file path"""
        json_obj = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as fd:
            json.dump(json_obj, fd)

    def reload(self):
        """deserializes the JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path, "r") as fd:
                FileStorage.__objects = json.load(fd)
            FileStorage.__objects = {
                                 key: models.classes[val["__class__"]](**val)
                                 for key, val in FileStorage.__objects.items()
                                 }
        except Exception:
            pass
