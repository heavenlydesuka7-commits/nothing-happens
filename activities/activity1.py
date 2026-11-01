import pandas as pd

df = pd.read_csv('bestseller_books.csv')

print(df.dtypes)

print(df.isnull().sum())

df_cleaned = df.fillna(0)

print(df_cleaned.isnull().sum())
