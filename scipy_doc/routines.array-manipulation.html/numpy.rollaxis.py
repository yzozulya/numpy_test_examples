import numpy as np

a = np.ones((3, 4, 5, 6))
np.rollaxis(a, 3, 1).shape
np.rollaxis(a, 2).shape
np.rollaxis(a, 1, 4).shape
