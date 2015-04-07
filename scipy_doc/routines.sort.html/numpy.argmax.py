import numpy as np

a = np.arange(6).reshape(2, 3)
a
np.argmax(a)
np.argmax(a, axis=0)
np.argmax(a, axis=1)
b = np.arange(6)
b[1] = 5
b
np.argmax(b)  # Only the first occurrence is returned.
