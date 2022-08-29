from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from decouple import config 

# postgres remote db connection string
connection_string = config("con_str")

# init base class
Base = declarative_base()

# init db engine
engine = create_engine(connection_string, echo=True)

# create session instance for db query 
Session = sessionmaker()