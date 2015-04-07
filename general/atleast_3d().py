from numpy import *

a = 1  # 0-d array
b = array([2, 3])  # 1-d array
c = array([[4, 5], [6, 7]])  # 2-d array
d = arange(8).reshape(2, 2, 2)  # 3-d array
d
atleast_3d(a, b, c, d)  # all output arrays have dim >= 3
