#!usr/bin/env python3
"""task 0: the basics of async"""
from random import uniform
import asyncio

async def wait_random(max_delay: int=10) -> float:
    """takes an int arg, waits for a random delay
    that has a max of max_delay value and eventually
    returns it"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
