class InvalidDimensionError():
    ''' An error to be raised when a dimension of a matrix which does not
    exist is trying to be accessed.'''
    pass


class MathError():
    ''' An error to be raised when doing math operations on incompatable types.
    i.e(adding a string to an integer).'''
    pass


class ValueTypeError():
    ''' An error to be raised when the user attempts to input a value in a
    matrix which does not support the values type.
    i.e (putting a float in a string matrix).'''
    pass


class InvalidMatrixError():
    ''' An error to be raised when the user attempts to perform a math
    operation on incompatible matrices. i.e(getting the determinant of a non
    2x2 matrix). '''
    pass


class Matrix():
    ''' A class representing a mathematical matrix.'''

    def __init__(self, row_size, col_size):
        '''
        (Matrix, int, int) -> NoneType
        Create a matrix with n amount of rows, and m amount of columns, which
        are given by the user.
        REQ: row_size is an int
        REQ: col_size is an int
        '''
        pass

    def __str__(self):
        '''
        (Matrix) -> Matrix
        Print out a representation of the matrix.
        REQ: None
        '''
        pass

    def set_value(self, row, col, value=None):
        '''
        (Matrix, int, int, int) -> NoneType
        Change the value of a single element in the matrix. The value will
        be changed on (row, col), where the first element in the tuple is
        the row, and the second is the column of the matrix.
        REQ: row > 0
        REQ: col > 0
        REQ: value is an int
        '''
        pass

    def get_value(self, row, col):
        '''
        (Matrix, int, int) -> int
        Return the value of a single element in the matrix. This method
        will return value (row, col), where the first element in the tuple
        is the row, and the second is the column of the matrix.
        REQ: row > 0
        REQ: col > 0
        '''
        pass

    def swap_row(self, curr_row, new_row):
        '''
        (Matrix, int, int) -> NoneType
        Swap two rows of a matrix. The row to be switched, curr_row, will
        be swapped with another row, new_row.
        REQ: curr_row > 0 and curr_row <= self.row
        REQ: new_row > 0 and new_row <= self.row
        '''
        pass

    def swap_col(self, curr_col, new_col):
        '''
        (Matrix, int, int) -> NoneType
        Swap two existing columns of a matrix. curr_col will be switched with
        new_col.
        REQ: curr_col > 0 and curr_col <= self.col
        REQ: new_col > 0 and new_col <= self.col
        '''
        pass

    def add(self, new_matrix):
        '''
        (Matrix, Matrix) -> Matrix
        Add the values of 2 independent matrices. The current matrix will be
        added to new_matrix.
        REQ: Matrices must be the same size
        '''
        pass

    def subtract(self, new_matrix):
        '''
        (Matrix, Matrix) -> Matrix
        Subtract 2 independent matrices. The new_matrix will be subtracted
        from the current matrix.
        REQ: Matrices must be the same size
        '''
        pass

    def multiply(self, new_matrix):
        '''
        (Matrix, Matrix) -> Matrix
        Multiply two independent matrices. The current matrix will be
        multiplied with new_matrix.
        REQ: The first matrix has the same amount of columns as the second
        matrix has rows. (i.e n x m and m x w)
        '''
        pass

    def transpose(self):
        '''
        (Matrix) -> NoneType
        Transpose a matrix. The index of each individual values row and column
        will be switched, keeping only the main diagonal the same.
        REQ: None
        '''
        pass


class StrMatrix(Matrix):
    ''' A class representing a matrix holding strings. '''

    def add(self, new_matrix):
        '''
        (Matrix, Matrix) -> Matrix
        Add 2 matrices holding string values. The current matrix will be
        added to new_matrix.
        REQ: Matrices are the same size
        '''
        pass


class SquareMatrix(Matrix):
    ''' A class representing an n x n square matrix. '''

    def __init__(self, row_and_col_size):
        '''
        (Matrix, int) -> NoneType
        Create a square matrix, with an equal amount of rows and columns.
        REQ: row_and_col_size > 0
        '''
        pass

    def get_determinant(self):
        '''
        (Matrix) -> int
        Calculate and return the determinant of a 2x2 matrix.
        REQ: Matrix must be 2x2
        '''
        pass

    def set_diag(self, value):
        '''
        (Matrix, int) -> NoneType
        Set the main diagonal of the square matrix to a value.
        REQ: value is an int
        '''
        pass


class SymmetricMatrix(SquareMatrix):
    ''' A class representing a symmetrical square matrix. '''

    def set_value(self, row, col, value):
        '''
        (Matrix, int) -> NoneType
        Change one value of a symmetric matrix and change its mirror too.
        REQ: value is an int
        REQ: Matrix is n x n, where n > 0
        '''
        pass


class DiagMatrix(SymmetricMatrix):
    ''' A class representing a diagonal square matrix. '''

    def __init__(self, row_and_col, diag_value):
        '''
        (DiagMatrix, int, int) -> NoneType
        Create a diagonal matrix with an equal amount of rows and columns
        and the same value across the main diagonal.
        REQ: diag_value is an int
        REQ: row_and_col > 0
        '''
        pass

    def get_diag(self):
        '''
        (DiagMatrix) -> int
        Return the value of the integer which makes up the main diagonal
        of the matrix.
        REQ: None
        '''
        pass

    def set_diag(self, value):
        '''
        (DiagMatrix, int) -> NoneType
        Change the value of the integer which makes up the main diagonal
        of the matrix.
        REQ: value is an int
        '''
        pass


class IdentityMatrix(DiagMatrix):
    ''' A class representing an identity matrix. '''

    def __init__(self, m_size):
        '''
        (IdentityMatrix, int) -> NoneType
        Create a square identity matrix, with a size of m_size. The values
        of the main diagonal are all 1 by definition of an identity matrix.
        REQ: m_size > 0
        '''
        pass


class OneDimMatrix(Matrix):
    ''' A class representing a one-dimensional matrix. '''

    def __init__(self, is_vertical=True, size):
        '''
        (OneDimMatrix, bool, int) -> NoneType
        Create a one-dimensional matrix, which is either 1 x col_size or
        row_size x 1 (either a column matrix or row matrix).
        REQ: if is_vertical == True, matrix is a 1 x n row matrix
        REQ: else, matrix is n x 1 column matrix
        '''
        pass

    def get_value(self, index):
        '''
        (OneDimMatrix, int) -> int
        Retrieve a value of the matrix at an index given by the user.
        REQ: index is within the size of the matrix
        '''
        pass

    def set_value(self, index, value):
        '''
        (OneDimMatrix, int, int) -> NoneType
        Set a value in the matrix at an index given by the user.
        REQ: index is within size of the matrix
        REQ: value is an int
        '''
        pass
