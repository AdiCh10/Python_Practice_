import numpy as np

arr = np.array([10, 15, 25, 5])
print(arr)
newarr = np.diff(arr)
print(newarr)
newarr = np.diff(arr, n = 2)
print(newarr)

arr = np.array([1, 2, 3, 4])
print(arr)
newarr = np.diff(arr)
print(newarr)