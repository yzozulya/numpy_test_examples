from numpy import *

a = array([[1, 2, 3, 4], [5, 6, 7, 8]])
split(a, 2, axis=0)  # split a in 2 parts. row-wise
split(a, 4, axis=1)  # split a in 4 parts, column-wise
split(a, 3, axis=1)  # impossible to split in 3 equal parts -> error (SEE: array_split)
split(a, [2, 3], axis=1)  # make a split before the 2nd and the 3rd column
