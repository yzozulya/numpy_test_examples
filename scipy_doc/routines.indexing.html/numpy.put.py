import numpy as np

a = np.arange(5)
np.put(a, [0, 2], [-44, -55])
a
a = np.arange(5)
np.put(a, 22, -5, mode='clip')
a
