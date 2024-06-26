#!/usr/bin/python3
"""
User Module

This module defines the User class, which inherits from BaseModel.
The User class represents a user in the system with various attributes.

Classes:
    User: A class representing a user with email, password, first name, and last name.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User in the system, inheriting from BaseModel.

    Attributes:
        email (str): The email address of the user. Defaults to an empty string.
        password (str): The password for the user account. Defaults to an empty string.
        first_name (str): The first name of the user. Defaults to an empty string.
        last_name (str): The last name of the user. Defaults to an empty string.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

