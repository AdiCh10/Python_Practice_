from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.rayleigh(scale = 2, size = (2, 3))
print(x)

sns.displot(random.rayleigh(size = 1000), kind = "kde")
plt.show()