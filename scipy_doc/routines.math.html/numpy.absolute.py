import numpy as np

x = np.array([-1.2, 1.2])
np.absolute(x)
np.absolute(1.2 + 1j)
import matplotlib.pyplot as plt

x = np.linspace(start=-10, stop=10, num=101)
plt.plot(x, np.absolute(x))
plt.show()
xx = x + 1j * x[:, np.newaxis]
plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10])
plt.show()
