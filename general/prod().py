from numpy import *

a = array([1, 2, 3])
a.prod()  # 1 * 2 * 3 = 6
prod(a)  # also exists
a = array([[1, 2, 3], [4, 5, 6]])
a.prod(dtype=float)  # specify type of output
a.prod(axis=0)  # for each of the 3 columns: product
a.prod(axis=1)  # for each of the two rows: product
