from numpy import *

a = array([1, 2, 3])  # cumulative sum = intermediate summing results & total sum
a.cumsum()
cumsum(a)  # also exists
a = array([[1, 2, 3], [4, 5, 6]])
a.cumsum(dtype=float)  # specifies type of output value(s)
a.cumsum(axis=0)  # sum over rows for each of the 3 columns
a.cumsum(axis=1)  # sum over columns for each of the 2 rows
