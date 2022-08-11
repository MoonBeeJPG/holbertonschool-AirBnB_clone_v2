#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id """
        cities = []
        for i, j in self.cities.items():
            if self.id == j.state_id:
                cities.append(j)
        return cities
