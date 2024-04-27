#!/usr/bin/env python3
'''The measure_runtime coroutine will execute async_comprehension
four times in parallel using asyncio.gather'''


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measure the runtime of async_comprehension'''

    start = time.time()
    await asyncio.gather(*async_comprehension() for x in range(4))
    end = time.time()
    return end - start
