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
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship('User', back_populates='tasks')
    category = relationship('Category', back_populates='tasks')
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
    
    def favorite_category(self):
        if not self.tasks:
            return None
        return max(self.tasks, key=lambda r: r.category.star_rating).category
    
    def add_task(self, category, rating):
        task = Task(title='New Tas', user=self, Category=category)
        session.add(Task)
        session.commit()

    def delete_tasks(self, category):
        session.query(Task).filter(Task.user == self, Task.category == category).delete()
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



@click.group()
def cli():
    pass

@cli.command()
def create_task():
    # task_title = click.prompt("Enter task title")
    # category_name = click.prompt("Enter category name")
    # rating = click.prompt("Enter star rating", type=int)
    
    # # Create category
    # category = Category(name=category_name, star_rating=rating)
    # session.add(category)
    # session.commit()

    #  # Create user
    # user = User(first_name='John', last_name='Doe')
    # session.add(user)
    # session.commit()

    # # Create task
    # task = Task(title=task_title, user=user, category=category)
    # session.add(task)
    # session.commit()
    
    # click.echo("Task created successfully!")


 if __name__ == "__main__":
  create_task()