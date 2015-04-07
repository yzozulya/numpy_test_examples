import numpy as np

np.sin(np.pi / 2.)
np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.)
import matplotlib.pylab as plt

x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()
