#!/usr/bin/python3
"""

All City Objects from [DB: hbtn_0e_14_usa]

"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_city = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in state_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
