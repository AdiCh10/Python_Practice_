import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

sorted_arr = np.sort(arr)
print(sorted_arr.base)

arr = np.array(["banana", "cherry", "apple", "strawberry"])
print(np.sort(arr))

arr = np.array([True, False, False])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))