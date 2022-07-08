"""Create model database"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from sys import argv
Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement="auto")
    first_name = Column(String(255))
    last_name = Column(String(255))
    UniqueConstraint(first_name, last_name)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<Author('%s','%s', '%s')>" % (self.id, self.first_name, self.last_name)


class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    title = Column(String(255), unique=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    
    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id

    def __repr__(self):
        return "<Book ('%s','%s','%s')>" % (self.id, self.title, self.author_id)


