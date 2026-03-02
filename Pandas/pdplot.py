import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\chaudadi\data3.csv")

df.plot()
plt.show()

df.plot(kind = "scatter", x = "Duration", y = "Calories")
plt.show()

df.plot(kind = "scatter", x = "Duration", y = "Maxpulse")
plt.show()

df["Duration"].plot(kind = "hist")
plt.show()