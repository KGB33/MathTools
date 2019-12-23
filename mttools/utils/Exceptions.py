class DimensionError(Exception):
    """
    Called when an array or matrix has an Unexpected Dimension
    """

    pass


class NoInverseWarning(RuntimeWarning):
    """
    Warns the user that the matrix provided has no inverse
    """

    pass


class UnderDeterminedError(Exception):
    """
    Raised when a system of Linear equations is undetermined
    """

    pass


class InconsistentWarning(RuntimeWarning):
    """
    Raised when a system of linear equations has no solutions
    """

    pass


class InfiniteSolutionsWaring(RuntimeWarning):
    """
    Raised when a system of linear equations has infinite solutions
    """

    pass
