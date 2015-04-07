from numpy import *

a = array([10, 20, 30])
minindex = a.argmin()
a[minindex]
a = array([[10, 50, 30], [60, 20, 40]])
minindex = a.argmin()
minindex
a.ravel()[minindex]
a.argmin(axis=0)  # for each column: the row index of the minimum value
a.argmin(axis=1)  # for each row: the column index of the minimum value
argmin(a)  # also exists, slower, default is axis=-1
