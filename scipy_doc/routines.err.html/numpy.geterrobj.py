import numpy as np

np.geterrobj()  # first get the defaults


def err_handler(err_type, flag):
    print
    "Floating point error (%s), with flag %s" % (err_type, flag)


old_bufsize = np.setbufsize(20000)
old_err = np.seterr(divide='raise')
old_handler = np.seterrcall(err_handler)
np.geterrobj()
old_err = np.seterr(all='ignore')
np.base_repr(np.geterrobj()[1], 8)
old_err = np.seterr(divide='warn', over='log', under='call')
np.base_repr(np.geterrobj()[1], 8)
