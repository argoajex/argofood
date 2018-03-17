from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, index=True)
    email = Column(String(250), nullable=False)


class Cook(Base):
    __tablename__ = 'cook'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, index=True)
    style = Column(String(250), nullable=False)
    description = Column(String(400), nullable=True)
    address = Column(String(250), nullable=False)
    zip = Column(Integer, nullable=False)


class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    cook_id = Column(Integer, ForeignKey(Cook.id), nullable=False)
    name = Column(String(250), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    CheckConstraint('price > 0.0', name='cost_positive')


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///argo_food.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)