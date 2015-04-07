from numpy import *

a = array([10, 20, 30, 40])
a.put([60, 70, 80], [0, 3, 2])  # first values, then indices
a
a[[0, 3, 2]] = [60, 70, 80]  # same effect
a.put([40, 50], [0, 3, 2, 1])  # if value array is too short, it is repeated
a
put(a, [0, 3], [90])  # also exists, but here FIRST indices, THEN values
a
