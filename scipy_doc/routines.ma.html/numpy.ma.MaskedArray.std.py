import numpy as np

a = np.array([[1, 2], [3, 4]])
np.std(a)
np.std(a, axis=0)
np.std(a, axis=1)
a = np.zeros((2, 512 * 512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
np.std(a)
np.std(a, dtype=np.float64)
