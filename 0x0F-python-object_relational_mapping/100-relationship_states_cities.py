#!/usr/bin/python3
"""Task: 0. Get all states"""

from sys import argv
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if (__name__ == "__main__"):

    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = "California"
    newCity = "San Francisco"
    new = (City(name=newCity, state=State(name=newState)))
    session.add(new)
    session.commit()
    session.close()
