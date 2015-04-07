import numpy as np

principal = 2500.00
per = np.arange(1 * 12) + 1
ipmt = np.ipmt(0.0824 / 12, per, 1 * 12, principal)
ppmt = np.ppmt(0.0824 / 12, per, 1 * 12, principal)
pmt = np.pmt(0.0824 / 12, 1 * 12, principal)
np.allclose(ipmt + ppmt, pmt)
fmt = '{0:2d} {1:8.2f} {2:8.2f} {3:8.2f}'
for payment in per:
    index = payment - 1
    principal = principal + ppmt[index]
    print
    fmt.format(payment, ppmt[index], ipmt[index], principal)
interestpd = np.sum(ipmt)
np.round(interestpd, 2)
