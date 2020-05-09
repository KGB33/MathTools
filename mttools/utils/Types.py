"""
A Collection of custom types for static type checking
"""
from typing import Union

RealNumber = Union[int, float]
Numeric = Union[RealNumber, complex]
