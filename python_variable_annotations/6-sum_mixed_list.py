#!/usr/bin/env python3
"""task 6, sum_mixed_list() function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "a function that returns the sum of a mixed list"
    sum_returned: float = 0
    for member in mxd_lst:
        sum_returned += member
    return sum_returned
