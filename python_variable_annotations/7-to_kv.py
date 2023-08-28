#!/usr/bin/env python3
"Task 7: to_kv() function"
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string and an int/float and returns
    them into a tuple"""
    return k, v**2
