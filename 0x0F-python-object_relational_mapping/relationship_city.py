#!/usr/bin/python3
"""Task: 0. Get all states"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """el coso que va aca"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
