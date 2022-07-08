"""DB query add books and author and get data from database """
from sys import argv
from models import Author, Book, Base
from connect import session, engine
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import logging

"""Use parametr setup when first time call program to create new tabel to database"""
if len(argv) > 1 and argv[1] == 'setup':
    Base.metadata.create_all(engine)

logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class Database:

    def create_session(self, data):
        try: 
                session.add(data)
                session.commit()
        except IntegrityError as e:
            logging.error(e.orig)
            raise e.orig
        except SQLAlchemyError as e:
            logging.error(f"Unexpected error when creating user: {e}")
            raise e
        finally:
            session.close()

    def add_book(self, title_book):
        book_add = Book(title_book)
        self.create_session(book_add)

    def add_author(self, author_first_name, author_last_name):
        author_add = Author(author_first_name, author_last_name)
        self.create_session(author_add)

    def get_authors(self):
        return session.query(Author.first_name, Author.last_name).all()

    def get_all_books(self):
        return session.query(Book.title, Author.first_name, Author.last_name).filter(Book.author_id==Author.id).all()