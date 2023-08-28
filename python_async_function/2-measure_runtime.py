#!/usr/bin/env python3
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """takes two int as args, measures the total execution time
    for wait_n, and returns total_time / n"""
    start = time.perf_counter()
    execution = asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter - start
    return end / n
