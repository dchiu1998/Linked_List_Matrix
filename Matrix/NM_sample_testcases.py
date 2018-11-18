import unittest
import Node_Matrix_design


class TestSetValue(unittest.TestCase):
    ''' Test the set_value method. '''
    
    def test1_change_single_value(self):
        new_matrix = Matrix(1,3)
        result = new_matrix.set_value(1, 1, 'a')
        expected = ['a', '', '']
        self.assertEqual(result, expected, "Should insert value at (1,1).")
        
    def test2_enter_blank_value(self):
        new_matrix = Matrix(3,1)
        result = new_matrix.set_value(1, 1)
        expected = ['', '', '']
        self.assertEqual(result, expected, "Should enter NoneType at (1,1).")
        
    def test3_set_value_at_invalid_dimension(self):
        with self.assertRaise(InvalidDimensionError):
            new_matrix = Matrix(3,3)
            new_matrix.set_value(5, 3, 'A')
    
    def test4_set_an_invalid_type(self):
        with self.assertRaise(ValueTypeError):
            new_matrix = Matrix (3,3)
            new_matrix.set_value(1,2, "covfefe")
    
    def test5_set_value_of_a_symmetric_matrix(self):
        matrix = Matrix(2,2)
        matrix = [[0,0],[0,0]]
        result = matrix.set_value(1,2,5)
        expected = [[0,5],[5,0]]
        self.assertEqual(result, expected, "The mirror value should change too.")
    
    def test6_set_value_of_one_dimensional_matrix(self):
        matrix = OneDimMatrix(False, 3)
        matrix = [0,0,0]
        result = matrix.set_value(2,5)
        expected = [0,5,0]
        self.assertEqual(result, expected, "The second index should change to 5")
    
    def test7_set_value_on_1D_matrix_at_non_existing_index(self):
        with assertRaise(InvalidDimensionError):
            matrix = OneDimMatrix(True, 5)
            matrix.set_value(6,0)


class TestGetValue(unittest.TestCase):
    
    def test1_get_single_value(self):
        matrix = Matrix(1,4)
        matrix = [1, 2, 3, 4]
        result = matrix.get_value(1,2)
        expected = 2
        self.assertEqual(result, expected, "Should have returned a 2.")
        
    def test2_get_value_at_invalid_dimension(self):
        with self.assertRaise(InvalidDimensionError):
            new_matrix = Matrix(4,4)
            new_matrix.get_value(4,5)

    def test3_get_value_at_invalid_dimeonsion_1D_matrix(self):
        with self.assertRaise(InvalidDimensionError):
            matrix = OneDimMatrix(False, 3)
            matrix.get_value(5)


class TestSwapRow(unittest.TestCase):
    
    def test1_swap_rows(self):
        new_matrix = Matrix(3,3)
        new_matrix = [[1,2,3], ['a','b','c'], [4,5,6]]
        result = new_matrix.swap_row(1,3)
        expected = [[4,5,6], ['a','b','c'], [1,2,3]]
        self.assertEqual(result, expected, "Should have swapped rows 1 and 3.")
        
    def test2_swap_non_existing_row(self):
        with self.assertRaise(InvalidDimensionError):
            new_matrix = Matrix(3,3)
            new_matrix.swap_row(1,5)
            
    def test3_swap_row_with_same_row(self):
        new_matrix = Matrix(2,2)
        new_matrix = [[1,2], [3,4]]
        result = new_matrix.swap_row(2,2)
        expected = [[1,2], [3,4]]
        self.assertEqual(result, expected, "The rows shouldn't have changed.")
    

class TestSwapColumn(unittest.TestCase):
    
    def test1_swap_non_existing_column(self):
        with self.assertRaise(InvalidDimensionError):
            new_matrix = Matrix(5,5)
            new_matrix.swap_col(1,7)
            
    def test2_swap_same_col(self):
        new_matrix = Matrix(2,2)
        new_matrix = [['a','b'], ['c','d']]
        result = new_matrix.swap(1,1)
        expected = [['a','b'], ['c','d']]
        self.assertEqual(result, expected, "Columns shouldn't have changed.")
        

class TestAdd(unittest.TestCase):
    
    def test1_add_2_matrices(self):
        matrix1 = [1,1,2]
        matrix2 = [2,2,1]
        result = matrix1.add(matrix2)
        expected = [3,3,3]
        self.assertEqual(result, expected, "The result should be [3,3,3].")
        
    def test2_add_matrices_with_different_dimensions(self):
        with self.assertRaise(InvalidMatrixError):
            matrix1 = [5]
            matrix2 = [1,1,4,5]
            matrix1.add(matrix2)
    
    def test3_add_string_matrix_to_integer_matrix(self):
        with self.assertRaise(MathError):
            matrix1 = [1,2,3]
            matrix2 = ['a','b','c']
            matrix1.add(matrix2)
    
    def test4_add_two_string_matrices(self):
        matrix1 = ['tk', 'computer']
        matrix2 = ['ko', 'science']
        result = matrix1.add(matrix2)
        expected = ['tkko', 'computerscience']
        self.assertEqual(result, expected, "Strings should habe combined.")


class TestSubtract(unittest.TestCase):
    
    def test1_subtract_2_matrices(self):
        matrix1 = [0,5,2]
        matrix2 = [1,5,0]
        result = matrix1.subtract(matrix2)
        expected = [-1,0,2]
        self.assertEqual(result, expected, "The result should be [-1,0,2].")
        
    def test2_subtract_matrices_with_different_dimensions(self):
        with self.assertRaise(InvalidMatrixError):
            matrix1 = [5,2,-3]
            matrix2 = [1,4,-3,0,0,10,15]
            matrix1.subtract(matrix2)
    
    def test3_subtract_string_matrix_with_integer_matrix(self):
        with self.assertRaise(MathError):
            matrix1 = ['d','e','f']
            matrix2 = [7,8,9]
            matrix1.subtract(matrix2)
            

class TestMultiply(unittest.TestCase):
    
    def test1_multiply_2_matrices(self):
        matrix1 = Matrix(1,3)
        matrix2 = Matrix(3,1)
        result = matrix1.multiply(matrix2)
        expected = ['']
        self.assertEqual(result, expected, "Matrices' dimensions must be compatible.")
    
    def test2_multiply_incompatible_matrices(self):
        with self.assertRaise(InvalidMatrixError):
            matrix1 = Matrix(2,5)
            matrix2 = Matrix(7,2)
            matrix1.multiply(matrix2)
            
    def test3_multiply_string_with_integer(self):
        with self.assertRaise(MathError):
            matrix1 = ['Banana']
            matrix2 = [42]
            matrix1.multiply(matrix2)
            

class TestTranspose(unittest.TestCase):
    
    def test1_transpose_single_dimension_matrix(self):
        new_matrix = Matrix(1,1)
        new_matrix = [5]
        new_matrix.transpose()
        expected_matrix = [5]
        self.assertEqual(new_matrix, expected_matrix, "Matrix should be the same.")
        
    def test2_transpose_a_diagonal_matrix(self):
        # Create a 3x3 identity matrix
        new_matrix = IdentityMatrix(3)
        # Store it in another variable, then compare after transposing
        temp = new_matrix
        new_matrix.transpose()
        self.assertEqual(new_matrix, temp, "Matrix should not have changed.")


class TestGetDeterminant(unittest.TestCase):
    
    def test1_get_determinant_of_2x2_matrix(self):
        matrix = Matrix(2,2)
        matrix = [[1,3], [2,1]]
        result = matrix.get_determinant()
        expected = -5
        self.assertEqual(result, expected, "Only 2x2 matrices will work.")
    
    def test2_get_determinant_of_invalid_matrix(self):
        with self.assertRaise(InvalidMatrixError):
            matrix = Matrix(3,2)
            matrix.get_determinant()
    
    def test3_get_determinant_of_matrix_with_string(self):
        with assertRaise(MathError):
            matrix = Matrix(2,2)
            matrix = [['a','b'], [1,2]]
            matrix.get_determinant()
            

class TestSetDiag(unittest.TestCase):
    
    def test1_set_diagonal_of_a_matrix(self):
        new_matrix = Matrix(3,3)
        new_matrix = [[1,5,3], [0,2,7], [3,2,2]]
        result = new_matrix.set_diag(6)
        expected = [[6,5,3], [0,6,7], [3,2,6]]
        self.assertEqual(result, expected, "The main diagonal should be all 6.")
    
    def test2_set_diagonal_of_an_integer_matrix_with_string(self):
        with assertRaise(ValueTypeError):
            new_matrix = Matrix(3,3)
            new_matrix.set_diag("ABC")
    

class TestGetDiag(unittest.TestCase):
    
    def test1_get_diagonal_value_of_an_identity_matrix(self):
        matrix = IdentityMatrix(4)
        result = matrix.get_diag()
        expected = 1
        self.assertEqual(result, expected, "Diagonal of an identity is 1.")
