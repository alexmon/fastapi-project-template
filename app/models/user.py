'''
app.models.user
'''

from sqlalchemy import Column, Integer, String, Boolean
from app.utils.password import hash_password, match_password
from .base import Base

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     email = Column(String, nullable=False, index=True, unique=True)
     password = Column(String, nullable=False)
     salt = Column(String, nullable=False)
     is_active = Column(Boolean, server_default='t', default=True)

     def set_password(self, plaintext_pwd: str):
          if len(plaintext_pwd) < 8:
               raise Exception('password is lessa than 8 characters')
          (self.salt, self.password) = hash_password(plaintext_pwd)
     
     def match_password(self, plaintext_pwd: str) -> bool:
          return match_password(
               plaintext_pwd, 
               self.salt, 
               self.password
          )