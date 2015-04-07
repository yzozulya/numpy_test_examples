import numpy as np

iu = np.mask_indices(3, np.triu)
a = np.arange(9).reshape(3, 3)
a
a[iu]
iu1 = np.mask_indices(3, np.triu, 1)
a[iu1]
