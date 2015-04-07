import numpy as np

test = np.array([0, 1, 2, 5, 0])
states = [0, 2]
mask = np.in1d(test, states)
mask
test[mask]
mask = np.in1d(test, states, invert=True)
mask
test[mask]
