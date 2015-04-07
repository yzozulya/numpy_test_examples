from numpy import *

mat('1 3 4; 5 6 9')  # matrices are always 2-dimensional
a = array([[1, 2], [3, 4]])
m = mat(a)  # convert 2-d array to matrix
m
a[0]  # result is 1-dimensional
m[0]  # result is 2-dimensional
a.ravel()  # result is 1-dimensional
m.ravel()  # result is 2-dimensional
a * a  # element-by-element multiplication
m * m  # (algebraic) matrix multiplication
a ** 3  # element-wise power
m ** 3  # matrix multiplication m*m*m
m.T  # transpose of the matrix
m.H  # conjugate transpose (differs from .T for complex matrices)
m.I  # inverse matrix
