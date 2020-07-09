"""
Custom, more discriptive, exceptions
"""


class DimensionError(Exception):
    """
    Called when an array or matrix has an Unexpected Dimension
    """


class NoInverseWarning(RuntimeWarning):
    """
    Warns the user that the matrix provided has no inverse
    """


class UnderDeterminedError(Exception):
    """
    Raised when a system of Linear equations is undetermined
    """


class InconsistentWarning(RuntimeWarning):
    """
    Raised when a system of linear equations has no solutions
    """


class InfiniteSolutionsWaring(RuntimeWarning):
    """
    Raised when a system of linear equations has infinite solutions
    """
