import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
xx = arr.view()
arr[0] = 24

print(arr)
print(xx)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

original_array = np.array([1, 2, 3])
x = original_array.copy()
x[0] = 5
print(original_array)