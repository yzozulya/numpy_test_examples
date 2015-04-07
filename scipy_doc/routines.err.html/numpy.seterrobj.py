import numpy as np

old_errobj = np.geterrobj()  # first get the defaults
old_errobj


def err_handler(err_type, flag):
    print
    "Floating point error (%s), with flag %s" % (err_type, flag)


new_errobj = [20000, 12, err_handler]
np.seterrobj(new_errobj)
np.base_repr(12, 8)  # int for divide=4 ('print') and over=1 ('warn')
np.geterr()
np.geterrcall() is err_handler
