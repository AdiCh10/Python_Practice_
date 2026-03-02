import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

newarr = arr.reshape(2,6)
print(newarr)

newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(3, 3)
# print(newarr)

print(arr.reshape(2,4).base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
flat = arr.flatten()
print(flat)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(6)
print(newarr)