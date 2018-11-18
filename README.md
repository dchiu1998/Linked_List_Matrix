# Linked_List_Matrix
A matrix project designed using linked lists. Includes matrix operations to manipulated matrix objects and exceptions.

A Matrix object is implemented in such that only a single node is declared at its creation
(i.e. a matrix with dimensions 5000x5000 will only have one single node, its head, at time of declaration). There 
is a default value which is the value for every element of the matrix which does not have any value set yet. 
This allows us to save space when working with extemely large matrices.

For example, consider the following example:

![alt text](https://github.com/dchiu1998/Linked_List_Matrix/blob/master/N_Matrix_image2.png)

Here, a 3000x3000 matrix is declared, with default value 1. This means every element of the 3000x3000
matrix has a value of 1 at this time. But we then set the value of the element at Z(1222,2111) to 17.
We can also perform various operations on matrix Z, such as subtracting every element by a scalar value of 1000.

Many other operations are also available, such as setting values of entire rows:

![alt text](https://github.com/dchiu1998/Linked_List_Matrix/blob/master/N_Matrix_image3.png)

First a matrix 3x3 matrix, A, was declared with default value 0. Then, a row vector B was declared with default
value 7. The second row of A was set to take the values of row vector B (0 indexing is used when setting inputs).

When an operation is attempted under invalid cirumstances, a specific exception will be raised:

![alt text](https://github.com/dchiu1998/Linked_List_Matrix/blob/master/N_Matrix_image4.png)

An identity matrix with dimensions 5x5 was declared, and attempted to be multiplied with by A. However,
their dimensions do not allow for them to be multiplied.
