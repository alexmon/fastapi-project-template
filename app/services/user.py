'''
app.services.user
'''

import typing
from .database import session
from app.models.user import User

def get_by_username(username: str) -> User:
    return session.query(User).filter_by(email=username).first()

