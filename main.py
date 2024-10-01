import pandas as pd


df = pd.read_csv('EA_stock_dividend.csv')

print(df.head())

print(df.info())

print(df.describe())