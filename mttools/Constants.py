from typing import TypeVar, Union

# Custom Types Variables
Prime = TypeVar("Prime", bound=int)
RealNumber = Union[int, float]
Number = Union[RealNumber, complex]

EPSILON = pow(10, -15)
