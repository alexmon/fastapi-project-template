'''
app.models.organization
'''

from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Organization(Base):
     __tablename__ = 'organizations'

     id = Column(Integer, primary_key=True)
     name = Column(String, nullable=False, index=True, unique=True)
     is_active = Column(Boolean, server_default='t', default=True)