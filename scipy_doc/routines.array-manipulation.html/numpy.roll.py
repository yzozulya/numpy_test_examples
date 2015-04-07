import numpy as np

x = np.arange(10)
np.roll(x, 2)
x2 = np.reshape(x, (2, 5))
x2
np.roll(x2, 1)
np.roll(x2, 1, axis=0)
np.roll(x2, 1, axis=1)
