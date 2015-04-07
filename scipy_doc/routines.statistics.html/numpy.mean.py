import numpy as np

a = np.array([[1, 2], [3, 4]])
np.mean(a)
np.mean(a, axis=0)
np.mean(a, axis=1)
a = np.zeros((2, 512 * 512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
np.mean(a)
np.mean(a, dtype=np.float64)
