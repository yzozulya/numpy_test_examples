import numpy as np

a = 2.  # parameter
s = np.random.zipf(a, 1000)
import matplotlib.pyplot as plt
import scipy.special as sps

count, bins, ignored = plt.hist(s[s < 50], 50, normed=True)
x = np.arange(1., 50.)
y = x ** (-a) / sps.zetac(a)
plt.plot(x, y / max(y), linewidth=2, color='r')
plt.show()
