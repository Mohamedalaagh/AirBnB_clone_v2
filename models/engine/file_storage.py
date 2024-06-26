#!/usr/bin/python3
"""
FileStorage Module

This module defines the FileStorage class, which provides an abstracted storage engine
for saving and loading instances of various models to and from a JSON file.

Classes:
    FileStorage: A class representing a file-based storage engine.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represents a file-based storage engine.

    Attributes:
        __file_path (str): The path to the JSON file used for storage. Defaults to "file.json".
        __objects (dict): A dictionary storing all instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all instantiated objects.

        Returns:
            dict: A dictionary of all instantiated objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to add to the storage.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serialize the objects in the storage dictionary to the JSON file.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        Deserialize the JSON file to the storage dictionary, if the file exists.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return

