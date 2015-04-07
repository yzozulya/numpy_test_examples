import numpy as np

np.random.choice(5, 3)
# This is equivalent to np.random.randint(0,5,3)
np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
np.random.choice(5, 3, replace=False)
# This is equivalent to np.random.permutation(np.arange(5))[:3]
np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
