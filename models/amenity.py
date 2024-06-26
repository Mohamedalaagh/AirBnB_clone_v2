#!/usr/bin/python3
"""
Amenity Module

This module defines the Amenity class, which inherits from BaseModel.
The Amenity class represents an amenity with a name attribute.

Classes:
    Amenity: A class representing an amenity with a name attribute.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Represents an amenity, inheriting from BaseModel.

    Attributes:
        name (str): The name of the amenity. Defaults to an empty string.
    """

    name = ""

