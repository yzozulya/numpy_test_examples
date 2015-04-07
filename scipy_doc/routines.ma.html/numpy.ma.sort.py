import numpy as np

a = ma.array([1, 2, 5, 4, 3], mask=[0, 1, 0, 1, 0])
# Default
a.sort()
print
a
a = ma.array([1, 2, 5, 4, 3], mask=[0, 1, 0, 1, 0])
# Put missing values in the front
a.sort(endwith=False)
print
a
a = ma.array([1, 2, 5, 4, 3], mask=[0, 1, 0, 1, 0])
# fill_value takes over endwith
a.sort(endwith=False, fill_value=3)
print
a
