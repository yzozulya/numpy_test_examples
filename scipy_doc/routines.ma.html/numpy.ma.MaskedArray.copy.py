import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]], order='F')
y = x.copy()
x.fill(0)
x
y
y.flags['C_CONTIGUOUS']
