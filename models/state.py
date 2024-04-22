#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


db = os.environ.get('HBNB_TYPE_STORAGE')
print(db)


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if (db == 'db'):
        cities = relationship("City", back_populates="state")
    elif (db == 'FileStorage'):
        def cities(self):
            from models import storage
            list = storage.all(cls='City')
            # DEBUG PRINTING TAKE NOTICE OF THE LINES BELOW
            # POSSIBLE ERROR
            print(list)
            result = [item for item in list if item.state_id == self.id]
            return result
