'''
app.models.client
'''

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class Client(Base):
     __tablename__ = 'clients'

     id = Column(Integer, primary_key=True)
     client_id = Column(UUID(as_uuid=True), nullable=False, unique=True)
     client_secret = Column(String, nullable=False, unique=True)
     grant_type = Column(String, nullable=False)
     response_type = Column(String, nullable=False)
     scopes = Column(String, nullable=False)
     organization_id = Column(
          Integer, 
          ForeignKey('organizations.id', ondelete='CASCADE'),
          nullable=False)
     is_active = Column(Boolean, server_default='t', default=True)

     organization = relationship('Organization', backref='organizations') 

