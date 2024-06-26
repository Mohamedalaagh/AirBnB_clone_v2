#!/usr/bin/python3
"""
Module for FileStorage class handling serialization to/from JSON files.
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
    """
    Serializes instances to a JSON file and deserializes back to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or filtered by class name.

        Args:
            cls (str or class, optional): Class name or class to filter objects.

        Returns:
            dict: Dictionary of objects keyed by their '__class__.__name__.id'.
        """
        if not cls:
            return self.__objects
        elif isinstance(cls, str):
            return {k: v for k, v in self.__objects.items()
                    if v.__class__.__name__ == cls}
        else:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): Object to be added to storage.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file at __file_path.
        """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict(save_to_disk=True)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializes the JSON file at __file_path to __objects.
        """
        try:
            with open(self.__file_path, 'r') as f:
                json_data = json.load(f)
            for key in json_data:
                class_name = json_data[key]["__class__"]
                if class_name in classes:
                    self.__objects[key] = classes[class_name](**json_data[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from __objects if it exists and saves the changes.

        Args:
            obj (BaseModel, optional): Object to be deleted from storage.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """
        Reloads the JSON file to refresh __objects.
        """
        self.reload()

    def get(self, cls, id):
        """
        Retrieves an object based on class name and ID.

        Args:
            cls (str): Class name of the object to retrieve.
            id (str): ID of the object to retrieve.

        Returns:
            object: Retrieved object or None if not found.
        """
        if isinstance(cls, str) and isinstance(id, str) and cls in classes:
            key = f"{cls}.{id}"
            return self.__objects.get(key, None)
        else:
            return None

    def count(self, cls=None):
        """
        Counts the number of objects in storage, optionally filtered by class.

        Args:
            cls (str or class, optional): Class name or class to filter objects.

        Returns:
            int: Total count of objects in storage.
        """
        if isinstance(cls, str) and cls in classes:
            return len(self.all(cls))
        elif cls is None:
            return len(self.__objects)
        else:
            return 0

