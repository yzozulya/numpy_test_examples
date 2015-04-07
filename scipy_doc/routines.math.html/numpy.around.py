import numpy as np

np.around([0.37, 1.64])
np.around([0.37, 1.64], decimals=1)
np.around([.5, 1.5, 2.5, 3.5, 4.5])  # rounds to nearest even value
np.around([1, 2, 3, 11], decimals=1)  # ndarray of ints is returned
np.around([1, 2, 3, 11], decimals=-1)
