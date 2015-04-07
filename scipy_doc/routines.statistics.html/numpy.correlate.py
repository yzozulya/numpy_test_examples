import numpy as np

np.correlate([1, 2, 3], [0, 1, 0.5])
np.correlate([1, 2, 3], [0, 1, 0.5], "same")
np.correlate([1, 2, 3], [0, 1, 0.5], "full")
np.correlate([1 + 1j, 2, 3 - 1j], [0, 1, 0.5j], 'full')
np.correlate([0, 1, 0.5j], [1 + 1j, 2, 3 - 1j], 'full')
