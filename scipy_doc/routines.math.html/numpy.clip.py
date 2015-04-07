import numpy as np

a = np.arange(10)
np.clip(a, 1, 8)
a
np.clip(a, 3, 6, out=a)
a = np.arange(10)
a
np.clip(a, [3, 4, 1, 1, 1, 4, 4, 4, 4, 4], 8)
