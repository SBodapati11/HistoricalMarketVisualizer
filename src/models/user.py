from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    userId = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "User: {0}".format(self.username)
