#!/usr/bin/python3
"""City modele"""

from relationship_state import Base, State

from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """this the model class"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
