import numpy as np
import numpy as np

s = np.random.poisson(5, 10000)
import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(s, 14, normed=True)
plt.show()
s = np.random.poisson(lam=(100., 500.), size=(100, 2))
