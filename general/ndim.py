from numpy import *

a = arange(12).reshape(3, 4)
a
a.ndim  # a has 2 axes
a.shape = (2, 2, 3)
a.ndim  # now a has 3 axes
len(a.shape)  # same as ndim
