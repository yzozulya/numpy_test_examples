import numpy as np

intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515,
                   7515, 8230, 8770])
s = np.random.standard_t(10, size=100000)
np.mean(intake)
intake.std(ddof=1)
t = (np.mean(intake) - 7725) / (intake.std(ddof=1) / np.sqrt(len(intake)))
import matplotlib.pyplot as plt

h = plt.hist(s, bins=100, normed=True)
np.sum(s < t) / float(len(s))
