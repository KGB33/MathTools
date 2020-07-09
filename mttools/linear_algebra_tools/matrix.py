from mttools.utils.exceptions import DimensionError, NoInverseWarning


class Matrix:
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
        for row in array:
            if len(row) != len(array[0]):
                print("Array is not rectangular, Cannot be a matrix")
                raise DimensionError

        self.array = array
        self.num_rows = len(array)
        self.num_columns = len(array[0])

    def __str__(self):
        result = ""
        for row in self.array:
            result += "[ "
            for value in row:
                result += str(value) + ", "
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
        if self.num_columns != other.num_rows:
            raise DimensionError(
                f"The number of columns in the RH maxtrix must equal the number of rows in the LH (got {self.num_columns} and {other.num_rows})"
            )
        new_array = self.zero_array(
            num_rows=self.num_rows, num_columns=other.num_columns
        )
        for r, row in enumerate(new_array):
            for c, _ in enumerate(row):
                new_array[r][c] = sum(
                    [
                        self.array[r][k] * other.array[k][c]
                        for k in range(self.num_columns)
                    ]
                )
        return self.__class__(new_array)

    def __add__(self, other):
        """
        Implements the addition operator between two matrices

        :param other: (Matrix Object)
            Matrix to add

        :return: (Matrix object)
            Sum of self + other
        """
        if self.num_rows != other.num_rows or self.num_columns != other.num_columns:
            raise DimensionError
        new_array = self.zero_array()
        for r, (s_row, o_row) in enumerate(zip(self.array, other.array)):
            for c, (s_val, o_val) in enumerate(zip(s_row, o_row)):
                new_array[r][c] = s_val + o_val
        return self.__class__(new_array)

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
                raise DimensionError("Array is not square, Use Matrix Instead")
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
