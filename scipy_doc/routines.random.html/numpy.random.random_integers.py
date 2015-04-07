import numpy as np

np.random.random_integers(5)
type(np.random.random_integers(5))
np.random.random_integers(5, size=(3., 2.))
2.5 * (np.random.random_integers(5, size=(5,)) - 1) / 4.
d1 = np.random.random_integers(1, 6, 1000)
d2 = np.random.random_integers(1, 6, 1000)
dsums = d1 + d2
import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(dsums, 11, normed=True)
plt.show()
