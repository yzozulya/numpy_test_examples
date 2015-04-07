from numpy import *

a = array([1, 2])
b = array([[3, 4], [5, 6]])
vstack((a, b, a))  # only the first dimension of the arrays is allowed to be different
