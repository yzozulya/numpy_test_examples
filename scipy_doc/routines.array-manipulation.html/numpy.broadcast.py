import numpy as np

x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
b = np.broadcast(x, y)
out = np.empty(b.shape)
out.flat = [u + v for (u, v) in b]
out
x + y
