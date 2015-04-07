import numpy as np

np.arccos([1, -1])
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, num=100)
plt.plot(x, np.arccos(x))
plt.axis('tight')
plt.show()
