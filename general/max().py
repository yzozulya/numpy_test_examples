from numpy import *

a = array([10, 20, 30])
a.max()
a = array([[10, 50, 30], [60, 20, 40]])
a.max()
a.max(axis=0)  # for each of the columns, find the maximum
a.max(axis=1)  # for each of the rows, find the maximum
max(a)  # also exists, but is slower
