import numpy as np

x = np.array([1, 2])
x.shape
y = np.expand_dims(x, axis=0)
y
y.shape
y = np.expand_dims(x, axis=1)  # Equivalent to x[:,newaxis]
y
y.shape
np.newaxis is None
