"""Create SQLAlchemy engine and session objects."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(getenv('URL_CONNECT_DATABASE'))

Session = sessionmaker(bind=engine)
session = Session()
