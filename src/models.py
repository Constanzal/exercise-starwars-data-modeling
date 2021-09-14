import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites = relationship('Favorites')
    planets = relationship('Planets')
    characters = relationship('Characters')
    vehicles = relationship('Vehicles')

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorite_id = Column(Integer, ForeignKey('user.id'))
    delete_elements = Column(Integer)
    planets = relationship('Planets')
    characters = relationship('Characters')
    vehicles = relationship('Vehicles')
    database_id = Column(Integer, ForeignKey('database.id'))
    database = relationship('database')
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('user.id'))
    planet_info = Column(String(250))
    fav_button = Column(Integer, ForeignKey('favorites.id'))
    database_id = Column(Integer, ForeignKey('database.id'))
    database = relationship('database')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('user.id'))
    character_info = Column(String(250))
    fav_button = Column(Integer, ForeignKey('favorites.id'))
    database_id = Column(Integer, ForeignKey('database.id'))
    database = relationship('database')

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('user.id'))
    vehicle_info = Column(String(250))
    fav_button = Column(Integer, ForeignKey('favorites.id'))
    database_id = Column(Integer, ForeignKey('database.id'))
    database = relationship('database')

class Database(Base):
    __tablename__ = 'database'
    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')