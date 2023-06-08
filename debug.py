import random

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///new_todo_test.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
import ipdb


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship('User', back_populates='tasks')
    category = relationship('Category', back_populates='tasks')

def __repr__(self):
        return f"Task: {self.id} Rate: {self.rating}" 

def full_task(self):
    if self.category.star_rating:
        return f"Task for {self.category.name} by {self.user.full_name()}: {self.category.star_rating} stars."
    else:
        return f"Task for {self.category.name} by {self.user.full_name()}"

def get_tasks():
    tasks = Task.query.all()
    return tasks

def get_completed_tasks(tasks):
    completed_tasks = [task for task in tasks if task.completed]
    return completed_tasks

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)  # Add first_name attribute
    last_name = Column(String)
    name = Column(String)
    tasks = relationship('Task', back_populates='user')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"User: {self.id} Name: {self.first_name} {self.last_name}"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    star_rating = Column(Integer)  # Add star_rating attribut
    tasks = relationship('Task', back_populates='category')

def __repr__(self):
        return f"Category: {self.id} Name: {self.name}"


    

def debug():
    # Create instances of Task, User, and Category
    task = Task(title='Debug Task')
    user = User(first_name='Mary', last_name='Jean')
    category = Category(name='Debug Category', star_rating=5)

    # Add instances to the session
    session.add(task)
    session.add(user)
    session.add(category)
    session.commit()

if __name__ == '__main__':
    debug()


ipdb.set_trace()
