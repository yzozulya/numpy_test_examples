import numpy as np

data = range(1, 5)
data
np.average(data)
np.average(range(1, 11), weights=range(10, 0, -1))
data = np.arange(6).reshape((3, 2))
data
np.average(data, axis=1, weights=[1. / 4, 3. / 4])
np.average(data, weights=[1. / 4, 3. / 4])
