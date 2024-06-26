#!/usr/bin/python3
"""
Review Module

This module defines the Review class, which inherits from BaseModel.
The Review class represents a review with associated place and user IDs,
and the text content of the review.

Classes:
    Review: A class representing a review with place_id, user_id, and text attributes.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review, inheriting from BaseModel.

    Attributes:
        place_id (str): The ID of the place being reviewed. Defaults to an empty string.
        user_id (str): The ID of the user who wrote the review. Defaults to an empty string.
        text (str): The content of the review. Defaults to an empty string.
    """

    place_id = ""
    user_id = ""
    text = ""

