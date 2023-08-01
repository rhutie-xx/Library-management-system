# models.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='books')

Category.books = relationship('Book', order_by=Book.id, back_populates='category')

engine = create_engine('sqlite:///ruth.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
