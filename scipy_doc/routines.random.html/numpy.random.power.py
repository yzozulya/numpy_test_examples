import numpy as np

a = 5.  # shape
samples = 1000
s = np.random.power(a, samples)
import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(s, bins=30)
x = np.linspace(0, 1, 100)
y = a * x ** (a - 1.)
normed_y = samples * np.diff(bins)[0] * y
plt.plot(x, normed_y)
plt.show()
from scipy import stats

rvs = np.random.power(5, 1000000)
rvsp = np.random.pareto(5, 1000000)
xx = np.linspace(0, 1, 100)
powpdf = stats.powerlaw.pdf(xx, 5)
plt.figure()
plt.hist(rvs, bins=50, normed=True)
plt.plot(xx, powpdf, 'r-')
plt.title('np.random.power(5)')
plt.figure()
plt.hist(1. / (1. + rvsp), bins=50, normed=True)
plt.plot(xx, powpdf, 'r-')
plt.title('inverse of 1 + np.random.pareto(5)')
plt.figure()
plt.hist(1. / (1. + rvsp), bins=50, normed=True)
plt.plot(xx, powpdf, 'r-')
plt.title('inverse of stats.pareto(5)')
