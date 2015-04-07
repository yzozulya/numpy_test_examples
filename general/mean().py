from numpy import *

a = array([1, 2, 7])
a.mean()
a = array([[1, 2, 7], [4, 9, 6]])
a.mean()
a.mean(axis=0)  # the mean of each of the 3 columns
a.mean(axis=1)  # the mean of each of the 2 rows
