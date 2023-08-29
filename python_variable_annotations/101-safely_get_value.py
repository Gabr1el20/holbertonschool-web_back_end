#!/usr/bin/env python3
"Task 101: More involved type annotations"
from typing import Mapping, Union, Any, NewType, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:  # noqa: E501
    if key in dct:
        return dct[key]
    else:
        return default
