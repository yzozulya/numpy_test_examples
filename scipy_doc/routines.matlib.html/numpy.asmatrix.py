import numpy as np

x = np.array([[1, 2], [3, 4]])
m = np.asmatrix(x)
x[0, 0] = 5
m
