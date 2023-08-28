#!/usr/bin/env python3
"task1: concurrent coroutines"
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times and append the results
    of the max_delay in each case in a list, and return it."""
    list_of_secs = []
    for _ in range(n):
        result = await (task_wait_random(max_delay))
        list_of_secs.append(result)
    return sorted(list_of_secs)
