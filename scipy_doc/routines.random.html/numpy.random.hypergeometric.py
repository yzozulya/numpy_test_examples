import numpy as np

ngood, nbad, nsamp = 100, 2, 10
s = np.random.hypergeometric(ngood, nbad, nsamp, 1000)
hist(s)
s = np.random.hypergeometric(15, 15, 15, 100000)
sum(s >= 12) / 100000. + sum(s <= 3) / 100000.
