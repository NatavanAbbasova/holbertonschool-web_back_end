#!/usr/bin/env python3
"""Measure how long the async code runs."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Check the time to run async_comprehension 10 times."""
    tasks = [async_comprehension() for _ in range(10)]

    start_time = time.perf_counter()
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()

    return end_time - start_time
