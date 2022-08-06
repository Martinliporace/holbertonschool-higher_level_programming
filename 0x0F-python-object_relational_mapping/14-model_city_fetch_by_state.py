#!/usr/bin/python3
"""Task: 0. Get all states"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if (__name__ == "__main__"):

    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City).filter(
             City.state_id == State.id)
    for x, y in cities:
        print("{}: ({}) {}".format(x.name, y.id, y.name))
    session.close()
