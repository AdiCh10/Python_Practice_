import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

filter_array = []

for element in arr:
    if element>42:
        filter_array.append(True)
    else:
        filter_array.append(False)

newarr = arr[filter_array]
print(filter_array)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr = np.array(["a", "b", "c"])
x = arr[[True, False, True]]
print(x)