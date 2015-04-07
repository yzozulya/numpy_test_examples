from numpy import *

a = array([1, 2, 3])
a.cumprod()  # total product 1*2*3 = 6, and intermediate results 1, 1*2
cumprod(a)  # also exists
a = array([[1, 2, 3], [4, 5, 6]])
a.cumprod(dtype=float)  # specify type of output
a.cumprod(axis=0)  # for each of the 3 columns: product and intermediate results
a.cumprod(axis=1)  # for each of the two rows: product and intermediate results
