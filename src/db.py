from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_URI
from contextlib import contextmanager
from sqlalchemy.orm import declarative_base


engine = create_engine(DB_URI)

BaseModel = declarative_base()
BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    dbSession = Session()
    try:
        yield dbSession
        dbSession.commit()
    except Exception:
        dbSession.rollback()
        raise
    finally:
        dbSession.close()



