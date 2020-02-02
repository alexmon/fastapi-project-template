'''
test.unit.test_utils.password
'''

from app.utils.password import hash_password, match_password

def test_match_password():
    plaintext = 'abcd1234'
    (s, h) = hash_password(plaintext)
    assert match_password(plaintext, s, h)
    pass

def test_not_match_password():
    plaintext = 'abcd1234'
    badpassword = 'abcd1235'
    (s, h) = hash_password(plaintext)
    assert not match_password(badpassword, s, h)
    pass