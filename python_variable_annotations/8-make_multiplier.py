#!/usr/bin/env python3
'''Type-annoted function that takes a float as argument
and returns a function that multiplies a float'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''make_multiplier function'''
    def multiplier_function(float):
        return multiplier * float
    return multiplier_function
