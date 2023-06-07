import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# list
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship('User', back_populates='tasks')
    category = relationship('Category', back_populates='tasks')

    def full_task(self):
        return f"Task for {self.category.name} by {self.user.full_name()}: {self.star_rating} stars."

def get_tasks():
    tasks = Task.query.all()
    return tasks

def get_completed_tasks(tasks):
    completed_tasks = [task for task in tasks if task.completed]
    return completed_tasks

categories = ['Work', 'Personal', 'Shopping']


# dictionary
class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tasks = relationship('Task', back_populates='user')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_category(self):
        if not self.tasks:
            return None
        return max(self.tasks, key=lambda r: r.category.star_rating).category
    
    def add_task(self, category, rating):
        review = Task(user=self, Category=category, star_rating=rating)
        session.add(review)
        session.commit()

    def delete_tasks(self, category):
        session.query(Task).filter(Task.customer == self, Task.category == category).delete()
        session.commit()

# tuple
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tasks = relationship('Task', back_populates='category')

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()
    
    def all_tasks(self):
        return [task.full_task() for task in self.tasks]
