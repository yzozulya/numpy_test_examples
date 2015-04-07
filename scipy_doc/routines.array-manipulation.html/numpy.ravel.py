import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print
np.ravel(x)
print
x.reshape(-1)
print
np.ravel(x, order='F')
print
np.ravel(x.T)
print
np.ravel(x.T, order='A')
a = np.arange(3)[::-1]
a
a.ravel(order='C')
a.ravel(order='K')
a = np.arange(12).reshape(2, 3, 2).swapaxes(1, 2)
a
a.ravel(order='C')
a.ravel(order='K')
