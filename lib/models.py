import os
import sys
import click
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

sys.path.append(os.getcwd)

Base = declarative_base()

engine = create_engine('sqlite:///new_todo_test.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer(), ForeignKey('categories.id'))


    def __repr__(self):
        return f"Task: {self.id} Rate: {self.rating}"
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
    
    # def favorite_category(self):
    #     if not self.tasks:
    #         return None
    #     return max(self.tasks, key=lambda r: r.category.star_rating).category
    
    # def add_task(self, category, rating):
    #     task = Task(title='New Tas', user=self, Category=category)
    #     session.add(Task)
    #     session.commit()

    # def delete_tasks(self, category):
    #     session.query(Task).filter(Task.user == self, Task.category == category).delete()
    #     session.commit()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    star_rating = Column(Integer)  # Add star_rating attribut
    tasks = relationship('Task', back_populates='category')

    def __repr__(self):
        return f"Category: {self.id} Name: {self.name}"


