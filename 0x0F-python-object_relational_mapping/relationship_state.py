#!/usr/bin/python3
"""state modele"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """this the model class"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete")
