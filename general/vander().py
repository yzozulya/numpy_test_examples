from numpy import *

x = array([1, 2, 3, 5])
N = 3
vander(x, N)  # Vandermonde matrix of the vector x
column_stack([x ** (N - 1 - i) for i in range(N)])  # to understand what a Vandermonde matrix contains
