import numpy as np
import matplotlib.pyplot as plt
from numpy.ma import exp

loc, scale = 10, 1
s = np.random.logistic(loc, scale, 10000)
count, bins, ignored = plt.hist(s, bins=50)


def logist(x, loc_, scale_):
    return exp((loc_ - x) / scale_) / (scale_ * (1 + exp((loc_ - x) / scale_)) ** 2)


plt.plot(bins, logist(bins, loc, scale) * count.max() /
         logist(bins, loc, scale).max())
plt.show()
