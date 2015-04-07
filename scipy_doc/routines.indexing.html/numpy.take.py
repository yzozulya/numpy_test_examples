import numpy as np

a = [4, 3, 5, 7, 6, 8]
indices = [0, 1, 4]
np.take(a, indices)
a = np.array(a)
a[indices]
np.take(a, [[0, 1], [2, 3]])
