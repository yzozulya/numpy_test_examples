from numpy import *

a = array([10, 20, 30, 40])
a.take([0, 0, 3])  # [0,0,3] is a set of indices
a[[0, 0, 3]]  # the same effect
a.take([[0, 1], [0, 1]])  # shape of return array depends on shape of indices array
a = array([[10, 20, 30], [40, 50, 60]])
a.take([0, 2], axis=1)
take(a, [0, 2], axis=1)  # also exists
