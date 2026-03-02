import pandas as pd

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")

df["Date"] = pd.to_datetime(df["Date"], format = "mixed")
print(df.to_string())

new_df = df.dropna(subset = ["Date"])
# df.dropna(subset = ["Date"], inplace = True)
print(new_df.to_string())