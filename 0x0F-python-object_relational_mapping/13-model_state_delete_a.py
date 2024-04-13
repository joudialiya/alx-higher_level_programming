#!/usr/bin/python3
"""Select all ORM"""

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(
                               sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State).filter(State.name.like('%a%'))
    for state in query.all():
        session.delete(state)
    session.commit()
    session.close()
