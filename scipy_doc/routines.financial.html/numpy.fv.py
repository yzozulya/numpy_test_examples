import numpy as np

np.fv(0.05 / 12, 10 * 12, -100, -100)
a = np.array((0.05, 0.06, 0.07)) / 12
np.fv(a, 10 * 12, -100, -100)
