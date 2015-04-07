import numpy as np
from numpy.ma import arange

x = np.ma.array(arange(4), mask=[1, 1, 0, 0])
x.shape = (2, 2)
print
x
print
x.argmin(axis=0, fill_value=-1)
print
x.argmin(axis=0, fill_value=9)
