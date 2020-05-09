from __future__ import (
    annotations,
)  # Allows Vector type hints before the class is defined
from typing import (
    Any,
    Literal,
    Union,
    TypedDict,
    Tuple,
    List,
    cast,
    overload,
)
from cmath import sqrt, pi, isclose, acos
import numbers

from mttools.utils.exceptions import DimensionError
from mttools.utils.types import Number

# Types
class Components(TypedDict):
    parallel: Vector
    othogonal: Vector


class Vector:
    def __init__(self, coords: Union[Tuple[Number], List[Number]]):
        if isinstance(coords, (tuple, list)):
            if not coords:
                raise ValueError("Coords must not be empty.")
            self.coords = tuple(coords)
            self.dimension: int = len(coords)
        else:
            raise TypeError("Coords must be a list or tuple.")

    @property
    def magnitude(self) -> Number:
        return sqrt(sum([a * a for a in self.coords]))

    @property
    def direction(self) -> List[Number]:
        if self.magnitude == 0:
            raise ZeroDivisionError("Cannot normalize the zero vector.")
        return [a / self.magnitude for a in self.coords]

    def normalize(self) -> Vector:
        return Vector(self.direction)

    def _has_same_dim(
        self,
        other: Any,
        operation: Literal["add", "subtract", "multiply", "compute angle"],
    ) -> bool:
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise DimensionError(
                    f"Cannot {operation} Vector with {self.dimension=} to Vector with {other.dimension=}."
                )
        else:
            raise TypeError(f"Expected Type 'Vector', got type '{type(other)}'.")
        return True

    def __add__(self, other: Vector) -> Vector:
        self._has_same_dim(other, "add")
        return Vector([a + b for a, b in zip(self.coords, other.coords)])

    def __sub__(self, other: Vector) -> Vector:
        self._has_same_dim(other, "subtract")
        return Vector([a - b for a, b in zip(self.coords, other.coords)])

    @overload
    def __mul__(self, other: Vector) -> Number:
        ...

    @overload
    def __mul__(self, other: Number) -> Vector:
        ...

    def __mul__(self, other: Union[Vector, Number]) -> Union[Number, Vector]:
        # Dot Product
        try:
            self._has_same_dim(other, "multiply")
            other = cast(Vector, other)
            return self._dot_product(other)

        except TypeError:
            # Scalar Mul
            if isinstance(other, numbers.Number):
                other = cast(Number, other)
                return self._scalar_mul(other)
            raise TypeError(
                f"Expected Type 'Vector' or 'numbers.real', got type '{type(other)}'."
            )

    def __rmul__(self, other: Number) -> Vector:
        return self * other

    def _dot_product(self, other: Vector) -> Number:
        return sum([a * b for a, b in zip(self.coords, other.coords)])

    def _scalar_mul(self, other: Number) -> Vector:
        return Vector([other * a for a in self.coords])

    def angle(
        self, other: Vector, unit: Literal["radians", "degrees"] = "radians"
    ) -> Number:
        self._has_same_dim(other, "compute angle")

        # theta = arccos(a · b /|a| × |b|)
        theta = acos((self * other) / (self.magnitude * other.magnitude))
        if unit == "degrees":
            theta = (theta * 180) / pi
        return theta

    def is_parallel(self, other: Vector) -> bool:
        if self.magnitude == 0 or other.magnitude == 0:
            return True  # Zero vector is parallel to all other vectors

        theta = self.angle(other)
        if isclose(theta, pi) or isclose(theta, 0.0, abs_tol=10 ** -10):
            return True

        return False

    def is_orthogonal(self, other: Vector) -> bool:
        if isclose(self * other, 0, abs_tol=10 ** -10):
            return True
        return False

    def parallel_component(self, basis: Vector) -> Vector:
        """
        Returns the component of the vector parallel to the basis
        """
        b_norm = basis.normalize()
        return (self * b_norm) * b_norm

    def orthogonal_component(self, basis: Vector) -> Vector:
        """
        Returns the component orthogonal to the basis
        """
        return self - self.parallel_component(basis)

    def components(self, basis: Vector) -> Components:
        """
        returns the components for the given basis
        """
        return {
            "parallel": self.parallel_component(basis),
            "othogonal": self.orthogonal_component(basis),
        }

    def cross_product(self, other: Vector) -> Vector:
        if self.dimension != 3:
            raise DimensionError(
                f"Cannot compute cross product with vector who's dimention is not 3 ({self.dimension=})."
            )
        if other.dimension != 3:
            raise DimensionError(
                f"Cannot compute cross product with vector who's dimention is not 3 ({other.dimension=})."
            )
        ijk = [
            (self.coords[1] * other.coords[2] - self.coords[2] * other.coords[1]),
            -1 * (self.coords[0] * other.coords[2] - self.coords[2] * other.coords[0]),
            (self.coords[0] * other.coords[1] - self.coords[1] * other.coords[0]),
        ]
        return Vector(ijk)

    def area(self, other: Vector) -> Number:
        return self.cross_product(other).magnitude

    def __str__(self):
        return f"Vector: {list(self.coords)}"

    def __repr__(self):
        return f"Vector({self.coords})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            return self.coords == other.coords
        return NotImplemented
