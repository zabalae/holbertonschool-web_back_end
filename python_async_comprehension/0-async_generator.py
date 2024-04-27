#!/usr/bin/env python3
'''The async_generator coroutine will loop 10 times then
yield a random number between 0 and 10'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''The async_generator coroutine will yield a random
    number between 0 and 10'''

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
