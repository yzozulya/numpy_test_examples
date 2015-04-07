import numpy as np

np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
np.histogram(np.arange(4), bins=np.arange(5), density=True)
np.histogram([[1, 2, 1], [1, 0, 1]], bins=[0, 1, 2, 3])
a = np.arange(5)
hist, bin_edges = np.histogram(a, density=True)
hist
hist.sum()
np.sum(hist * np.diff(bin_edges))
