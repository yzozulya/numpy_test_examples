import numpy as np

a = np.array([[[1, 0, 1],
               [0, 1, 0]],
              [[1, 1, 0],
               [0, 0, 1]]])
b = np.packbits(a, axis=-1)
b
