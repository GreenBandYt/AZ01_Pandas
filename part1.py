from lib2to3.pgen2.tokenize import group

import pandas as pd

df = pd.read_csv('animal.csv')
print(df)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

