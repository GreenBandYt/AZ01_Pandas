import pandas as pd

df = pd.read_csv("dz.csv")

# print(df.head(12))
# print(df.info())
# print(df.describe())

group = df.groupby('City')['Salary'].mean()
print(group)
