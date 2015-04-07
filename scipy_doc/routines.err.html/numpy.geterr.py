import numpy as np

np.geterr()
np.arange(3.) / np.arange(3.)
oldsettings = np.seterr(all='warn', over='raise')
np.geterr()
np.arange(3.) / np.arange(3.)
