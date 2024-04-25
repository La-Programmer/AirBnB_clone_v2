#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table, MetaData
import os



place_amenity = Table("place_amenity",
                      Base.metadata,
                      Column(
                            "place_id",
                            String(60),
                            ForeignKey("places.id"),
                            primary_key=True),
                      Column(
                            "amenity_id",
                            String(60),
                            ForeignKey("amenities.id"),
                            primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    db = os.environ.get('HBNB_TYPE_STORAGE')

    # def __init__(self):
    #     """Intialize Place instance"""
    #     self.amenity_ids = []
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128))
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if (db == 'db'):
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship(
                               "Review",
                               back_populates="place")
        amenities = relationship(
                                 "Amenity",
                                 secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        amenity_ids = []
        @property
        def reviews(self):
            """Getter for reviews of a place"""
            list = storage.all(cls='Review')
            temp = []
            result = []
            # DEBUG PRINTING TAKE NOTICE OF THE LINES BELOW
            # POSSIBLE ERROR
            print(list)
            for key, value in list.items:
                temp.append(str(value))
            result = [x for x in temp if x.place_id == self.id]
            return result

        @property
        def amenities(self):
            """Getter for the amenities of a place"""
            list = storage.all(cls='Amenity')
            temp = []
            result = []
            # NOTICE NEXT LINE
            for key, value in list.items:
                temp.append(str(value))
            result = [x for x in temp if x.id in self.amenity_ids]

        @amenities.setter
        def amenities(self):
            if self.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(self.id)
