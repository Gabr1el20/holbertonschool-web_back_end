#!/usr/bin/env python3
"task 0: Async Generator"
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """takes no args, yields a random number between 0 and 10."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
