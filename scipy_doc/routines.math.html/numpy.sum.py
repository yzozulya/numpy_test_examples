import numpy as np

np.sum([0.5, 1.5])
np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
np.sum([[0, 1], [0, 5]])
np.sum([[0, 1], [0, 5]], axis=0)
np.sum([[0, 1], [0, 5]], axis=1)
np.ones(128, dtype=np.int8).sum(dtype=np.int8)
