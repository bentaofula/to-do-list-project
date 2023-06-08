import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///new_todo.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship('User', back_populates='tasks')
    category = relationship('Category', back_populates='tasks')

    def full_task(self):
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

categories = ['Work', 'Personal', 'Shopping']



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)  # Add first_name attribute
    last_name = Column(String)
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
        session.add(Task)
        session.commit()

    def delete_tasks(self, category):
        session.query(Task).filter(Task.customer == self, Task.category == category).delete()
        session.commit()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    star_rating = Column(Integer)  # Add star_rating attribut
    tasks = relationship('Task', back_populates='category')

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()
    
    def all_tasks(self):
        return [task.full_task() for task in self.tasks]
