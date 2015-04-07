from numpy import *

a = arange(24).reshape(2, 3, 4)  # a has 3 axes: 0,1 and 2
a
apply_over_axes(sum, a, [0, 2])  # sum over all axes except axis=1, result has same shape as original
