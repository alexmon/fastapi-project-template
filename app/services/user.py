'''
app.services.user
'''

import typing
from .database import session
from app.models.user import User
from app.utils.password import hash_password, match_password

def authenticate(username: str, password: str) -> User:
    user = session.query(User).filter_by(email=username).first()
    if not user:
        return None
    if not match_password(password, user.hashed_password):
        return False
    return user      

def set_password(plaintext_pwd: str, user: User) -> bool:
    if len(plaintext_pwd) < 8:
        return False
    user.password = hash_password(plaintext_pwd)
    return True
    

    
