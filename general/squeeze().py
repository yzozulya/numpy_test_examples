from numpy import *

a = arange(6)
a = a.reshape(1, 2, 1, 1, 3, 1)
a
a.squeeze()  # result has shape 2x3, all dimensions with length 1 are removed
squeeze(a)  # also exists
