import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String(15), nullable=False)
    suscription_date = Column(Date)
    is_login = Column(Boolean, nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    climate = Column(String)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    population = Column(Integer)
    rotation_period = Column(Integer)   
    terrain = Column(String)

class FavouritePlanets(Base):
    __tablename__ = 'favourite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) # Defino clave foránea
    user = relationship(Users) # Defino la relacion que tiene la clave foránea
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(Date)
    eye_color = Column(String)
    gender = Column(String, nullable=False)
    mass = Column(Integer) 
    skin_color = Column(String)

class FavouriteCharacters(Base):
    __tablename__ = 'favourite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
