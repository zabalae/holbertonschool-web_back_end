#!/usr/bin/env python3
'''Duck-typed annotations'''
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''safe_first_element function'''
    if lst:
        return lst[0]
    else:
        return None
