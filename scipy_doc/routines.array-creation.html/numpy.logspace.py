import numpy as np
from numpy.ma import power

start = 0
stop = 1
num = 10
endpoint = False
base = 1

y = np.linspace(start, stop, num=num, endpoint=endpoint)

power(base, y).astype(int)

np.logspace(2.0, 3.0, num=4)
np.logspace(2.0, 3.0, num=4, endpoint=False)
np.logspace(2.0, 3.0, num=4, base=2.0)
import matplotlib.pyplot as plt

N = 10
x1 = np.logspace(0.1, 1, N, endpoint=True)
x2 = np.logspace(0.1, 1, N, endpoint=False)
y = np.zeros(N)
plt.plot(x1, y, 'o')
plt.plot(x2, y + 0.5, 'o')
plt.ylim([-0.5, 1])
plt.show()
