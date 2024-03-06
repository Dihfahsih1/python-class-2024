import pandas as pd
data = {"name": ["Aksam", "Cyrus", "Uzumaki"], "Age": [12,34,56]}
df = pd.DataFrame(data)

df = pd.read_csv("csv_file.csv")
# print(df.loc[100])

print(df[df["Index"] > 13])

print(df.describe())

print(df.sort_values(by = "Index", ascending=True))

df.dropna(inplace=True)
print(df)