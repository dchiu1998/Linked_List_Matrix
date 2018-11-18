class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''


class MatrixDimensionError(Exception):
    '''An attempt has been made to perform an operation on this matrix which
    is not valid given its dimensions'''


class MatrixInvalidOperationError(Exception):
    '''An attempt was made to perform an operation on this matrix which is
    not valid given its type'''


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, contents, row=None, col=None, right=None, down=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        '''
        self._contents = contents
        self._right = right
        self._down = down
        self._row = row
        self._col = col

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_row(self):
        '''
        (MatrixNode) -> int
        Return the row this node belongs to.
        '''
        return self._row

    def get_col(self):
        '''
        (MatrixNode) -> int
        Return the column this node belongs to.
        '''
        return self._col

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node


class Matrix():
    '''A class to represent a mathematical matrix
    Note: Uses 0-indexing, so an m x n matrix will have
    indices (0,0) through (m-1, n-1)'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        REQ: m is an int > 0
        REQ: n is an int > 0
        REq: default is some real number
        '''
        # Representation Invariant
        # self._head is a Node representing the start of the Matrix
        # self._rows is an integer indicating the amount of rows in the matrix
        # self._cols in an integer indicating # of columns in the matrix
        # if self._rows == self._cols, then Matrix is a Square Matrix
        # if self._rows == self._cols == 0, the Matrix is a single Node
        # self._existing_rows is a list containing rows that exist in
        # the matrix, entered by the user
        # self._existing_cols is a list containing columns which exist in
        # the matrix
        # if i is in self._existing_rows, then i is an index node in the matrix
        # self._default is a float value representing every value in the
        # matrix at the time of creation
        # If Matrix[m,n] does not have a node, then it is the default value
        self._head = MatrixNode(None)
        self._rows = m - 1
        self._cols = n - 1
        self._existing_rows = []
        self._existing_cols = []
        self._default = default
        # Check if the dimensions are valid
        if (self._rows < 0 or self._cols < 0):
            raise MatrixDimensionError("Invalid dimension input.")

    def get_num_cols(self):
        '''
        (self) -> int
        Return the number of columns this matrix contains.
        Note: 0-indexing does not apply when returning the amount.
        REQ: None
        '''
        return self._cols + 1

    def get_num_rows(self):
        '''
        (self) -> int
        Return the number of columns in this matrix.
        Note: 0-indexing does not apply when returning the amount.
        REQ: None
        '''
        return self._rows + 1

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        REQ: i > 0 and i <= number of rows in the matrix
        REQ: j > 0 and j <= number of columns in the matrix
        '''
        # First check if the coordinate is valid and within the matrix
        if (i > self._rows or i < 0 or j > self._cols or j < 0):
            raise MatrixIndexError("Dimension does not exist in the Matrix.")
        value = None
        # If the coordinate has a new row or a new col, then there does not
        # exist a node in the matrix for that value. Therefore, return the
        # default value
        if(i not in self._existing_rows or j not in self._existing_cols):
            # Set value to default
            value = self._default
        # Otherwise, we have to look to see if a node exists at the coordinate
        else:
            # Create a pointer to help navigate
            curr = self._head.get_down()
            # Check if the row the user entered already exists
            while(curr is not None and i > curr.get_contents()):
                curr = curr.get_down()
            # If we can't find the row index, then the node does
            # not exist, so return the default value
            if(curr is None or curr.get_contents() != i):
                value = self._default
            # If we find the row, check to see if there is a corresponding col
            else:
                curr = curr.get_right()
                while(curr is not None and j > curr.get_col()):
                    curr = curr.get_right()

                # If we find a corresponding column, then a node does exist
                # so return the value the node holds
                if(curr is not None and j == curr.get_col()):
                    value = curr.get_contents()
                # Otherwise, return the default value
                else:
                    value = self._default
        return value

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        REQ: i > 0 and i <= number of rows in the matrix
        REQ: j > 0 and j <= number of columns in the matrix
        REQ: new_val is some real number
        '''
        # First check if the coordinate is valid and within the matrix
        if (i > self._rows or i < 0 or j > self._cols or j < 0):
            raise MatrixIndexError("Dimension does not exist in the Matrix.")
        # Create a new Node to hold the new value and its row and col
        val_node = MatrixNode(new_val, i, j)

        # Consider the dimension the user entered:
        # If it is a new row and/or column to our current Matrix:
        # If it is the first value the user entered:
        if (self._head.get_right() is None and self._head.get_down() is None):
            # Create the index nodes, which act like an outer frame
            row_node = MatrixNode(i)
            col_node = MatrixNode(j)
            # Link the head of the Matrix to the index nodes
            self._head.set_right(col_node)
            self._head.set_down(row_node)
            # Link the index nodes to the new value node
            col_node.set_down(val_node)
            row_node.set_right(val_node)
            # Add the row number and column number to a list of existing nodes
            self._existing_rows.append(i)
            self._existing_cols.append(j)

        # If the user enters a value at a new row and column
        elif (i not in self._existing_rows and j not in self._existing_cols):
            # Create the new index nodes
            row_node = MatrixNode(i)
            col_node = MatrixNode(j)
            # Set a pointer to the first row index
            curr = self._head.get_down()
            # Make a temporary pointer to point at the previous node
            prev = self._head
            # Find a place for the new row index node
            if(i not in self._existing_rows):
                while(curr is not None and i > curr.get_contents()):
                    prev = curr
                    curr = curr.get_down()
                # Set the previous node's link to the new row node
                prev.set_down(row_node)
                # Set the new row node to the current node
                row_node.set_down(curr)
                # Now link the row node to the new value node
                row_node.set_right(val_node)
            # Find a place for the new column node
            # Repeat process similar to the one above
            curr = self._head.get_right()
            prev = self._head
            if(j not in self._existing_cols):
                while(curr is not None and j > curr.get_contents()):
                    prev = curr
                    curr = curr.get_right()
                prev.set_right(col_node)
                col_node.set_right(curr)
                col_node.set_down(val_node)
            # Add the column and row to the list of existing ones
            self._existing_rows.append(i)
            self._existing_cols.append(j)

        # If the user adds a value at a new row, but existing columm:
        elif (i not in self._existing_rows and j in self._existing_cols):
            # Create the new row node
            row_node = MatrixNode(i)
            # Add the row to existing rows list
            self._existing_rows.append(i)
            # Create temporary pointers to the index nodes
            prev = self._head
            curr = self._head.get_down()
            # Find the place to insert the new row node
            while(curr is not None and i > curr.get_contents()):
                prev = curr
                curr = curr.get_down()
            # Link the previous node to the new row node
            prev.set_down(row_node)
            # Link the row node to the current node
            row_node.set_down(curr)
            # Link the row node to its column value
            row_node.set_right(val_node)
            # Now find the column index node
            curr = self._head.get_right()
            while(curr.get_contents() != j):
                curr = curr.get_right()
            # Now that we've found the column, find the row to link the node
            prev = curr
            curr = curr.get_down()
            while(curr is not None and val_node.get_row() > curr.get_row()):
                prev = curr
                curr = curr.get_down()
            # Link the previous node to the value node, and value node to curr
            prev.set_down(val_node)
            val_node.set_down(curr)

        # If the user adds a value at an existing row but new column:
        elif (i in self._existing_rows and j not in self._existing_cols):
            # Create the new column index node
            col_node = MatrixNode(j)
            # Add the column to the list of existing columns
            self._existing_cols.append(j)
            # Create temporary pointers for index nodes
            prev = self._head
            curr = self._head.get_right()
            # Find where to insert the new column index node
            while(curr is not None and j > curr.get_contents()):
                prev = curr
                curr = curr.get_right()
            # Link previous node to new column index node
            prev.set_right(col_node)
            # Link col idx node to current node
            col_node.set_right(curr)
            # Link column index node to new value node
            col_node.set_down(val_node)
            # Now find the row index node
            curr = self._head.get_down()
            while(curr.get_contents() != i):
                curr = curr.get_down()
            # Find the node to link the row index chain to
            prev = curr
            curr = curr.get_right()
            while(curr is not None and val_node.get_col() > curr.get_col()):
                prev = curr
                curr = curr.get_right()
            # Link the nodes accordingly
            prev.set_right(val_node)
            val_node.set_right(curr)

        # Otherwise, the user enters a value at an existing row and col
        else:
            # Start by finding the row the input is at
            curr = self._head.get_down()
            while(curr.get_contents() != i):
                curr = curr.get_down()
            # Find the column the input is asking for
            prev = curr
            curr = curr.get_right()
            while(curr is not None and j > curr.get_col()):
                prev = curr
                curr = curr.get_right()
            # If a node already exists at that coordinate:
            if(curr is not None and j == curr.get_col()):
                # Replace the nodes value with the new value
                curr.set_contents(new_val)
            # Otherwise, set a new node to the matrix
            else:
                # Link the previous pointer to the new node
                prev.set_right(val_node)
                # Link the new nodes right pointer to the current node
                val_node.set_right(curr)
                # Now link the column's chain appropriately
                curr = self._head.get_right()
                while(curr.get_contents() != j):
                    curr = curr.get_right()
                # Now that we've found the column, find the row to link
                # the node
                prev = curr
                curr = curr.get_down()
                while(curr is not None and
                      val_node.get_row() > curr.get_row()):
                    prev = curr
                    curr = curr.get_down()
                # Link the previous node to the value node, and value node
                # to curr
                prev.set_down(val_node)
                val_node.set_down(curr)

    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix.
        REQ: row_num > 0 and row_num <= number of rows in the matrix
        '''
        # Check if the row to be returned exists in the matrix
        if (row_num < 0 or row_num > self._rows):
            raise MatrixIndexError("Given row does not exist in this matrix.")
        result = None
        # Find the row to be returned
        curr = self._head.get_down()
        while(curr is not None and row_num > curr.get_contents()):
            curr = curr.get_down()
        # If current is not pointing to the matching row index, then the
        # row hasn't been created, so the row contains all default values
        if(curr is None or curr.get_contents() != row_num):
            # Create a OneDimensionalMatrix to return
            # add 1 to the number of columns because of 0 indexing
            result = OneDimensionalMatrix(1, self._cols + 1, self._default)

        # Otherwise, the current row is linked to existing nodes
        else:
            result = OneDimensionalMatrix(1, self._cols + 1, self._default)
            # Find the nodes to link to the new row matrix
            curr = curr.get_right()
            while(curr is not None):
                # Copy over the values
                result.set_val(0, curr.get_col(), curr.get_contents())
                curr = curr.get_right()
        return result

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        REQ: row_num > 0 and row_num <= number of rows in the matrix
        REQ: new_row size is equal to amount of columns in the matrix
        '''
        # Check if the user entered a valid row number
        if(row_num < 0 or row_num > self.get_num_rows() - 1):
            raise MatrixIndexError("Given column not in the matrix.")
        # If the user entered a row matrix:
        if(new_row.get_num_rows() == 1 and new_row.get_num_cols() >= 1):
            # Make sure the matrix sizes are compatible
            if(new_row.get_size() != self.get_num_cols()):
                raise MatrixDimensionError("Matrix sizes not compatible.")
            # Loop through each coordinate in the row matrix
            for i in range(0, new_row.get_num_cols()):
                # Use the set_val method to help copy values from the
                # row matrix
                self.set_val(row_num, i, new_row.get_item(i))
        # Otherwise if a column matrix was entered
        else:
            # Make sure the matrix sizes are compatible
            if(new_row.get_size() != self.get_num_cols()):
                raise MatrixDimensionError("Matrix sizes not compatible.")
            # Loop through each item in the matrix
            for i in range(0, new_row.get_num_rows()):
                # Use set_val to add values to self one at a time
                self.set_val(row_num, i, new_row.get_item(i))

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix.
        REQ: col_num > 0 and col_num <= number of columns in the matrix
        '''
        # Check if the column exists in the matrix
        if (col_num > self._cols or col_num < 0):
            raise MatrixIndexError("Given column not in the matrix.")
        result = None
        # Find the column to be returned
        curr = self._head.get_right()
        while (curr is not None and col_num > curr.get_contents()):
            curr = curr.get_right()
        # If current is not pointing to an index node return a default value
        # one dimensional column matrix
        if(curr is None or curr.get_contents() != col_num):
            result = OneDimensionalMatrix(self._rows + 1, 1, self._default)
        # Otherwise the current index is linked to existing nodes
        else:
            result = OneDimensionalMatrix(self._rows + 1, 1, self._default)
            # Find the nodes to link to the new column matrix
            curr = curr.get_down()
            while(curr is not None):
                # Copy the values to the new column matrix
                result.set_val(curr.get_row(), 0, curr.get_contents())
                curr = curr.get_down()
        return result

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix to
        those of new_row
        REQ: col_num > 0 and col_num <= number of columns in the matrix
        REQ: new_col size is equal to amount of rows in the matrix
        '''
        # Check if the user entered a valid column number
        if(col_num < 0 or col_num > self.get_num_cols() - 1):
            raise MatrixIndexError("Given column not in the matrix.")
        # If the user entered a column matrix
        if(new_col.get_num_cols() == 1 and new_col.get_num_rows() >= 1):
            # Make sure the matrix sizes are compatible
            if(new_col.get_size() != self.get_num_rows()):
                raise MatrixDimensionError("Matrix sizes not compatible.")
            # Loop through each coordinate of the column matrix
            for i in range(0, new_col.get_num_rows()):
                # Use set_val to help add new values to self one at a time
                self.set_val(i, col_num, new_col.get_item(i))
        # Otherwise if a row matrix was entered:
        else:
            # Make sure the matrix sizes are compatible
            if(new_col.get_size() != self.get_num_cols()):
                raise MatrixDimensionError("Matrix sizes not compatible.")
            for i in range(0, new_col.get_num_cols()):
                # Use set_val to help add new values to self one at a time
                self.set_val(i, col_num, new_col.get_item(i))

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        REQ: i > 0 and i <= number of rows in the matrix
        REQ: j > 0 and j <= number of rows in the matrix
        '''
        # Make sure the given rows are in the matrix
        if(i < 0 or j < 0 or i > self.get_num_rows() - 1 or
           j > self.get_num_cols() - 1):
            raise MatrixIndexError("Given row(s) does not exist.")
        # First, get the rows to be swapped
        row_1 = self.get_row(i)
        row_2 = self.get_row(j)
        # Now switch the rows by setting them in each others place
        self.set_row(j, row_1)
        self.set_row(i, row_2)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        REQ: i > 0 and i <= number of columns in the matrix
        REQ: j > 0 and j <= number of columns in the matrix
        '''
        # Make sure the given columns are in the matrix
        if(i < 0 or j < 0 or i > self.get_num_cols() - 1 or
           j > self.get_num_cols() - 1):
            raise MatrixIndexError("Given column(s) does not exist.")
        # Get the two columns to be swapped
        col_1 = self.get_col(i)
        col_2 = self.get_col(j)
        # Switch the two columns
        self.set_col(j, col_1)
        self.set_col(i, col_2)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        REQ: add_value is some real number
        '''
        # Make sure the given value is a float
        if(type(add_value) is not int and type(add_value) is not float):
            raise MatrixInvalidOperationError("Given input is not a float.")
        # Add to the default value first
        self._default = self._default + add_value
        # Now add the value to each individual node
        curr_row = self._head.get_down()
        curr_col = self._head.get_right()
        # Go through each node in the matrix and add one by one
        while(curr_row is not None):
            # Create a nested loop to go through each column, moving down 1
            # row at a time after visiting every column
            curr_col = curr_row.get_right()
            while(curr_col is not None):
                # Add the value given to the nodes contents
                curr_col.set_contents(curr_col.get_contents() + add_value)
                # Move 1 column right
                curr_col = curr_col.get_right()
            # Move 1 row down
            curr_row = curr_row.get_down()

    def subtract_scalar(self, sub_value):
        '''Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        REQ: sub_value is some real number
        '''
        # Make sure the given value is a float
        if(type(sub_value) is not int and type(sub_value) is not float):
            raise MatrixInvalidOperationError("Given input is not a float.")
        # Subtract to the default value first
        self._default = self._default - sub_value
        # Now subtract the value to each individual node
        curr_row = self._head.get_down()
        curr_col = self._head.get_right()
        # Go through each node in the matrix and subtract one by one
        while(curr_row is not None):
            # Create a nested loop to go through each column, moving down 1
            # row at a time after visiting every column
            curr_col = curr_row.get_right()
            while(curr_col is not None):
                # subtract the value given to the nodes contents
                curr_col.set_contents(curr_col.get_contents() - sub_value)
                # Move 1 column right
                curr_col = curr_col.get_right()
            # Move 1 row down
            curr_row = curr_row.get_down()

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        REQ: mult_value is some real number
        '''
        # Make sure the given value is a float
        if(type(mult_value) is not int and type(mult_value) is not float):
            raise MatrixInvalidOperationError("Given input is not a float.")
        # Multiply default value of matrix by the value given
        self._default = self._default * mult_value
        # Now multiply by the value for each individual node
        curr_row = self._head.get_down()
        curr_col = self._head.get_right()
        # Go through each node in the matrix and multiply one by one
        while(curr_row is not None):
            # Create a nested loop to go through each column, moving down 1
            # row at a time after visiting every column
            curr_col = curr_row.get_right()
            while(curr_col is not None):
                # Multiply the value given to the nodes contents
                curr_col.set_contents(curr_col.get_contents() * mult_value)
                # Move 1 column right
                curr_col = curr_col.get_right()
            # Move 1 row down
            curr_row = curr_row.get_down()

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        REQ: adder_matrix has same dimensions as self
        '''
        # Make sure the matrix are the same dimensions
        if(self.get_num_rows() != adder_matrix.get_num_rows() or
           self.get_num_cols() is not adder_matrix.get_num_cols()):
            raise MatrixDimensionError("The matrices are not the same size.")
        # Create a new matrix representing the sum of the other two
        sum_matrix = Matrix(self.get_num_rows(), self.get_num_cols())
        # Go through every row in the matrices
        for i in range(0, self.get_num_rows()):
            # Go through every column in the matrices
            for j in range(0, self.get_num_cols()):
                # Add the contents of the matrices for the current coordinate
                sum_matrix.set_val(i, j, self.get_val(i, j) +
                                   adder_matrix.get_val(i, j))

        return sum_matrix

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        REQ: Matrices are MxN and NxW, that is, first matrix has an amount of
        columns equal to the second matrix's rows
        '''
        # Make sure the first matrix has an amount of columns equal to the
        # second matrix's rows (i.e MxN and NxW)
        if(self.get_num_cols() != mult_matrix.get_num_rows()):
            raise MatrixDimensionError("Unable to multiply given dimensions.")
        # Create a new matrix with the first matrix's amount of columns
        # and the second matrix's amount of rows
        product_matrix = Matrix(self.get_num_rows(),
                                mult_matrix.get_num_cols(), 0)
        # Loop to go through each row
        for i in range(0, self.get_num_rows()):
            # Loop to go through each column
            for j in range(0, mult_matrix.get_num_cols()):
                # Get the dot product of the first matrix's row and the
                # second matrix's column
                # Essentially go through each matrices' coordinates one
                # at a time and multiplying them respectively
                for k in range(0, self.get_num_cols()):
                    # Update the new matrix's values each iteration by
                    # adding to the current value
                    product_matrix.set_val(i, j, product_matrix.get_val(i, j) +
                                           (self.get_val(i, k) *
                                            mult_matrix.get_val(k, j)))
        return product_matrix


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''

    def __init__(self, m, n, default=0):
        '''
        (OneDimensionalMatrix, int, int, float) ->
        Create a OneDimensionalMatrix.
        REQ: m is an int > 0
        REQ: n is an int > 0
        REQ: default is some real number
        '''
        # REPRESENTATION INVARIANT

        # self._rows is the number of rows in the matrix using 0-indexing
        # self._cols is the number of rows in the matrix using 0-indexing
        # If self._rows = self._cols = m
        #    there are m + 1 rows and columns in the matrix
        # self._default is the default value for the matrix
        # self._existing_rows is a list containing existing row index
        # nodes in the matrix
        # self._existing_cols is a list containing existing column index
        # nodes in the matrix
        # If there are no manually set values in the matrix
        #    self._existing_rows is empty
        #    self._existing_cols is empty
        #    self._head is the sole node in the OneDimensionalMatrix
        self._head = MatrixNode(None)
        self._rows = m - 1
        self._cols = n - 1
        self._default = default
        self._existing_rows = []
        self._existing_cols = []
        # The row or column must be only a single dimension, by definition
        if(self._rows != 0 and self._cols != 0 or
           self._rows < 0 or self._cols < 0):
            raise MatrixDimensionError("Invalid 1D matrix dimension input.")

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        REQ: i is an integer within the number of rows/cols the matrix has
        '''
        result = None
        # Determine if it is a row matrix or column matrix
        # If it is a row matrix
        if(self._rows == 0 and self._cols >= 0):
            # Check if input column is valid
            if(i < 0 or i > self._cols):
                raise MatrixIndexError("The column is not in the matrix.")
            # Call helper method from parent class
            result = self.get_val(0, i)
        # Otherwise, if it's a column matrix
        else:
            # Check if input row is valid
            if (i < 0 or i > self._rows):
                raise MatrixIndexError("The row is not in the matrix")
            # Call parent method to help set the value
            result = self.get_val(i, 0)
        return result

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        REQ: i is an integer within amount of rows/cols the matrix has
        REQ: new_val is some real number
        '''
        # Check if it's a row matrix
        if(self._rows == 0 and self._cols >= 0):
            # Check if the coordinate is within the matrix
            if (i > self._cols or i < 0):
                raise MatrixIndexError("The column is not in the matrix.")
            # Call set method from parent class to set the value
            self.set_val(0, i, new_val)
        # Otherwise, it is a column matrix
        else:
            if (i > self._rows or i < 0):
                raise MatrixIndexError("The row is not in the matrix.")
            self.set_val(i, 0, new_val)

    def get_size(self):
        '''
        (OneDimensionalMatrix) -> int
        Return the size of the OneDimensionalMatrix.
        If it is a row matrix, return the amount of columns it contains; if
        it is a column matrix, return the amount of rows it contains.
        REQ: None
        '''
        result = None
        # If it is a row matrix
        if(self._rows == 0 and self._cols >= 0):
            # Set result to the number of columns in the matrix
            result = self._cols + 1
        # Otherwise if it is a column matrix
        else:
            # Set the result to the number of rows in the matrix
            result = self._rows + 1
        return result


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''

    def __init__(self, dimensions, default=0):
        '''
        (SquareMatrix, int, float) -> NoneType
        Create a SquareMatrix.
        REQ: dimensions is an int > 0
        REQ: default is some real number
        '''
        # REPRESENTAION INVARIANT

        # self._head is a single MatrixNode representing start of the matrix
        # self._default is a float representing the default value of this
        # matrix
        # self._existing_rows is a list containing all existing index
        # row node values
        # self._existing_cols is a list containing all existing index
        # column node values
        # If the matrix has no manually set values, then
        #     self._default is the value for all coordinates in the matrix
        #     self._existing_rows is empty
        #     self._existing_cols is empty
        #     self._head is the sole node in SquareMatrix
        # If there is a value at SquareMatrix[m,n] not equal to self._default
        #     self._existing_rows contains m
        #     self._existing_cols contains n
        # If self._rows = n, then
        #    self._cols = n and vice versa

        self._head = MatrixNode(None)
        self._default = default
        self._rows = dimensions - 1
        self._cols = dimensions - 1
        self._existing_rows = []
        self._existing_cols = []

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        REQ: None
        '''
        # Create a new temporary matrix to hold the transposed matrix
        transpose = SquareMatrix(self.get_num_rows())
        # Go through every row in self and set that current row to the
        # temporary matrix's corresponding column
        # self[Row 1] -> transpose[Column 1]
        for i in range(0, self.get_num_rows()):
            transpose.set_col(i, self.get_row(i))
        # Update this matrix so it becomes its own transpose by copying
        # the temporary matrix
        for i in range(0, self.get_num_cols()):
            self.set_col(i, transpose.get_col(i))

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        REQ: None
        '''
        # Create a new OneDimensionalMatrix to hold the diagonal values
        diag_matrix = OneDimensionalMatrix(1, self.get_num_rows())
        # Go through each diagonal coordinate in the matrix
        for i in range(0, self.get_num_rows()):
            # Add current value of the matrix to the new 1D Matrix
            diag_matrix.set_item(i, self.get_val(i, i))
        return diag_matrix

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        REQ: new_diagonal is a OneDimensionalMatrix
        REQ: the size of new_diagonal is equal to that of self's rows/cols
        '''
        # Make sure the matrix has an acceptable amount of values
        if(new_diagonal.get_size() != self.get_num_rows()):
            raise MatrixDimensionError("Matrix sizes not compatible.")
        # Loop through all the columns and set the values to the diagonal
        for i in range(0, new_diagonal.get_size()):
            Matrix.set_val(self, i, i, new_diagonal.get_item(i))


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''

    def set_val(self, i, j, new_val):
        '''
        (int, int, float) -> NoneType
        Set the value at position [i, j] in the SymmetricMatrix to new_val,
        and also set position [j, i] in the matrix to new_val.
        REQ: i >= 0 and i <= number of rows in the matrix
        REQ: j >= 0 and j <= number of columns in the matrix
        REQ: new_val is some real number
        '''
        # Make sure the given indexes are valid
        if(i < 0 or i > self.get_num_rows() - 1 or
           j < 0 or j > self.get_num_cols() - 1):
            raise MatrixIndexError("Dimension does not exist in the matrix.")
        # First set the value of the given coordinate with parent class method
        Matrix.set_val(self, i, j, new_val)
        # Now set the value at the matrix's mirror coordinate to be the same
        Matrix.set_val(self, j, i, new_val)

    def set_row(self, row_num, new_row):
        '''
        (SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        Will raise an error if the user attempts to set an row.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot change any rows.")

    def set_col(self, col_num, new_col):
        '''
        (SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        Will raise an error if the user attempts to set a column.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot change any values.")

    def swap_rows(self, i, j):
        '''
        (SymmetricMatrix, int, int) -> NoneType
        Raise an error if an attempt is made to swap two rows.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot swap any rows given type.")

    def swap_cols(self, i, j):
        '''
        (SymmetricMatrix, int, int) -> NoneType
        Raise an error if an attempt is made to swap two columns.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot swap any cols given type.")


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''

    def __init__(self, dimensions, default=0):
        '''
        (DiagonalMatrix, int, float) -> NoneType
        Create a diagonal matrix.
        REQ: dimensions is an int > 0
        REQ: default is some real number
        '''
        # REPRESENTATION INVARIANT

        # self._head is the first node in the DiagonalMatrix
        # (self._rows == self._cols) + 1 is the number of rows and columns
        # in the matrix (0 indexing used)
        # self._existing_rows is a list containing the existing row index
        # nodes in the matrix
        # self._existing_cols is a list containing the existing col index
        # nodes in the matrix
        # self._default is 0, and is the value for all non-diagonal indexes
        # self._diag_default is the default for all diagonal indexes
        # If there are no manually set values in the DiagonalMatrix
        #    self._head is the sole node in the matrix
        #    self._existing_rows is empty
        #    self._existing_cols is empty
        #    DiagonalMatrix[i,j] for all i != j is 0
        #    DiagonalMatrix[k,k] is self._diag_default

        # Call the parent class init to intialize some variables
        # Enter 0 as default since non-diagonal entries will be 0
        super(DiagonalMatrix, self).__init__(dimensions, 0)
        self._diag_default = default
        # If the user enters a default value which is not 0, change the
        # main diagonal of the matrix to that default value
        if(self._diag_default != 0):
            diag = OneDimensionalMatrix(1, dimensions, default)
            SquareMatrix.set_diagonal(self, diag)

    def set_val(self, i, j, new_val):
        '''
        (DiagonalMatrix, int, int, float) -> NoneType
        Set value at position [i,j] in the matrix to new_val
        REQ: i is a number within the first and last row in the matrix
        REQ: j is a number wihin the first and last column in the matrix
        '''
        # Check if an attempt was made to set a non-diagonal value
        if(i != j):
            raise MatrixInvalidOperationError("Non-diagonal values must be 0.")
        # If not, set the value at the new position
        Matrix.set_val(self, i, j, new_val)

    def set_row(self, row_num, new_row):
        '''
        (DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        Will raise an error if the user attempts to set an row.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot change any rows.")

    def set_col(self, col_num, new_col):
        '''
        (DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        Will raise an error if the user attempts to set a column.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot change any columns.")

    def swap_rows(self, i, j):
        '''
        (DiagonalMatrix, int, int) -> NoneType
        Raise an error if an attempt is made to swap two rows.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot swap any rows given type.")

    def swap_cols(self, i, j):
        '''
        (DiagonalMatrix, int, int) -> NoneType
        Raise an error if an attempt is made to swap two columns.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot swap any cols given type.")


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''

    def __init__(self, dimensions):
        '''
        Create an IdentityMatrix.
        REQ: dimensions is an int > 0
        '''
        # REPRESENTATION INVARIANT

        # self._head is the first node in the matrix
        # (self._rows == self._cols) + 1 is the amount of rows and columns
        # self._diag_default will always be 1
        # If I_M is an IdentityMatrx
        #    I_M has m rows and m columns
        #    I_M[i,j] for all i == j is 1
        #    I_M[i,j] for all i != j is 0

        # Call the DiagonalMatrix parent classes init to intialize
        # Set default value as 1 for the main diagonal
        super(IdentityMatrix, self).__init__(dimensions, 1)

    def set_val(self, i, j, new_val):
        '''
        (IdentityMatrix, int, int, float) -> NoneType
        Will raise an error if the user attempts to set any value.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot change any values.")

    def set_diagonal(self, new_diag):
        '''
        (IdentityMatrix, OneDimensionalMatrix) -> NoneType
        Will raise an error if the user attempts to set an diagonal.
        REQ: None
        '''
        raise MatrixInvalidOperationError("Cannot change any values")
