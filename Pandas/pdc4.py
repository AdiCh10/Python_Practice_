import pandas as pd

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")

print(df.duplicated())

new_df = df.drop_duplicates()
print(new_df.to_string())

# df.drop_duplicates(inplace = True)