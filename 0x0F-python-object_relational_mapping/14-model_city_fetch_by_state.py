#!/usr/bin/python3
"""Select all ORM"""

import sys
from model_state import Base, State
from model_city import City

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
    for city in session.query(City).order_by(City.id).all():
        state = session.query(State).where(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state[2], city[0], city[1]))
    session.close()
