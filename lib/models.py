from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# from lib.models import Base

Base = declarative_base()

engine = create_engine('sqlite:///todo_test.db')
# Base.metadata.create_all(engine)

# # list
# class Task(Base):
#     __tablename__ = 'tasks'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     category_id = Column(Integer, ForeignKey('categories.id'))

#     user = relationship('User', back_populates='tasks')
#     category = relationship('Category', back_populates='tasks')

# def get_tasks():
#     tasks = Task.query.all()
#     return tasks

# def get_completed_tasks(tasks):
#     completed_tasks = [task for task in tasks if task.completed]
#     return completed_tasks

# categories = ['Work', 'Personal', 'Shopping']


# # dictionary
# class user(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     tasks = relationship('Task', back_populates='user')

# # tuple
# class Category(Base):
#     __tablename__ = 'categories'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     tasks = relationship('Task', back_populates='category')
