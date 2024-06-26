#!/usr/bin/python3
"""Database storage engine using SQLAlchemy with a MySQL database connection."""

import os
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Mapping of class names to class objects
class_map = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """Database Storage Engine"""
    
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database engine."""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}')
        
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, class_name=None):
        """
        Returns a dictionary of all objects present.
        
        Args:
            class_name (str): The class name of the objects to retrieve.
        
        Returns:
            dict: A dictionary of all objects.
        """
        if not self.__session:
            self.reload()
        objects = {}
        if isinstance(class_name, str):
            class_name = class_map.get(class_name, None)
        if class_name:
            for obj in self.__session.query(class_name):
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            for cls in class_map.values():
                for obj in self.__session.query(cls):
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def reload(self):
        """Reloads objects from the database."""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """
        Adds a new object to the current session.
        
        Args:
            obj: The object to add.
        """
        self.__session.add(obj)

    def save(self):
        """Commits the current session to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current session.
        
        Args:
            obj: The object to delete.
        """
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Closes the current session."""
        self.__session.remove()

    def get(self, class_name, object_id):
        """
        Retrieves an object by class name and ID.
        
        Args:
            class_name (str): The class name of the object.
            object_id (str): The ID of the object.
        
        Returns:
            The object if found, None otherwise.
        """
        if class_name and isinstance(class_name, str) and object_id and isinstance(object_id, str):
            class_obj = class_map.get(class_name)
            if class_obj:
                return self.__session.query(class_obj).filter(class_obj.id == object_id).first()
        return None

    def count(self, class_name=None):
        """
        Counts the number of objects in storage.
        
        Args:
            class_name (str): The class name of the objects to count.
        
        Returns:
            int: The number of objects in storage.
        """
        total_count = 0
        if isinstance(class_name, str):
            class_obj = class_map.get(class_name)
            if class_obj:
                total_count = self.__session.query(class_obj).count()
        else:
            for cls in class_map.values():
                total_count += self.__session.query(cls).count()
        return total_count

