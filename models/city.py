#!/usr/bin/python3
"""Defines the City class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Represents a city, inherits from BaseModel and Base.

    Attributes:
        __tablename__ (str): Name of the database table for SQLAlchemy.
        name (Column): City name (max length 128, non-nullable).
        state_id (Column): State ID associated with the city (max length 60, non-nullable).
        places (relationship): Relationship to Place instances, with cascading delete.

    Methods:
        __init__(*args, **kwargs): Initializes a new City instance.
    """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance."""
        super().__init__(*args, **kwargs)

