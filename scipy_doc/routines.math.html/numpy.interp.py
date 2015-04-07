import numpy as np

xp = [1, 2, 3]
fp = [3, 2, 0]
np.interp(2.5, xp, fp)
np.interp([0, 1, 1.5, 2.72, 3.14], xp, fp)
UNDEF = -99.0
np.interp(3.14, xp, fp, right=UNDEF)
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)
xvals = np.linspace(0, 2 * np.pi, 50)
yinterp = np.interp(xvals, x, y)
import matplotlib.pyplot as plt

plt.plot(x, y, 'o')
plt.plot(xvals, yinterp, '-x')
plt.show()
