from numpy import *

a = array([[1, 2], [3, 4], [5, 6], [7, 8]])
vsplit(a, 2)  # split, row-wise, in 2 equal parts
vsplit(a, [1, 2])  # split, row-wise, before row 1 and before row 2
