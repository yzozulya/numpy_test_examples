from numpy import *

a = arange(9).reshape(3, 3)
print a
indices = ix_([0, 1, 2], [1, 2, 0])  # trick to be used with array broadcasting
print indices
print a[indices]
# The latter array is the cross-product:
# [[ a[0,1] a[0,2] a[0,0]]
# [ a[1,1] a[1,2] a[1,0]]
# [ a[2,1] a[2,2] a[2,0]]]
