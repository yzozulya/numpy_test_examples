import numpy as np

phase = np.linspace(0, np.pi, num=5)
phase[3:] += np.pi
phase
np.unwrap(phase)
