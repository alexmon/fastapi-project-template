'''
app.utils.password
'''

import typing
import hashlib, uuid

def hash_password(plaintext_pwd: str) -> tuple():
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512((plaintext_pwd + salt).encode('utf-8')).hexdigest()
    return (salt, hashed_password)


def match_password(plaintext_pwd: str, salt: str, hashed_password: str) -> bool:
    return hashlib.sha512((plaintext_pwd + salt).encode('utf-8')).hexdigest() == hashed_password


    