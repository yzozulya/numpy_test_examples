import numpy as np

z = np.random.geometric(p=0.35, size=10000)
(z == 1).sum() / 10000.
