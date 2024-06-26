#!/usr/bin/python3
"""
This module contains the FileStorage class responsible for serializing instances 
to a JSON file and deserializing back to instances.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Dictionary mapping class names to their corresponding classes
CLASSES = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class FileStorage:
    """
    Handles serialization and deserialization of instances to/from a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file storing serialized data.
        __objects (dict): Dictionary storing all serialized instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Retrieves all instances stored in __objects.

        Args:
            cls (str or class, optional): If provided, filters instances by class name or type.

        Returns:
            dict: Dictionary of instances keyed by <class name>.id or all instances if cls is None.
        """
        if cls is None:
            return self.__objects
        elif isinstance(cls, str):
            return {key: value for key, value in self.__objects.items()
                    if value.__class__.__name__ == cls}
        else:
            return {key: value for key, value in self.__objects.items()
                    if isinstance(value, cls)}

    def new(self, obj):
        """
        Adds a new object instance to __objects.

        Args:
            obj (BaseModel): Instance of a BaseModel subclass to be added.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file specified by __file_path.
        """
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict(save_to_disk=True)
        with open(self.__file_path, 'w') as file:
            json.dump(json_objects, file)

    def reload(self):
        """
        Deserializes the JSON file specified by __file_path to __objects.
        """
        try:
            with open(self.__file_path, 'r') as file:
                json_data = json.load(file)
            for key, data in json_data.items():
                class_name = data["__class__"]
                if class_name in CLASSES:
                    self.__objects[key] = CLASSES[class_name](**data)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes the specified object instance from __objects.

        Args:
            obj (BaseModel, optional): Instance of a BaseModel subclass to be deleted.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """
        Alias for reload method to deserialize JSON file back into objects.
        """
        self.reload()

    def get(self, cls_name, obj_id):
        """
        Retrieves an object instance from __objects based on class name and object ID.

        Args:
            cls_name (str): Name of the class of the object instance.
            obj_id (str): ID of the object instance.

        Returns:
            obj: Object instance if found, None if not found.
        """
        if isinstance(cls_name, str) and isinstance(obj_id, str) and cls_name in CLASSES:
            key = cls_name + '.' + obj_id
            obj = self.__objects.get(key, None)
            return obj
        else:
            return None

    def count(self, cls=None):
        """
        Counts the number of object instances in __objects.

        Args:
            cls (str or class, optional): If provided, counts instances by class name or type.

        Returns:
            int: Number of object instances.
        """
        total = 0
        if isinstance(cls, str) and cls in CLASSES:
            total = len(self.all(cls))
        elif cls is None:
            total = len(self.__objects)
        return total

