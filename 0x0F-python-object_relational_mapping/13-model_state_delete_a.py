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
    toDel = session.query(State).filter(State.name.like('%a%')).all()
    for x in toDel:
        session.delete(x)
    session.commit()
    session.close()
