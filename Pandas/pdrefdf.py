import pandas as pd

data = [[-50, 40, 30], [-1, 2, -2]]
df = pd.DataFrame(data)

print(df.abs())

data = {
    "points": [100, 120, 114],
    "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.add(15))

data = {
    "age": [50, 40, 30, 40, 20, 10, 30],
    "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)

newdf = df.add_prefix("person_")
print(newdf)

newdf = df.add_suffix("_after")
print(newdf)

data = {
    "x": [50, 40, 30],
    "y": [300, 1112, 42]
}
df = pd.DataFrame(data)

x = df.agg(["sum"])
print(x)

x = df.aggregate(["sum"])
print(x)

df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6]],
                   columns = ["A", "B", "C"], index = [1, 2])
df2 = pd.DataFrame([[10, 20], [30, 40], [50, 60]],
                   columns = ["B", "D"], index = [2, 3, 4])
a1, a2 = df1.align(df2, join = "outer", axis = None)
print("a1:\n", a1)
print("a2:\n", a2)

data = [[True, False, True], [True, True, True]]
df = pd.DataFrame(data)
print(df.all())

data = [[True, False, True], [True, False, False]]
df = pd.DataFrame(data)
print(df.any())

def make_big(x):
    return x.upper()

data = {
    "name": ["Sally", "Mary", "John"],
    "city": ["London", "Tokyo", "Madrid"]
}
df = pd.DataFrame(data)
newdf = df.map(make_big)
print(newdf)

def calc_sum(x):
    return x.sum()

data = {
    "x": [50, 40, 30],
    "y": [300, 1112, 42]
}
df = pd.DataFrame(data)

x = df.apply(calc_sum)
print(x)

data = {
    "age": [16, 14, 10],
    "qualified": [True, True, True]
}
df = pd.DataFrame(data)

newdf = df.assign(name = ["Emil", "Tobias", "Linus"])
print(newdf)

data = {
    "Duration": [50, 40, 45],
    "Pulse": [109, 117, 110],
    "Calories": [409.1, 479.5, 340.8]
}
df = pd.DataFrame(data)

newdf = df.astype("int64")
print(newdf)

data = {
    "firstname": ["Sally", "Mary", "John"],
    "age": [50, 40, 30],
    "qualified": [True, False, False]
}
df = pd.DataFrame(data)
print(df.at[1, "firstname"])

df = pd.read_csv(r"C:\Users\chaudadi\data3.csv")
print(df.axes)

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
print(df.to_string())
newdf = df.bfill()
print(newdf.to_string())

data = {
    "myval": [True]
}
df = pd.DataFrame(data)
print(df.bool())

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
print(df.columns)

df1 = pd.DataFrame([[1, 2], [3, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])

def myfunc(a, b):
    if (a.sum() > b.sum()):
        return a
    else:
        return b

print(df1.combine(df2, myfunc))

df1 = pd.DataFrame([[1, 2], [None, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])
print(df1.combine_first(df2))

df1 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})
df2 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 99, 6],
    "C": [7, 8, 101]
})
differences = df1.compare(df2, align_axis=1, result_names=('df1_val', 'df2_val'))
print(differences)

data = {
    "name": ["Sally", "Mary", pd.NA],
    "qualified": [True, False, pd.NA]
}
df = pd.DataFrame(data)

print("Original dtypes: ")
print(df.dtypes)

newdf = df.convert_dtypes()

print("New dtypes: ")
print(newdf.dtypes)

data = {
    "Duration": [50, 40, 45],
    "Pulse": [109, 117, 110],
    "Calories": [409.1, 479.5, 340.8]
}
df = pd.DataFrame(data)
print(df.corr())

data = {
    "Duration": [50, 40, None, None, 90, 20],
    "Pulse": [109, 140, 110, 125, 138, 170]
}

df = pd.DataFrame(data)
print(df.count())

data = [[5, 6, 7], [2, 6, 9]]
df = pd.DataFrame(data)
print(df.cov())

data = {
    "name": ["Sally", "Mary", "John"],
    "qualified": [True, False, False]
}
df = pd.DataFrame(data)

newdf = df.copy()
print(newdf)

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)

print(df.cummax())
print(df.cummin())
print(df.cumprod())
print(df.cumsum())

print(df.describe())
print(df.diff())
print(df.diff(axis = 1))

data = {
    "points": [100, 120, 114],
    "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.div(10))

df1 = pd.DataFrame([[1, 2], [3, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])
print(df1.dot(df2))

data = {
    "firstname": ["Sally", "Mary", "John"],
    "age": [50, 40, 30],
    "qualified": [True, False, False]
}
df = pd.DataFrame(data)

newdf = df.drop("age", axis = "columns")
print(newdf)

data = {
  "name": ["Sally", "Mary", "John", "Mary"],
  "age": [50, 40, 30, 40],
  "qualified": [True, False, False, False]
}
df = pd.DataFrame(data)

newdf = df.drop_duplicates()
print(newdf)

data = {
    "name": ["Bill", "Bob", "Betty"],
    "age": [50, 50, 30],
    "qualified": [True, False, False]
}
df = pd.DataFrame(data).set_index(["name", "age"])
print(df)
newdf = df.droplevel(0)
print(newdf)

data = {
  "name": ["John", "Mary", "John", "Sally", "Mary"],
  "age": [40, 30, 40, 50, 30],
  "city": ["Bergen", "Oslo", "Stavanger", "Oslo", "Oslo"]
}
df = pd.DataFrame(data)
s = df.duplicated()
print(s)

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
print(df.empty)

df = pd.DataFrame([[10, 12, 7], [3, 4, 7]])
print(df.eq(7))

data1 = {
  "name": ["Sally", "Mary", "John", "Mary"],
  "age": [50, 40, 30, 40]
}
data2 = {
  "name": ["Sally", "Mary", "John", "Mary"],
  "age": [50, 40, 30, 40]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1.equals(df2))

data = {
    "Women": [125, 230, 412],
    "Men": [219, 185, 452]
}
df = pd.DataFrame(data)
print(df.eval("Women + Men"))

data = {
    "Brand": ["Ford", "Ford", "Ford"],
    "Model": ["Sierra", "F-150", "Mustang"],
    "Type": ["2.0 GL", "Raptor", ["Mach-E", "Mach-1"]]
}
df = pd.DataFrame(data)

newdf = df.explode("Type")
print(newdf)

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
newdf = df.ffill()
print(newdf)

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
newdf = df.filter(items = ["name", "age"])
print(newdf)

jan = pd.date_range(start = "2026-01-01", end = "2026-01-31")
data = {
    "registered": [5, 4, 3, 4, 3, 5, 1, 6, 1, 9, 5, 3, 7, 2, 8, 4, 4, 6, 4, 3, 2, 5, 3, 4, 2, 6, 8, 5, 3, 4, 5]
}
df = pd.DataFrame(data, index = jan)
print(df.first("7D"))

data = {
  "points": [100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.floordiv(10))

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.ge(7))

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
print(df.get("firstname"))

# Doubt
data = {
    "co2": [95, 90, 99, 104, 105, 94, 99, 104],
    "model": ["Citigo", "Fabia", "Fiesta", "Rapid", "Focus", "Mondeo", "Octavia", "B-Max"],
    "car": ["Skoda", "Skoda", "Ford", "Skoda", "Ford", "Ford", "Skoda", "Ford"]
}
df = pd.DataFrame(data)
x = df.groupby("car")
print(x)

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.gt(7))

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
print(df.iat[2, 1])

data = {
    "sales": [23, 34, 56],
    "age": [50, 40, 30]
}
df = pd.DataFrame(data)

print(df.idxmax())
print(df.idxmin())

data = [[50, True], [40, False], [30, False]]
df = pd.DataFrame(data)
print(df.iloc[1, 0])
print(df.iloc[0:2])

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
print(df.index)

data = {
    "age": ["fifty", 40, 30],
    "qualified": ["No", True, False]
}
df = pd.DataFrame(data)

print("Original Dataframe:")
print(df)
print("Orignal dtypes:")
print(df.dtypes)

df = df.iloc[1:]

print("New DataFrame: ")
print(df)

newdf = df.infer_objects()
print("New dtypes:")
print(newdf.dtypes)

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
df.info()

data = {
  "name": ["Sally", "Mary", "John"],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
print(df)
df.insert(1, "age", [50, 40, 30])
print(df)

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
newdf = df.interpolate(method = "linear")
print(newdf)

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
print(df.isin([50, 40]))

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
newdf = df.isna()
print(newdf)
newdf = df.isnull()
print(newdf)

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)

for x, y in df.items():
    print(x)
    print(y)

for index, row in df.iterrows():
  print(row["firstname"])

for row in df.itertuples():
  print(row)

data1 = {
    "name": ["Sally", "Mary", "John"],
    "age": [50, 40, 30]
}
data2 = {
    "qualified": [True, False, False]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

newdf = df1.join(df2)
print(newdf)

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
print(df.keys())

data = {"A": [55, 60, 48, 60, 50],
        "B": [42, 30, 50, 40, 47],
        "C": [70, 75, 55, 44, 66]}
df = pd.DataFrame(data)
x = df.kurtosis()
print(x)

jan = pd.date_range(start = "2026-01-01", end = "2026-01-31")
data = {
    "registered": [5, 4, 3, 4, 3, 5, 1, 6, 1, 9, 5, 3, 7, 2, 8, 4, 4, 6, 4, 3, 2, 5, 3, 4, 2, 6, 8, 5, 3, 4, 5]
}
df = pd.DataFrame(data, index = jan)
print(df.last("7D"))

df = pd.DataFrame([[10, 7, 2], [3, 4, 7]])
print(df.le(7))
print(df.lt(7))

data = [[50, True], [40, False], [30, False]]
label_rows = ["Sally", "Mary", "John"]
label_cols = ["age", "qualified"]
df = pd.DataFrame(data, label_rows, label_cols)
print(df.loc["Mary", "age"])

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.mask(df["age"] > 30)
print(newdf)
newdf = df.where(df["age"] > 30)
print(newdf)

# Doubt
data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.max())
print(df.min())

data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.mean())
print(df.median())
print(df.mode())

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
newdf = df.melt()
print(newdf.to_string())
newdf = df.memory_usage()
print(newdf)

# Doubt
data1 = {
    "name": ["Sally", "Mary", "John"],
    "age": [50, 40, 30]
}
data1 = {
    "name": ["Sally", "Peter", "Micky"],
    "age": [50, 44, 22]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# newdf = df1.merge(df2)
# print(newdf)

data = {
    "points": [5, 6, 4],
    "total": [50, 40, 20]
}
df = pd.DataFrame(data)
print(df.mod(3))

data = {
  "points": [100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.mul(10))

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
print(df.ndim)

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.ne(7))

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
newdf = df.nlargest(10, "Calories")
print(newdf)
newdf = df.notna()
print(newdf)
newdf = df.notnull()
print(newdf)
newdf = df.nsmallest(10, "Calories")
print(newdf)

data = [[10, 20, 0], [10, 10, 10], [10, 20, 30]]
df = pd.DataFrame(data)
print(df.nunique())

data = [[10, 18, 11], [20, 15, 8], [30, 20, 3]]
df = pd.DataFrame(data)
print(df.pct_change())

def change_age(x):
    x["age"] = [10, 20, 30]
    return x

data = {
    "name": ["Sally", "Mary", "John"],
    "age": [50, 40, 30]
}

df = pd.DataFrame(data)
df.pipe(change_age)
print(df)

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
df.pop('age')
print(df)

data = {
    "points": [4, 5, 6],
    "total": [10, 12, 15]
}

df = pd.DataFrame(data)
print(df.pow(2))

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.prod())
print(df.product())

data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.quantile(0.2))

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
print(df.query('age > 35'))

data = {
  "points": [100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)

print(df.radd(15))
print(df.rdiv(10))

data = {
  "age": [50, 40, 30, 40],
  "qualified": [True, False, False, False]
}
idx = ["Sally", "Mary", "John", "Monica"]
df = pd.DataFrame(data, index=idx)
print(df)
newidx = ["Robert", "Cindy", "Chloe", "Pete"]
newdf = df.reindex(newidx)
print(newdf)

data = {
"age": [50, 40, 30],
"qualified": [True, False, False]
}
idx = ["Sally", "Mary", "John"]
df = pd.DataFrame(data, index=idx)
print(df)
newdf = df.rename({"Sally": "Pete", "Mary": "Patrick", "John": "Paula"})
print(newdf)
newdf = df.rename_axis("members")
print(newdf)

data = {
  "name": ["Bill", "Bob", "Betty"],
  "age": [50, 50, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)

newdf = df.replace(50, 60)
print(newdf)

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
idx = ["X", "Y", "Z"]
df = pd.DataFrame(data, index=idx)
print(df)
newdf = df.reset_index()
print(newdf)

data = {
  "points": [100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.rfloordiv(10))
print(df.rmul(10))
print(df.rsub(15))
print(df.rtruediv(10))
print(df.sub(15))

data = {
   "points": [5, 6, 4],
  "total": [50, 40, 20]
}
df = pd.DataFrame(data)
print(df.rmod(3))

data = [[1.1235, 1.9654, 2.6874], [6.5124, 4.2210, 2.2899]]
df = pd.DataFrame(data)
print(df.round(1))

data = {
  "points": [4, 5, 6],
  "total": [10, 12, 15]
}
df = pd.DataFrame(data)
print(df.rpow(2))

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
print(df.sample())
print(df.size)
print(df.stack())
print(df.take([5, 10]))

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.sem())
print(df.skew())
print(df.std())
print(df.sum())
print(df.var())

data = {
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
newdf = df.set_axis(["John", "Peter", "Alex"])
print(newdf)

data = {
  "name": ["Sally", "Mary", "John", "Monica"],
  "age": [50, 40, 30, 40],
  "qualified": [True, False, False, False]
}
df = pd.DataFrame(data)
newdf = df.set_index("name")
print(newdf)

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
idx = ["Mary", "Sally", "Emil", "Tobias", "Linus", "John", "Peter"]
df = pd.DataFrame(data, index = idx)
newdf = df.sort_index()
print(newdf)

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.sort_values(by='age')
print(newdf)
newdf = df.T
print(newdf)
newdf = df.transpose()
print(newdf)
print(df)
newdf = df.truncate(before=3, after=5)
print(newdf)

data = {
  "age": [50, 40, 30, 40, 20, 10, 30]
}
df = pd.DataFrame(data)
s = df.squeeze()
print(s)

def eur_to_nok(x):
    return x * 10

data = {
    "for1": [2, 6, 3],
    "for5": [8, 20, 12]
}
df = pd.DataFrame(data)
newdf = df.transform(eur_to_nok)
print(newdf)

data = {
  "points": [100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.truediv(10))

df = pd.read_csv(r"C:\Users\chaudadi\workout_data.csv")
print(df.values)

data = {
    "weight": [929, 1109, 1112, 1119, 1328, 1584, 1415, 1235],
    "co2": [95, 90, 99, 104, 105, 94, 99, 104],
    "model": ["Citigo", "Fabia", "Fiesta", "Rapid", "Focus", "Mondeo", "Octavia", "B-Max"],
    "car": ["Skoda", "Skoda", "Ford", "Skoda", "Ford", "Ford", "Skoda", "Ford"]
}
df = pd.DataFrame(data)
df = df.set_index(["car", "model"])
print(df.xs("Ford"))
print(df.xs("Skoda"))

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
for x in df.__iter__():
    print(x)