#!/usr/bin/env python3
""" Encrypt password """


import bcrypt


def hash_password(password: str) -> bytes:
    """ hash encryption """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that the provided password matches the hashed password.
    """
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False
    