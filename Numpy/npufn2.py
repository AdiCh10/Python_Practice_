import numpy as np

def myadd(x, y):
    return (x + y)

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

def blahblah():
    print("Blahblah!! Duh.....")

print(type(np.add))
print(type(myadd))
print(type(np.concatenate))
print(type(blahblah))

if type(np.add) == np.ufunc:
    print("add is ufunc")
else:
    print("add is not ufunc")