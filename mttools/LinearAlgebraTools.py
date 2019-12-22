from mttools.Exceptions import (
    DimensionError,
    InconsistentWarning,
    InfiniteSolutionsWaring,
    NoInverseWarning,
    UnderDeterminedError,
)


class Vector:
    def __init__(self, coords):
        if isinstance(coords, tuple) or isinstance(coords, list):
            if not coords:
                raise ValueError("Coords must not be empty.")
            self.coords = tuple(coords)
            self.dimension = len(coords)
        else:
            raise TypeError("Coords must be a list or tuple.")

    def __str__(self):
        return f"Vector: {list(self.coords)}"

    def __repr__(self):
        return f"Vector({self.coords})"

    def __eq__(self, other):
        return self.coords == other.coords


class Matrix(object):
    """
    Models matrix objects

    Rows by Columns

    Attributes:
        :array: (Array Like)
            The matrix

        :num_rows: (int)
            Number of rows

        :num_columns: (int)
            Number of Columns

    """

    def __init__(self, array):
        """
        :param array: (NxM array-like)
            Array of M, N-length arrays
        """
        for a in array:
            if len(a) != len(array[0]):
                print("Array is not rectangular, Cannot be a matrix")
                raise DimensionError
        else:
            self.array = array
            self.num_rows = len(array)
            self.num_columns = len(array[0])

    def __str__(self):
        result = ""
        for r in self.array:
            result += "[ "
            for n in r:
                result += str(n) + ", "
            result += "]\n"
        return result

    def __mul__(self, other):
        """
        Implements the multilation operator between two matrices

        :param other: (Matrix Object)
            Matrix to multiply by
        :return: (Matrix Object)
            Product
        """
        if self.num_columns == other.num_rows:
            new_array = self.zero_array(
                num_rows=self.num_rows, num_columns=other.num_columns
            )
            for r, row in enumerate(new_array):
                for c, val in enumerate(row):
                    new_array[r][c] = sum(
                        [
                            self.array[r][k] * other.array[k][c]
                            for k in range(self.num_columns)
                        ]
                    )
            return Matrix(new_array)
        else:
            raise DimensionError

    def __add__(self, other):
        """
        Implements the addition operator between two matrices

        :param other: (Matrix Object)
            Matrix to add

        :return: (Matrix object)
            Sum of self + other
        """
        # Check that matrices have the same dimensions
        if self.num_rows == other.num_rows and self.num_columns == other.num_columns:
            new_array = self.zero_array()
            for r, (s_row, o_row) in enumerate(zip(self.array, other.array)):
                for c, (s_val, o_val) in enumerate(zip(s_row, o_row)):
                    new_array[r][c] = s_val + o_val
            # TODO: Return type called i.e, if they're SquareMatrix return SquareMatrix
            return Matrix(new_array)
        else:
            raise DimensionError

    def zero_array(self, num_rows=None, num_columns=None):
        """
        Creates an array with the dimensions provided, (default same dim as self),
        where all values are zero

        :param num_rows: (int, Optional, default = same as self)
            Number of rows
        :param num_columns: (int, Optional, default = same as self)
            Number of columns
        :return: (list)
            List with all values == 0
        """
        if num_rows is None:
            num_rows = self.num_rows
        if num_columns is None:
            num_columns = self.num_columns
        return [[0 for _ in range(num_columns)] for _ in range(num_rows)]

    def scalar_multiplication(self, scalar):
        """
        Multiples matrix by a scalar

        :param scalar: (Numeric)
            Number to multiply by
        """
        new_array = self.zero_array()
        for r, row in enumerate(self.array):
            for c, value in enumerate(row):
                new_array[r][c] = value * scalar
        self.array = new_array

    def transpose(self):
        """
        Transposes matrix
        """
        new_array = self.zero_array(
            num_rows=self.num_columns, num_columns=self.num_rows
        )
        for r, row in enumerate(self.array):
            for c, val in enumerate(row):
                new_array[c][r] = val
        self.array = new_array

    def swap_rows(self, row_1, row_2):
        """
        First Elementary Row operation
            Swap two rows

        :param row_1: (int)
            index of the first row
        :param row_2: (int)
            index of the second row
        """
        self.array[row_1], self.array[row_2] = self.array[row_2], self.array[row_1]

    def multiply_row(self, row_num, scalar):
        """
        Second Elementary Row operation
            multiply one row by a scalar

        :param row_num: (int)
            index of row
        :param scalar: (numeric)
            scalar to multiply row by
        """
        self.array[row_num] = [scalar * x for x in self.array[row_num]]

    def add_rows(self, from_row, to_row, scalar=1):
        """
        Third Elementary Row Operation
            Add a multiple of one row to another

        Example:
            to_row += scalar * from_row

        :param from_row: (int)
            index of row to add to to_row
        :param to_row: (int)
            index of row being added to
        :param scalar: (numeric, Optional, default=1)
            optional multiple for from_row
        """
        self.array[to_row] = [
            scalar * y + x for x, y in zip(self.array[to_row], self.array[from_row])
        ]

    def rref(self):
        """
        Puts the matrix in Reduced Row Echelon Form
        """
        lead = 0
        for r in range(self.num_rows):
            if lead >= self.num_columns:
                return
            i = r
            while self.array[i][lead] == 0:
                i += 1
                if i == self.num_rows:
                    i = r
                    lead += 1
                    if self.num_columns == lead:
                        return
            self.swap_rows(i, r)
            lv = self.array[r][lead]
            self.multiply_row(r, (1 / lv))
            for i in range(self.num_rows):
                if i != r:
                    lv = self.array[i][lead]
                    self.add_rows(r, i, -lv)
            lead += 1

    def rank(self):
        """
        Calculates the Rank of a matrix without modifying the current matrix

        :return: (int)
            Rank of self
        """
        new_matrix = Matrix(self.array)
        new_matrix.rref()
        num_non_zero_rows = 0
        for row in new_matrix.array:
            is_non_zero = False
            for val in row:
                if val != 0:
                    is_non_zero = True
            if is_non_zero:
                num_non_zero_rows += 1
        return num_non_zero_rows


class SquareMatrix(Matrix):
    """
    Models a Square matrix

        Attributes:
            :array: (Array Like)
                The matrix

            :num_rows: (int)
                Number of rows

            :num_columns: (int)
                Number of Columns
    """

    def __init__(self, array):
        """
        :param array: (NxN array-like)
            Array of N, N-length arrays
        """
        for a in array:
            if len(a) != len(array):
                print("Array is not square, Use Matrix Instead")
                raise DimensionError
        else:
            super().__init__(array)

    def identity_matrix(self, size=None):
        """
        Creates an identity array with the dimensions provided, (default same dim as self),

        :param size: (int, Optional, default = same as self)
            Number of rows & columns
        :return: (list)
            List with all values == 0
        """
        if size is None:
            size = self.num_rows
        a = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            a[i][i] = 1
        return SquareMatrix(a)

    def inverse(self):
        """
        Calculates then sets self.array as the Inverse of self, if one exists
        """
        if self.determinate() == 0:
            raise NoInverseWarning(self.__str__())
        # Do ERO on array and identity matrix to get inverse
        else:
            new_array = self.identity_matrix()

            lead = 0
            for r in range(self.num_rows):
                if lead >= self.num_columns:
                    return
                i = r
                while self.array[i][lead] == 0:
                    i += 1
                    if i == self.num_rows:
                        i = r
                        lead += 1
                        if self.num_columns == lead:
                            return
                # Swap Rows
                self.swap_rows(i, r)
                new_array.swap_rows(i, r)

                lv = self.array[r][lead]

                # Multiply row
                self.multiply_row(r, (1 / lv))
                new_array.multiply_row(r, (1 / lv))

                for i in range(self.num_rows):
                    if i != r:

                        # Add rows
                        lv = self.array[i][lead]
                        self.add_rows(r, i, -lv)
                        new_array.add_rows(r, i, -lv)

                lead += 1
            self.array = new_array.array

    def minor(self, row_number, col_number):
        """
        Returns the matrix made by removing the col number and row number provided

        :param row_number: (int)
            Row number to remove

        :param col_number: (int)
            Col number to remove

        :return: (SquareMatrix)
            The minor for Row, Col provided
        """
        new_array = self.zero_array(
            num_columns=self.num_columns - 1, num_rows=self.num_rows - 1
        )
        i = 0
        for r, row in enumerate(self.array):
            if r == row_number - 1:
                continue
            j = 0
            for c, val in enumerate(row):
                if c == col_number - 1:
                    continue
                new_array[i][j] = val
                j += 1
            i += 1

        if self.num_columns == 2:
            return new_array[0][0]

        return SquareMatrix(new_array)

    def determinate(self):
        """
        Calculates the determinate of self

        :return: (numeric)
            the determinate
        """
        r = 1  # "first" index in the matrix
        total = 0
        for c in range(1, self.num_columns + 1):  # add one because matrix start at one
            val = self.array[r - 1][c - 1]
            sign = pow(-1, (r + c))
            m = self.minor(r, c)
            if isinstance(m, SquareMatrix):
                det_m = m.determinate()
            else:
                det_m = m
            total += val * sign * det_m
        return total

    def trace(self):
        """
        Calculate the trace of self

        :return: (numeric)
            trace of self.array
        """
        total = 0
        for i in range(self.num_columns):
            total += self.array[i][i]
        return total


def solve_linear_equations(*args):
    """
    Solves a system of linear equations

    :param args: (dicts)
        {variable: coefficient} pairs, one dictionary per equation
        if a coefficient is zero it NEEDS to be in the dict.
        the last key: value pair should be the solution (RH) of the equation

    :return: (dict)
        {variable: value} pairs
    """
    # Check to see if solution is underdetermined (num_eq < num_var)
    if len(args) < len(args[0]) - 1:  # -1 for sol key
        raise UnderDeterminedError

    # Create solution dict
    solution = {key: None for key in args[0]}
    del solution["sol"]  # removes unneeded key

    # Convert Dicts to matrix
    to_array = []
    for equation in args:
        to_row = []
        for variable in equation:
            to_row.append(equation[variable])
        to_array.append(to_row)
    m = Matrix(to_array)

    # Put Matrix in Reduced-Row Echelon Form
    m.rref()

    # Check matrix for num_solutions
    inf_sol = [0 for _ in range(m.num_columns)]
    no_sol = inf_sol[:-1] + [1]
    for row in m.array:
        if row == inf_sol:
            raise InfiniteSolutionsWaring
        elif row == no_sol:
            raise InconsistentWarning

    # Convert matrix to solution dict
    for row in m.array:
        variable_key = None
        for value, key in zip(row, solution):
            if value == 1:
                variable_key = key
        solution.update({variable_key: row[-1]})

    # Return solution
    return solution
