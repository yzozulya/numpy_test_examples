import numpy as np
import matplotlib.pyplot as plt

values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
                  bins=200, normed=True)
plt.show()
plt.figure()
values = plt.hist(np.random.noncentral_chisquare(3, .0000001, 100000),
                  bins=np.arange(0., 25, .1), normed=True)
values2 = plt.hist(np.random.chisquare(3, 100000),
                   bins=np.arange(0., 25, .1), normed=True)
plt.plot(values[1][0:-1], values[0] - values2[0], 'ob')
plt.show()
plt.figure()
values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
                  bins=200, normed=True)
plt.show()
