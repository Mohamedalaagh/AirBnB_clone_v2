#!/usr/bin/python3
"""
BaseModel Module

This module defines the BaseModel class, which serves as the base class for
other models in the HBnB project. It includes common attributes and methods
that other models will inherit.

Classes:
    BaseModel: A base class with common attributes and methods for other models.
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Represents the BaseModel of the HBnB project.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime and save the instance."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing the class name of the object.

        Returns:
            dict: A dictionary representation of the instance.
        """
        redict = self.__dict__.copy()
        redict["created_at"] = self.created_at.isoformat()
        redict["updated_at"] = self.updated_at.isoformat()
        redict["__class__"] = self.__class__.__name__
        return redict

    def __str__(self):
        """
        Return the string representation of the BaseModel instance.

        Returns:
            str: A string representation of the instance.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

