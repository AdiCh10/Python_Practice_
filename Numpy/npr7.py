from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.poisson(lam = 2, size = 10)
print(x)

sns.displot(random.poisson(lam = 2, size = 1000))
plt.show()

data = {
    "normal": random.normal(loc = 50, scale = 7, size = 1000),
    "poisson": random.poisson(lam = 50, size = 1000)
}

sns.displot(data, kind = "kde")
plt.show()

data = {
    "binomial": random.binomial(n = 1000, p = 0.01, size = 1000),
    "poisson": random.poisson(lam = 10, size = 1000)
}

sns.displot(data, kind = "kde")
plt.show()