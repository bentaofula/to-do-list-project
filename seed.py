#!usr/bin/env python3
import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Task, User, Category

if __name__ == "__main__":
    engine = create_engine("sqlite:///todo.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Task).delete()
    session.query(User).delete()
    session.query(Category).delete()

    fake = Faker()

    users = []
    for _ in range(10):
        user = User(
            name=fake.name()
        )
        session.add(user)
        users.append(user)

    categories = []
    for _ in range(5):
        category = Category(
            name=fake.word()
        )
        session.add(category)
        categories.append(category)

    for _ in range(30):
        task = Task(
            title=fake.sentence(),
            description=fake.paragraph(),
            user=random.choice(users),
            category=random.choice(categories)
        )
        session.add(task)

    session.commit()
    session.close()
