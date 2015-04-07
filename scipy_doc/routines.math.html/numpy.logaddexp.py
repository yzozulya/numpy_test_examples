import numpy as np

prob1 = np.log(1e-50)
prob2 = np.log(2.5e-50)
prob12 = np.logaddexp(prob1, prob2)
prob12
np.exp(prob12)
