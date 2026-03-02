from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.binomial(n = 10, p = 0.5, size = 10)
print(x)

sns.displot(random.binomial(n = 10, p = 0.5, size = 1000))
plt.show()

data = {
    "normal": random.normal(loc = 50, scale = 5, size = 1000),
    "binomial": random.binomial(n = 100, p = 0.5, size = 1000)
}

sns.displot(data, kind = "kde")
plt.show()