"""
A Collection of geometry realated function and tools.
"""

from utils.Types import Numeric

from math import sqrt


def distance(start: List[Numeric], end: List[Numeric]) -> Numeric:
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
