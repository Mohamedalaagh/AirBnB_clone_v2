#!/usr/bin/python3
"""
Module containing BaseModel class definitions.
"""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from os import getenv

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
    Base class for all data models, providing common functionality and attributes.

    Attributes (database mode):
        id (str): Unique identifier for the instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when the instance was last updated.

    Methods:
        __init__(*args, **kwargs): Initializes a new instance based on given arguments.
        __str__(): Returns a string representation of the instance.
        save(): Updates the 'updated_at' attribute with the current datetime and saves the instance.
        to_dict(save_to_disk=False): Returns a dictionary representation of the instance.
        delete(): Deletes the instance from storage.
    """

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments to initialize the instance attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
            if type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at, TIME_FORMAT)
            if type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at, TIME_FORMAT)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation including class name, instance id, and instance attributes.
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime and saves the instance to storage.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_to_disk=False):
        """
        Returns a dictionary representation of the BaseModel instance.

        Args:
            save_to_disk (bool, optional): Flag to include attributes not to be saved to disk.

        Returns:
            dict: Dictionary representation of the instance.
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        if '_password' in new_dict:
            new_dict['password'] = new_dict['_password']
            new_dict.pop('_password', None)
        if 'amenities' in new_dict:
            new_dict.pop('amenities', None)
        if 'reviews' in new_dict:
            new_dict.pop('reviews', None)
        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop('_sa_instance_state', None)
        if not save_to_disk:
            new_dict.pop('password', None)
        return new_dict

    def delete(self):
        """
        Deletes the instance from storage using the models module.
        """
        models.storage.delete(self)

