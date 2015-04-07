import numpy as np

print
round(np.nper(0.07 / 12, -150, 8000), 5)
np.nper(*(np.ogrid[0.07 / 12: 0.08 / 12: 0.01 / 12,
          -150: -99: 50,
          8000: 9001: 1000]))
