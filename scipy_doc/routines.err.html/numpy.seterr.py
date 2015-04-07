import numpy as np

old_settings = np.seterr(all='ignore')  # seterr to known value
np.seterr(over='raise')
np.seterr(**old_settings)  # reset to default
np.int16(32000) * np.int16(3)
old_settings = np.seterr(all='warn', over='raise')
np.int16(32000) * np.int16(3)
old_settings = np.seterr(all='print')
np.geterr()
np.int16(32000) * np.int16(3)
