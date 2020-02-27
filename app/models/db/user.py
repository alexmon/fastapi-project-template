'''
app.models.user
'''

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .organization import Organization

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     email = Column(String, nullable=False, index=True, unique=True)
     password = Column(String, nullable=False)
     is_active = Column(Boolean, server_default='t', default=True)
     organization_id = Column(
          Integer, 
          ForeignKey('organizations.id', ondelete='CASCADE'),
          nullable=False)

     organization = relationship('Organization', backref='organizations')      

