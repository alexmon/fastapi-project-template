'''
app.models.user
'''

from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     email = Column(String, nullable=False, index=True, unique=True)
     password = Column(String, nullable=False)
     is_active = Column(Boolean, server_default='t', default=True)
