#!/usr/bin/python3
"""
Place Module

This module defines the Place class, which inherits from BaseModel.
The Place class represents a place with various attributes such as city ID, user ID,
name, description, number of rooms and bathrooms, maximum guests, price per night,
latitude, longitude, and a list of amenity IDs.

Classes:
    Place: A class representing a place with various attributes.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place, inheriting from BaseModel.

    Attributes:
        city_id (str): The ID of the city where the place is located. Defaults to an empty string.
        user_id (str): The ID of the user who owns the place. Defaults to an empty string.
        name (str): The name of the place. Defaults to an empty string.
        description (str): The description of the place. Defaults to an empty string.
        number_rooms (int): The number of rooms in the place. Defaults to 0.
        number_bathrooms (int): The number of bathrooms in the place. Defaults to 0.
        max_guest (int): The maximum number of guests the place can accommodate. Defaults to 0.
        price_by_night (int): The price per night for the place. Defaults to 0.
        latitude (float): The latitude of the place. Defaults to 0.0.
        longitude (float): The longitude of the place. Defaults to 0.0.
        amenity_ids (list): A list of amenity IDs associated with the place. Defaults to an empty list.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

