"""
A Collection of geometry realated function and tools.
"""

from math import sqrt, pi
from typing import List

from mttools.utils.types import Number
from mttools.utils.exceptions import DimensionError


def distance(start: List[Number], end: List[Number]) -> Number:
    """
    Calculates the Euclidean distance between two points.
        Points must have the same dimensions


    Examples:

    >>> distance([0], [5]))
    5
    >>> distance([0, 0, 0, 0], [5, 5, 5, 5])
    10

    """
    if len(start) != len(end):
        raise ValueError(
            f"start and end must have the same length, got {len(start)} and {len(end)}"
        )
    return sqrt(sum([pow(i - j, 2) for i, j in zip(start, end)]))


def area_of_circle(radius: Number) -> Number:
    """
    Calculates the area of a Circle with a given radius

    Examples:

    >>> area_of_circle(3)
    28.274333882308138
    >>> area_of_circle(-48)
    7238.229473870883
    >>> area_of_circle(3+2j)
    40.840704496667314

    """
    radius = sqrt(radius.real * radius.real + radius.imag * radius.imag)
    return radius * radius * pi
