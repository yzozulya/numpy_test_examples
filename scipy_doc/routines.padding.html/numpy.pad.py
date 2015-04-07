import numpy as np

a = [1, 2, 3, 4, 5]
np.lib.pad(a, (2, 3), 'constant', constant_values=(4, 6))
np.lib.pad(a, (2, 3), 'edge')
np.lib.pad(a, (2, 3), 'linear_ramp', end_values=(5, -4))
np.lib.pad(a, (2,), 'maximum')
np.lib.pad(a, (2,), 'mean')
np.lib.pad(a, (2,), 'median')
a = [[1, 2], [3, 4]]
np.lib.pad(a, ((3, 2), (2, 3)), 'minimum')
a = [1, 2, 3, 4, 5]
np.lib.pad(a, (2, 3), 'reflect')
np.lib.pad(a, (2, 3), 'reflect', reflect_type='odd')
np.lib.pad(a, (2, 3), 'symmetric')
np.lib.pad(a, (2, 3), 'symmetric', reflect_type='odd')
np.lib.pad(a, (2, 3), 'wrap')


# noinspection PyUnusedLocal
def padwithtens(vector, pad_width, iaxis, kwargs):
    vector[:pad_width[0]] = 10
    vector[-pad_width[1]:] = 10
    return vector


a = np.arange(6)
a = a.reshape((2, 3))
np.lib.pad(a, 2, padwithtens)
