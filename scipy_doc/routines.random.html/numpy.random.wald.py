import numpy as np
import matplotlib.pyplot as plt

h = plt.hist(np.random.wald(3, 2, 100000), bins=200, normed=True)
plt.show()
