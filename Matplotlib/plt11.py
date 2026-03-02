import numpy as np
import matplotlib.pyplot as plt

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.show()

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()

mycolors = ["y", "r", "#4CAF50", "c"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

mycolors = ["r", "yellow", "#D2042D", "brown"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()

plt.pie(y, labels = mylabels)
plt.legend(title = "Fruits:")
plt.show()
