from numpy import *

a = array([10, 20])
tile(a, (3, 2))  # concatenate 3x2 copies of a together
tile(42.0, (3, 2))  # works for scalars, too
tile([[1, 2], [4, 8]], (2, 3))  # works for 2-d arrays and list literals, too
