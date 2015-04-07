from numpy import *

a = array([1., 2, 7])
a.std()  # normalized by N (not N-1)
a = array([[1., 2, 7], [4, 9, 6]])
a.std()
a.std(axis=0)  # standard deviation of each of the 3 columns
a.std(axis=1)  # standard deviation of each of the 2 columns
