from numpy import *

a = array([[1, 2, 3, 4], [5, 6, 7, 8]])
hsplit(a, 2)  # split, column-wise, in 2 equal parts
hsplit(a, [1, 2])  # split before column 1 and before column 2
