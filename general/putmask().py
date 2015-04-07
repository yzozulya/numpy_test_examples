from numpy import *

a = array([10, 20, 30, 40])
mask = array([True, False, True, True])  # size mask = size a
a.putmask([60, 70, 80, 90], mask)  # first values, then the mask
a
a = array([10, 20, 30, 40])
a[mask]  # reference
a[mask] = array([60, 70, 80, 90])  # NOT exactly the same as putmask
a
a.putmask([10, 90], mask)  # if value array is too short, it is repeated
a
putmask(a, mask, [60, 70, 80, 90])  # also exists, but here FIRST mask, THEN values
