#!/usr/bin/python3
"""Defines the State class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents a state, inherits from BaseModel and Base.

    Attributes:
        __table_name (str): Name of the database table for SQLAlchemy.
        state_name (Column): State name (max length 128, non-nullable).
        related_cities (relationship): Relationship to City instances, with cascading delete.

    Methods:
        __init__(*args, **kwargs): Initializes a new State instance.
    """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __table_name = 'states'
        state_name = Column(String(128), nullable=False)
        related_cities = relationship("City", cascade="all, delete", backref="state")
    else:
        state_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new State instance."""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def related_cities(self):
            """Getter attribute that returns City instances associated with this State."""
            all_cities = models.storage.all("City").values()
            state_cities = [city for city in all_cities if city.state_id == self.id]
            return state_cities

