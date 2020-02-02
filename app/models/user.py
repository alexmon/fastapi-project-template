# app.models.user

from .base import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     email = Column(String, nullable=False)
     password = Column(String, nullable=False)
     is_active = Column(Boolean, server_default='t', default=True)