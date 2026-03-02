import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print(newarr)

newarr = np.intersect1d(arr1, arr2)
print(newarr)

newarr = np.setdiff1d(arr1, arr2, assume_unique = True)
print(newarr)

newarr = np.setxor1d(arr1, arr2, assume_unique = True)
print(newarr)