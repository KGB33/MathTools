"""
A Collection of geometry realated function and tools.
"""

from math import sqrt


def distance(cord_1, cord_2):
    """
    Calculates the Euclidean distance between two points.
        Points must have the same dimensions

    :param cord_1: (Array-like, numeric)
        Coords of First Point

    :param cord_2: (Array-like, numeric)
        Coords of Second Point

    :return: (float)
        Distance between the two points

    Examples:
        distance([0], [5])) --> 5
        distance([0, 0, 0, 0], [5, 5, 5, 5]) --> 10

    """
    if len(cord_1) == len(cord_2):
        sum_squares = 0
        for i, j in zip(cord_1, cord_2):
            sum_squares += pow(i - j, 2)
        return sqrt(sum_squares)
