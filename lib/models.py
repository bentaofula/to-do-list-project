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
    password = Column(String(30))

# Define the Product table
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Integer)

    def if_name_is_empty(self):
        if self.product_name == "":
            return True
        else:
            return False

    def if_name_is_valid(self):
        if self.product_name != self.product_name.capitalize():
            return False 
        else:
            return True


    def __repr__(self):
        return 'Product name - {}'.format(self.product_name)



engine = create_engine('sqlite:///todo_test.db')

Base.metadata.create_all(engine)
