import numpy as np

x = np.arange(10)
condlist = [x < 3, x > 5]
choicelist = [x, x ** 2]
np.select(condlist, choicelist)
