import pandas as pd

df = pd.read_csv(r"C:\Users\chaudadi\data.csv")
print(df.to_string())
print(df)

print(pd.options.display.max_rows)
pd.options.display.max_rows = 999
df = pd.read_csv(r"C:\Users\chaudadi\data.csv")
print(df)