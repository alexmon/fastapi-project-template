# app.models.user

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     email = Column(String)
     password = Column(String)
     is_active = Column(Boolean, default=1)