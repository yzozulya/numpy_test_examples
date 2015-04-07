from matplotlib.pyplot import hist
import numpy as np

values = hist(np.random.rayleigh(3, 100000), bins=200, normed=True)
meanvalue = 1
modevalue = np.sqrt(2 / np.pi) * meanvalue
s = np.random.rayleigh(modevalue, 1000000)
100. * sum(s > 3) / 1000000.
