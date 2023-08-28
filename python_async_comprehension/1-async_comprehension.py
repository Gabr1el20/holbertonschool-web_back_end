#!/usr/bin/env python3
"task 1: Async comprehension"
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[list, None, None]:
    """this coroutine will collect 10 random numbers
    using an async comprehension over async_generator, then
    will return all those numbers."""
    list_of_yields = []
    async for i in async_generator():
        list_of_yields.append(i)
    return list_of_yields
