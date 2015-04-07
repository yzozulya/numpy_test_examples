import numpy as np

rl = np.outer(np.ones((5,)), np.linspace(-2, 2, 5))
rl
im = np.outer(1j * np.linspace(2, -2, 5), np.ones((5,)))
im
grid = rl + im
grid
x = np.array(['a', 'b', 'c'], dtype=object)
np.outer(x, [1, 2, 3])
