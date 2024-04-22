#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float
import os


class Place(BaseModel, Base):
    """ A place to stay """
    db = os.environ.get('HBNB_TYPE_STORAGE')
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128))
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    if (db == 'db'):
        reviews = relationship("Review", back_populates="place")
    else:
        @property
        def reviews(self):
            """Getter for reviews of a place"""
            from models import storage
            list = storage.all(cls='Review')
            temp = []
            result = []
            # DEBUG PRINTING TAKE NOTICE OF THE LINES BELOW
            # POSSIBLE ERROR
            print(list)
            for key, value in list.items:
                temp.append(str(value))
            result = [instance for instance in temp if instance.place_id == self.id]
            return result
