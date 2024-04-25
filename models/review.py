#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os
from sqlalchemy import Column, String, ForeignKey


db = os.environ.get('HBNB_TYPE_STORAGE')

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    text = Column(String(1024))
    place_id = Column(String(60), ForeignKey('places.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    if (db == 'db'):
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
