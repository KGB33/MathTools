"""
A Collection of custom types for static type checking
"""
from typing import Union

RealNumber = Union[int, float]
Number = Union[RealNumber, complex]
