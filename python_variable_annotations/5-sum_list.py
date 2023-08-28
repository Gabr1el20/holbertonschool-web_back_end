#!/usr/bin/env python3
"""a sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    return_sum: float = 0
    for member in input_list:
        return_sum += member
    return return_sum
