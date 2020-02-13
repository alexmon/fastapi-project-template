'''
app.utils.password
'''

import typing
import hashlib, uuid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plaintext_pwd: str) -> str:
    return pwd_context.hash(plaintext_pwd)


def match_password(plaintext_pwd: str, hashed_password: str) -> bool:
    return pwd_context.verify(plaintext_pwd, hashed_password)


    