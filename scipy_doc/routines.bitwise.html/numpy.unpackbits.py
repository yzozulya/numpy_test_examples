import numpy as np

a = np.array([[2], [7], [23]], dtype=np.uint8)
a
b = np.unpackbits(a, axis=1)
b
