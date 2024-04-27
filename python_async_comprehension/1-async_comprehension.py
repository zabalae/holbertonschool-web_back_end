#!/usr/bin/env python3
'''The async_comprehension coroutine will collect 10 random
numbers using an async comprehensing over async_generator
then return 10 random numbers.'''


import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''The async_comprehension coroutine will collect 10 random numbers'''

    return [x async for x in async_generator()]
