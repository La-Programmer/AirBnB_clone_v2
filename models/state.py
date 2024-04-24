#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


db = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if (db == 'db'):
        cities = relationship("City", back_populates="state")
    elif (db == 'FileStorage'):
        @property
        def cities(self):
            """Getter for cities in a State"""
            from models import storage
            list = storage.all(cls='City')
            temp = []
            result = []
            # DEBUG PRINTING TAKE NOTICE OF THE LINES BELOW
            # POSSIBLE ERROR
            print(list)
            for key, value in list.items:
                temp.append(str(value))
            result = [x for x in temp if x.state2_id == self.id]
            return result
