from numpy import *

a = array([1, 2, 3])
a.sum()
sum(a)  # also exists
a = array([[1, 2, 3], [4, 5, 6]])
a.sum()
a.sum(dtype=float)  # specify type of output
a.sum(axis=0)  # sum over rows for each of the 3 columns
a.sum(axis=1)  # sum over columns for each of the 2 rows
