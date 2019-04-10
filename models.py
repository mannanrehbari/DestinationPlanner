import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), nullable=False)
    picture = Column(String(250))


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """return country object in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class DestSpot(Base):
    __tablename__ = 'dest_spot'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    destdescription = Column(String(600))
    destlat = Column(String(100))
    destlng = Column(String(100))
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship(Country)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """ return destination object in serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'lat': self.destlat,
            'lng': self.destlng,
            'description': self.destdescription,
            'country_id': self.country_id,
            'user_id': self.user_id
        }


engine = create_engine('sqlite:///countrydestinations.db')

Base.metadata.create_all(engine)
