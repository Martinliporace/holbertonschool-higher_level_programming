#!/usr/bin/python3
"""Task: 0. Get all states"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if (__name__ == "__main__"):

    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    firstState = session.query(State).order_by(State.id).first()
    if (firstState is None):
        print('Nothing')
    else:
        print("{}: {}".format(firstState.id, firstState.name))
    session.close()
