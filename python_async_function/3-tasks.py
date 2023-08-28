#!/usr/bin/env python3
"task 3: create tasks"
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an int and returns an asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
