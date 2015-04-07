from numpy import *

a = array([1, 2, 7])
a.var()  # normalised with N (not N-1)
a = array([[1, 2, 7], [4, 9, 6]])
a.var()
a.var(axis=0)  # the variance of each of the 3 columns
a.var(axis=1)  # the variance of each of the 2 rows
