import numpy as np

prob1 = np.log2(1e-50)
prob2 = np.log2(2.5e-50)
prob12 = np.logaddexp2(prob1, prob2)
prob1, prob2, prob12
2 ** prob12
