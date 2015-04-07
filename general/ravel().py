from numpy import *

a = array([[1, 2], [3, 4]])
a.ravel()  # 1-d version of a
b = a[:, 0].ravel()  # a[:,0] does not occupy a single memory segment, thus b is a copy, not a reference
b
c = a[0, :].ravel()  # a[0,:] occupies a single memory segment, thus c is a reference, not a copy
c
b[0] = -1
c[1] = -2
a
ravel(a)  # also exists
