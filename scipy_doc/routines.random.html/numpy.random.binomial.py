import numpy as np

n, p = 10, .5  # number of trials, probability of each trial
s = np.random.binomial(n, p, 1000)
sum(np.random.binomial(9, 0.1, 20000) == 0) / 20000.
