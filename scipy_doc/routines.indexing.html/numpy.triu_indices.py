import numpy as np

iu1 = np.triu_indices(4)
iu2 = np.triu_indices(4, 2)
a = np.arange(16).reshape(4, 4)
a
a[iu1]
a[iu1] = -1
a
a[iu2] = -10
a
