#!/usr/bin/python3
"""
State Module

This module defines the State class, which inherits from BaseModel.
The State class represents a state with a name attribute.

Classes:
    State: A class representing a state with a name attribute.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state, inheriting from BaseModel.

    Attributes:
        name (str): The name of the state. Defaults to an empty string.
    """

    name = ""

