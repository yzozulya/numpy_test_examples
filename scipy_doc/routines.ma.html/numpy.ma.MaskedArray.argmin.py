import numpy as np

x = np.ma.array(np.arange(4), mask=[1, 1, 0, 0])
x.shape = (2, 2)
print
x
print
x.argmin(axis=0, fill_value=-1)
print
x.argmin(axis=0, fill_value=9)
