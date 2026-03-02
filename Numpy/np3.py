import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

arr = np.array((1, 2, 3, 4, 5))

print(arr)

arr0 = np.array(42)

arr1 = np.array([1, 2, 3, 4, 5])

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr0)

print(arr1)

print(arr2)

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3)

arr = np.array([1, 2, 3, 4], ndmin = 5)

print(arr)
print("number of dimensions: ", arr.ndim)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ndim)