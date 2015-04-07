import numpy as np

s = np.random.negative_binomial(1, 0.1, 100000)
for i in range(1, 11):
    probability = sum(s < i) / 100000.
    print
    i, "wells drilled, probability of one success =", probability
