import os
from dotenv import load_dotenv

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DB_URI = 'postgresql+psycopg2://postgres:{0}@localhost:5432/historical-market-visualizer'.format(os.getenv('POSTGRES_PASSWORD'))

# Create the engine for the PostgreSQL server
engine = create_engine(DB_URI)

# Our models inherits the declarative base model
BaseModel = declarative_base()
BaseModel.metadata.create_all(engine)

# Create the Session construct
Session = sessionmaker(bind=engine)

# Use a contextmanager to automate the DB session usage
@contextmanager
def session_scope():
    dbSession = Session(expire_on_commit=False)
    try:
        yield dbSession
        dbSession.commit()
    except Exception:
        dbSession.rollback()
        raise
    finally:
        dbSession.close()
