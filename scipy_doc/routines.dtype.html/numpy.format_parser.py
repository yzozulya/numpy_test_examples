import numpy as np

np.format_parser(['f8', 'i4', 'a5'], ['col1', 'col2', 'col3'],
                 ['T1', 'T2', 'T3']).dtype
np.format_parser(['f8', 'i4', 'a5'], ['col1', 'col2', 'col3'],
                 []).dtype
np.format_parser(['f8', 'i4', 'a5'], [], []).dtype
