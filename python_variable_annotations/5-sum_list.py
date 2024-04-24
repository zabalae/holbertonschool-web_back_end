#!/usr/bin/env python3
'''Type-annoted function which takes a list of floats
as argument and returns their sum as a float'''
from typing import List

def sum_list(input_list: List[float]) -> float:
    '''sum_list function'''
    return sum(input_list)
