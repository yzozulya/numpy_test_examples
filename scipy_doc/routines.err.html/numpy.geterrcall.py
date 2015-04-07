import numpy as np

np.geterrcall()  # we did not yet set a handler, returns None
oldsettings = np.seterr(all='call')


def err_handler(err_type, flag):
    print
    "Floating point error (%s), with flag %s" % (err_type, flag)


oldhandler = np.seterrcall(err_handler)
np.array([1, 2, 3]) / 0.0
cur_handler = np.geterrcall()
cur_handler is err_handler
