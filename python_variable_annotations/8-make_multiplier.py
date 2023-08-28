#!/usr/bin/env python3
"task 8: make_multiplier() function"
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def func(x: float) -> float:
        return x * multiplier
    return func
