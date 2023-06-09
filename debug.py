import ipdb

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
        if self.category.star_rating:
            return f"Task for {self.category.name} by {self.user.full_name()}: {self.category.star_rating} stars."
        else:
            return f"Task for {self.category.name} by {self.user.full_name()}"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    name = Column(String)
    tasks = relationship('Task', back_populates='user')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    star_rating = Column(Integer)
    tasks = relationship('Task', back_populates='category')

    def all_tasks(self):
        return [task.full_task() for task in self.tasks]


# create a user object
user1 = User(first_name='Mary', last_name='Jean', name='Mary Jean')

#  Create a category object
category1 = Category(name='Category 1', star_rating=5)
category2 = Category(name='Category 2', star_rating=50)

category1.tasks.append(Task(title='Task 1', user=User(first_name='Mary', last_name='Jean')))
category2.tasks.append(Task(title='Task 2', user=User(first_name='Jane', last_name='Sam')))

    # Retrieve all tasks for the category
tasks1 = category1.all_tasks()


ipdb.set_trace()
