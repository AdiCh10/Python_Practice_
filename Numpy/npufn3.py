import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([2, 5, 7, 4, 9, 3])
newarr = np.multiply(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 4, 3, 5, 10, 12])
newarr = np.divide(arr1, arr2)
print(newarr)

arr1 = np.array([2, 3, 5, 10, 40])
arr2 = np.array([9, 4, 4, 5, 2])
newarr = np.power(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([3, 7, 9, 8, 2])
newarr_rem = np.remainder(arr1, arr2)
newarr = np.mod(arr1, arr2)
newarray = np.divmod(arr1, arr2)
print(newarr_rem)
print(newarr)
print(newarray)

arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

x = [2, 5, 5, 1]
y = [1, 4, 3, 1]
z = np.subtract(x, y)
print(z)