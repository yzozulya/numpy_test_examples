import numpy as np

a = 5.  # shape
s = np.random.weibull(a, 1000)
import matplotlib.pyplot as plt

x = np.arange(1, 100.) / 50.


def weib(x_, n, a_):
    return (a_ / n) * (x_ / n) ** (a_ - 1) * np.exp(-(x_ / n) ** a_)


count, bins, ignored = plt.hist(np.random.weibull(5., 1000))
x = np.arange(1, 100.) / 50.
scale = count.max() / weib(x, 1., 5.).max()
plt.plot(x, weib(x, 1., 5.) * scale)
plt.show()
