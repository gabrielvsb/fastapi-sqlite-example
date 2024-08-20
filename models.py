from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column

from database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)

    books = relationship("Book", back_populates="author")


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

    purchases = relationship("Sale", back_populates="client")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = mapped_column(ForeignKey('authors.id'))

    author = relationship("Author", back_populates="books")

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    client_id = mapped_column(ForeignKey('clients.id'))
    book_id = mapped_column(ForeignKey('books.id'))

    client = relationship('Client', back_populates='purchases')
    book = relationship('Book')
    