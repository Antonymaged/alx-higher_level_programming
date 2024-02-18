#!/usr/bin/python3
import sys
from SQLAlchemy import create_engine
from model_state import Base, State
"""making the state class"""

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
