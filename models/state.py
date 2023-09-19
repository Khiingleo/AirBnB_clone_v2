#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """
            getter attribute that returns the list of City
            instances with state_id equal to the current state.id
            """
            from models import storage
            cities_list = []
            for city in storage.all("City").values():
                if city.state_id == State.id:
                    cities_list.append(city)
            return cities_list
