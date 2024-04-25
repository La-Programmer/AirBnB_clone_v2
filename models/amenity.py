#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


db = os.environ.get('HBNB_TYPE_STORAGE')

class Amenity(BaseModel, Base):
    """This class defines an amenity"""
    from models.place import place_amenity
    __tablename__ = "amenities"
    name = Column(String(128))
    if (db == 'db'):
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities")
