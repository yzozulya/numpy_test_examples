import numpy as np


def err_handler(err_type, flag):
    print
    "Floating point error (%s), with flag %s" % (err_type, flag)


saved_handler = np.seterrcall(err_handler)
save_err = np.seterr(all='call')
np.array([1, 2, 3]) / 0.0
np.seterrcall(saved_handler)
np.seterr(**save_err)


class Log(object):
    @staticmethod
    def write(msg):
        print
        "LOG: %s" % msg


log = Log()
saved_handler = np.seterrcall(log)
save_err = np.seterr(all='log')
np.array([1, 2, 3]) / 0.0
np.seterrcall(saved_handler)
np.seterr(**save_err)
