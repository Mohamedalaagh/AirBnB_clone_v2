#!/usr/bin/python3
"""
Contains the FileStorage class for serializing and deserializing instances
to and from a JSON file.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class FileStorage:
    """Handles serialization and deserialization
    of instances to a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary __objects. If cls is provided,
        returns dictionary
        of objects of type cls.

        Args:
            cls (type or str): The class type or class name to filter objects.

        Returns:
            dict: A dictionary of objects.
        """
        if cls is None:
            return self.__objects

        if isinstance(cls, str):
            return {
                k: v for k, v in self.__objects.items()
                if v.__class__.__name__ == cls
            }

        return {
            k: v for k, v in self.__objects.items()
            if v.__class__ == cls
        }

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (BaseModel): The object to be added to __objects.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        json_objects = {
            key: obj.to_dict(save_to_disk=True)
            for key, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects. If the file does not exist,
        it handles the exception and continues.
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key, value in jo.items():
                cls_name = value["__class__"]
                if cls_name in classes:
                    self.__objects[key] = classes[cls_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it’s inside and saves the changes.

        Args:
            obj (BaseModel): The object to be deleted.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """
        Call reload() to deserialize the JSON file to objects.
        """
        self.reload()

    def get(self, cls, id):
        """
        Retrieve an object by class name and id.

        Args:
            cls (str): The class name of the object.
            id (str): The id of the object.

        Returns:
            BaseModel: The object if found, otherwise None.
        """
        if (cls and isinstance(cls, str) and id and isinstance(id, str) and
                cls in classes):
            key = f"{cls}.{id}"
            return self.__objects.get(key, None)
        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage. If a class name is given, count
        the objects of that class type.

        Args:
            cls (type or str, optional): The class type to filter objects.

        Returns:
            int: The number of objects.
        """
        t = 0
        if isinstance(cls, str) and cls in classes:
            t = len(self.all(cls))
        elif cls is None:
            t = len(self.__objects)
        return t
