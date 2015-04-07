from numpy import *

a = array([10, 20, 30])
a.min()
a = array([[10, 50, 30], [60, 20, 40]])
a.min()
a.min(axis=0)  # for each of the columns, find the minimum
a.min(axis=1)  # for each of the rows, find the minimum
min(a)  # also exists, but is slower
