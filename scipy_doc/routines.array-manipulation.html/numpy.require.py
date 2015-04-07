import numpy as np

x = np.arange(6).reshape(2, 3)
x.flags
y = np.require(x, dtype=np.float32, requirements=['A', 'O', 'W', 'F'])
y.flags
