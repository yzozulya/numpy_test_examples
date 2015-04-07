import numpy as np
from numpy import *
import matplotlib.pyplot as plt

nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = meshgrid(x, y)
xv
yv
xv, yv = meshgrid(x, y, sparse=True)  # make sparse output arrays
xv
yv
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = meshgrid(x, y, sparse=True)
z = np.sin(xx ** 2 + yy ** 2) / (xx ** 2 + yy ** 2)
h = plt.contourf(x, y, z)
