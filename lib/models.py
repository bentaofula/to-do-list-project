from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# Define the User table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(30))
    password_hash = Column(String(30))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return str(self.id)

# @login.user_loader
# def load_user(id):
#     return Users.query.get(int(id))
    

engine = create_engine('sqlite:///todo_test.db')

Base.metadata.create_all(engine)
