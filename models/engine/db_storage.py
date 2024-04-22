#!/usr/bin/env python3
"""This module defines a class that handles python DB storage"""
from sqlalchemy import create_engine, MetaData
import configparser
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """This class manages the DB storage"""
    user = os.environ.get('HBNB_MYSQL_USER')
    password = os.environ.get('HBNB_MYSQL_PWD')
    database = os.environ.get('HBNB_MYSQL_DB')
    env = os.environ.get('HBNB_ENV')
    eng = f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    __engine = None
    __session = None
    metadata = MetaData()

    def __init__(self):
        """Class initialization"""
        self.__engine = create_engine(self.eng, pool_pre_ping=True)
        if (self.env == 'test'):
            self.metadata.reflect(self.__engine)
            self.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all instance based on class"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review}

        result = {}
        print(cls)
        if (cls is not None):
            instances = self.__session.query(classes[cls]).all()
            for instance in instances:
                key = f'{instance.__class__}.{instance.id}'
                result[key] = instance
        else:
            for class_name in classes:
                instances = self.__session.query(classes[class_name]).all()
                for instance in instances:
                    key = f'{instance.__class__}.{instance.id}'
                    result[key] = instance
        return result

    def new(self, obj):
        """Add object to current DB session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current DB session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current DB session"""
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
