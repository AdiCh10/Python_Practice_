import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = "o")
plt.show()

plt.plot(ypoints, marker = "*")
plt.show()

plt.plot(ypoints, "o:r")
plt.show()

plt.plot(ypoints, "o--r")
plt.show()

plt.plot(ypoints, "or")
plt.show()

plt.plot(ypoints, marker = "o", ms = 20)
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'y', mfc = 'y')
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()