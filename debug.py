import random
import os
import sys

sys.path.append(os.getcwd())

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///new_todo_test.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
import ipdb



if __name__ == '__main__':
    debug()


ipdb.set_trace()
