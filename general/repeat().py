from numpy import *

repeat(7., 4)
a = array([10, 20])
a.repeat([3, 2])
repeat(a, [3, 2])  # also exists
a = array([[10, 20], [30, 40]])
a.repeat([3, 2, 1, 1])
a.repeat([3, 2], axis=0)
a.repeat([3, 2], axis=1)
