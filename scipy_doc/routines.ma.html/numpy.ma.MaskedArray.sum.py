import numpy as np

x = np.ma.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], mask=[0] + [1, 0] * 4)
print
x
print
x.sum()
print
x.sum(axis=1)
print
x.sum(axis=0)
print
type(x.sum(axis=0, dtype=np.int64)[0])
