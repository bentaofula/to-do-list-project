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


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    star_rating = Column(Integer)
    tasks = relationship('Task', back_populates='category')

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_tasks(self):
        return [task.full_task() for task in self.tasks]


def debug():
    Base.metadata.create_all(engine)


# Create users
user1 = User("John")
user2 = User("Alice")

# Create categories
category1 = Category("Work")
category2 = Category("Personal")

# Add tasks to categories
category1.add_task("Task 1", user1)
category1.add_task("Task 2", user2)
category2.add_task("Task 3", user1)

# Shuffle a list
tasks = category1.tasks + category2.tasks
shuffle_list(tasks)
print("Shuffled tasks:", [task.title for task in tasks])

# Find the maximum element in a tuple
ratings = (5, 3, 8, 2, 9)
max_rating = find_max_tuple(ratings)
print("Maximum rating:", max_rating)

# Add items to a dictionary
my_dict = {}
my_dict["name"] = "John"
my_dict["age"] = 30
my_dict["city"] = "New York"
print("Dictionary:", my_dict)

#     user1 = User(first_name='Mary', last_name='Jean')
#     # Access the full_name method of the user1 object
#     print(user1.full_name())

#     user2 = User(first_name='Moe', last_name='Rue')
#     session.add_all([user1, user2])
#     session.commit()

#     category1 = Category(name='Category A')
#     category2 = Category(name='Category B')
#     # session.add_all([category1, category2])
#     # session.commit()

#     # Create some tasks and assign categories
#     task1 = Task(star_rating=2.0)
#     task1.user = user1
#     task1.category = category1

#     task2 = Task(star_rating=3.0)
#     task2.user = user2
#     task2.category = category2
#     # task1.category = category1
#     # task2.category = category2
#     # session.add_all([task1, task2])
#     # session.commit()

#    # Print all tasks for the user
#     tasks = session.query(Task).filter(Task.user == user1).all()
#     print("All Tasks:")
#     for task in tasks:
#          print(task.full_task())

#     # Print the user's favorite category
#     favorite_category = user1.favorite_category()
#     if favorite_category:
#         print(f"Favorite Category: {favorite_category.name}")
#     else:
#         print("No tasks found.")

#     # Delete all tasks for the user
#     session.query(Task).filter(Task.user == user1).delete()
#     session.commit()

#     # Print all tasks for the user after deletion
#     tasks = session.query(Task).filter(Task.user == user1).all()
#     print("All Tasks after deletion:")
#     for task in tasks:
#         print(task1.full_task())
#         print(task2.full_task)

#     # Delete the user
#     session.delete(user1)
#     session.commit()

if __name__ == '__main__':
    debug()


ipdb.set_trace()
