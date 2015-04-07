import numpy as np
# np.reshape()
x = np.arange(16.0).reshape(4, 4)
x
np.hsplit(x, 2)
np.hsplit(x, np.array([3, 6]))
y = np.arange(8.0)
print(y)
x = y.reshape(2, 2, 2)
print(x)
np.hsplit(x, 2)
