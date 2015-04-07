from numpy import *

add.reduce(array([1., 2., 3., 4.]))  # computes ((((1.)+2.)+3.)+4.)
multiply.reduce(array([1., 2., 3., 4.]))  # works also with other operands. Computes ((((1.)*2.)*3.)*4.)
add.reduce(array([[1, 2, 3], [4, 5, 6]]), axis=0)  # reduce every column separately
add.reduce(array([[1, 2, 3], [4, 5, 6]]), axis=1)  # reduce every row separately
