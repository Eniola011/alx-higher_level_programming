#!/usr/bin/python3
"""

State Object with the name passed as argument 
from [DB: hbtn_0e_6_usa]

"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == argv[4]).first()
    print("Not found" if not state else state.id)
    session.close()
