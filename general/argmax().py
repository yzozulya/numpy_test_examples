from numpy import *

a = array([10, 20, 30])
maxindex = a.argmax()
a[maxindex]
a = array([[10, 50, 30], [60, 20, 40]])
maxindex = a.argmax()
maxindex
a.ravel()[maxindex]
a.argmax(axis=0)  # for each column: the row index of the maximum value
a.argmax(axis=1)  # for each row: the column index of the maximum value
argmax(a)  # also exists, slower, default is axis=-1
