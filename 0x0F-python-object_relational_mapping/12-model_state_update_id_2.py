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
    state = session.select(State).where(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()
