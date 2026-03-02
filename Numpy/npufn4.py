import numpy as np

arr1 = np.trunc([-3.1666, 3.6667])
arr2 = np.fix([-3.1666, 3.6667])
print(arr1)
print(arr2)

arr = np.around(3.1666, 2)
print(arr)

arr = np.floor([-3.1666, 3.6667])
print(arr)

arr = np.ceil([-3.1666, 3.6667])
print(arr)

arr = np.trunc([5.998, 1.455])
print(arr)