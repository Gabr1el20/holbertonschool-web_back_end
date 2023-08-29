#!/usr/bin/env python3
"Task 100: duck-type a first element of a sequence"
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    "safe_first_element() duck-typed"
    if lst:
        return lst[0]
    else:
        return None
