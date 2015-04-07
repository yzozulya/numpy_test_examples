import numpy as np


# noinspection PyUnusedLocal
def pprint(arr):
    return 'HA! - What are you going to do now?'


np.set_string_function(pprint)
a = np.arange(10)
a
print
a
np.set_string_function(None)
a
x = np.arange(4)
np.set_string_function(lambda x_: 'random', repr=False)
x.__str__()
x.__repr__()
