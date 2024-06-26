#!/usr/bin/python3
"""
City Module

This module defines the City class, which inherits from BaseModel.
The City class represents a city with a state ID and a name.

Classes:
    City: A class representing a city with state_id and name attributes.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city, inheriting from BaseModel.

    Attributes:
        state_id (str): The ID of the state where the city is located. Defaults to an empty string.
        name (str): The name of the city. Defaults to an empty string.
    """

    state_id = ""
    name = ""

