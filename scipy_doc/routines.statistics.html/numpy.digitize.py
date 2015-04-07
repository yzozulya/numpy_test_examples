import numpy as np

x = np.array([0.2, 6.4, 3.0, 1.6])
bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
inds = np.digitize(x, bins)
inds
for n in range(x.size):
    print
    bins[inds[n] - 1], "<=", x[n], "<", bins[inds[n]]
x = np.array([1.2, 10.0, 12.4, 15.5, 20.])
bins = np.array([0, 5, 10, 15, 20])
np.digitize(x, bins, right=True)
np.digitize(x, bins, right=False)
