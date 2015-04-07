import numpy as np
import matplotlib.pyplot as plt

h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
             normed=True)
plt.show()
