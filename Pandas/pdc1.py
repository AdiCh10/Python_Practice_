import pandas as pd

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
new_df = df.dropna()
print(new_df.to_string())

# df.dropna(inplace = True)
# print(df.to_string())

new_df = df.fillna(130)
print(new_df.to_string())

# df.fillna(130, inplace = True)

new_df = df.fillna({"Calories": 130})
print(new_df.to_string())

# df.fillna({"Calories": 130}, inplace = True)

x = df["Calories"].mean()
new_df = df.fillna({"Calories": x})
print(new_df.to_string())

# df.fillna({"Calories": x}, inplace = True)

x = df["Calories"].median()
new_df = df.fillna({"Calories": x})
print(new_df.to_string())

# df.fillna({"Calories": x}, inplace = True)

x = df["Calories"].mode()[0]
new_df = df.fillna({"Calories": x})
print(new_df.to_string())

# df.fillna({"Calories": x}, inplace = True)