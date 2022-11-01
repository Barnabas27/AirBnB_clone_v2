#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
import os


place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', ForeignKey('places.id')),
                          Column('amenity_id', ForeignKey('amenities.id')),
                          mysql_charset="latin1"
                          )

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)

    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)

    name = Column(String(128),
                  nullable=False)

    description = Column(String(1024),
                         nullable=True)

    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)

    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)

    max_guest = Column(Integer,
                       nullable=False,
                       default=0)

    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)

    latitude = Column(Float,
                      nullable=True)

    longitude = Column(Float,
                       nullable=True)

    reviews = relationship("Review",
                           backref="place",
                           cascade="all, delete-orphan")
    am_id = []
    __table_args__ = (
        {'mysql_default_charset': 'latin1'}
        )

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def amenities(self):
            """Returns the instances"""
            _inst = []
            for am in am_id:
                if am.id == self.id:
                    _inst.append(am)
            return _inst

        @amenities.setter
        def amenities(self, am):
            """Adds an Amenity"""
            if type(am).__name__ == 'Amenity':
                self.am_id.append(am)
    elif os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def reviews(self):
            _rev = []
            for review in self.reviews:
                if review.place_id == self.id:
                    _rev.append(review)
            return(_rev)
        amenities = relationship("Amenity",
                                 secondary=place_amenity)