from numpy import *

a = array([1, 0, 5])
b = array([3, 2, 4])
maximum(a, b)  # element-by-element comparison
max(a.tolist(), b.tolist())  # standard Python function does not give the same!
