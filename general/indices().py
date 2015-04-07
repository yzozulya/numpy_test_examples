from numpy import *

indices((2, 3))
a = array([[0, 1, 2, 3, 4],
           [10, 11, 12, 13, 14],
           [20, 21, 22, 23, 24],
           [30, 31, 32, 33, 34]])
i, j = indices((2, 3))
a[i, j]
