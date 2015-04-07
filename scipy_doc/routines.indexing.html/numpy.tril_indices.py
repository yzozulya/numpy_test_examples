import numpy as np

il1 = np.tril_indices(4)
il2 = np.tril_indices(4, 2)
a = np.arange(16).reshape(4, 4)
a
a[il1]
a[il1] = -1
a
a[il2] = -10
a
