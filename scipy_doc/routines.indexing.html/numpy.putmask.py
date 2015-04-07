import numpy as np

x = np.arange(6).reshape(2, 3)
np.putmask(x, x > 2, x ** 2)
x
x = np.arange(5)
np.putmask(x, x > 1, [-33, -44])
x
