"""
A Collection of geometry realated function and tools.
"""

from math import sqrt
from typing import List

from mttools.utils.types import Number


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
