import numpy as np

x = np.ma.array([[1, 2], [3, 4]], mask=[1, 0, 0, 1])
print
x
x = x.reshape((4, 1))
print
x
