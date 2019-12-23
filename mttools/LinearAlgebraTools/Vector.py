from mttools.utils.Exceptions import DimensionError
from math import sqrt, acos, pi, isclose

import numbers


class Vector:
    def __init__(self, coords):
        if isinstance(coords, tuple) or isinstance(coords, list):
            if not coords:
                raise ValueError("Coords must not be empty.")
            self.coords = tuple(coords)
            self.dimension = len(coords)
        else:
            raise TypeError("Coords must be a list or tuple.")

    @property
    def magnitude(self):
        return sqrt(sum([a * a for a in self.coords]))

    @property
    def direction(self):
        if self.magnitude == 0:
            raise ZeroDivisionError(f"Cannot normalize the zero vector.")
        return [a / self.magnitude for a in self.coords]

    def normalize(self):
        return Vector(self.direction)

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise DimensionError(
                    f"Cannot add Vector with {self.dimension=} to Vector with {other.dimension=}."
                )
            new_coords = [a + b for a, b in zip(self.coords, other.coords)]
            return Vector(new_coords)
        else:
            raise TypeError(f"Expected Type 'Vector', got type '{type(other)}'.")

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise DimensionError(
                    f"Cannot add Vector with {self.dimension=} to Vector with {other.dimension=}."
                )
            new_coords = [a - b for a, b in zip(self.coords, other.coords)]
            return Vector(new_coords)
        else:
            raise TypeError(f"Expected Type 'Vector', got type '{type(other)}'.")

    def __mul__(self, other):
        # Dot Product
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise DimensionError(
                    f"Cannot compute dot product between Vector with {self.dimension=} and Vector with {other.dimension=}."
                )
            return sum([a * b for a, b in zip(self.coords, other.coords)])

        # Scalar Mul
        elif isinstance(other, numbers.Real):
            new_coords = [other * a for a in self.coords]
            return Vector(new_coords)

        else:
            raise TypeError(
                f"Expected Type 'Vector' or 'numbers.real', got type '{type(other)}'."
            )

    def __rmul__(self, other):
        return self * other

    def angle(self, other, unit="radians"):
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise DimensionError(
                    f"Cannot compute angle between Vector with {self.dimension=} and Vector with {other.dimension=}."
                )

            # Compute
            # theta = arccos(a · b /|a| × |b|)
            theta = acos((self * other) / (self.magnitude * other.magnitude))
            if unit == "degrees":
                theta = (theta * 180) / pi
            return theta

        else:
            raise TypeError(f"Expected Type 'Vector', got type '{type(other)}'.")

    def is_parallel(self, other):
        if self.magnitude == 0 or other.magnitude == 0:
            return True  # Zero vector is parallel to all other vectors

        theta = self.angle(other)
        if isclose(theta, pi) or isclose(theta, 0.0, abs_tol=10 ** -10):
            return True

        return False

    def is_orthogonal(self, other):
        if isclose(self * other, 0, abs_tol=10 ** -10):
            return True
        return False

    def parallel_component(self, basis):
        """
        Returns the component of the vector parallel to the basis
        """
        b_norm = basis.normalize()
        return (self * b_norm) * b_norm

    def orthogonal_component(self, basis):
        """
        Returns the component orthogonal to the basis
        """
        return self - self.parallel_component(basis)

    def components(self, basis):
        """
        returns the components for the given basis
        """
        return {
            "parallel": self.parallel_component(basis),
            "othogonal": self.orthogonal_component(basis),
        }

    def cross_product(self, other):
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

    def area(self, other):
        return self.cross_product(other).magnitude

    def __str__(self):
        return f"Vector: {list(self.coords)}"

    def __repr__(self):
        return f"Vector({self.coords})"

    def __eq__(self, other):
        return self.coords == other.coords
