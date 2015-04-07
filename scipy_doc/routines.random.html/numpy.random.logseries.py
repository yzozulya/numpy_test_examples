import numpy as np
import matplotlib.pyplot as plt
from numpy.ma import log

a = .6
s = np.random.logseries(a, 10000)
count, bins, ignored = plt.hist(s)


def logseries(k, p):
    return -p ** k / (k * log(1 - p))


plt.plot(bins, logseries(bins, a) * count.max() /
         logseries(bins, a).max(), 'r')
plt.show()