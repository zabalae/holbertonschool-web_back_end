#!/usr/bin/env python3
'''function that return values with the appropiate
types'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''element_length function'''
    return [(i, len(i)) for i in lst]
