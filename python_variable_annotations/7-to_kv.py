#!/usr/bin/env python3
'''Type_annotated function that takes a string and an int or
float as arguments and returns a tuple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''to_kv function'''
    return (k, float(v**2))
