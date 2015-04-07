import numpy as np

loc, scale = 0., 1.
s = np.random.laplace(loc, scale, 1000)
import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(s, 30, normed=True)
x = np.arange(-8., 8., .01)
pdf = np.exp(-abs(x - loc) / scale) / (2. * scale)
plt.plot(x, pdf)
pi_ = 1 / (scale * np.sqrt(2 * np.pi))
g = (pi_ *
     np.exp(-(x - loc) ** 2 / (2 * scale ** 2)))
plt.plot(x, g)
