#!/usr/bin/env python3
"""task 9: annotate correctly"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """take a list with a sequence inside, and return a list
    that contains a tuple that contains the sequence member and its length"""
    saved = []
    for member in lst:
        saved.append((member, len(member)))
    return saved
