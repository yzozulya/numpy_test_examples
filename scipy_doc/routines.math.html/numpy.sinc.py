import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 41)
np.sinc(x)
plt.plot(x, np.sinc(x))
plt.title("Sinc Function")
plt.ylabel("Amplitude")
plt.xlabel("X")
plt.show()
x = np.linspace(-4, 4, 401)
xx = np.outer(x, x)
plt.imshow(np.sinc(xx))
