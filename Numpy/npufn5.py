import numpy as np
from math import log

arr = np.arange(1, 10)

print(np.log2(arr))

print(np.log10(arr))

print(np.log(arr))

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))