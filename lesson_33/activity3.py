import sqlite3
import pandas as pd

database = sqlite3.connect("database.sqlite")

books = pd.read_sql("select * from books", database)
#print(books)

genre = pd.read_sql("select * from books where genre = 'Fantasy'", database)
#print(genre)

title = pd.read_sql("select * from books where title like '%Harry%'", database)
#print(title)

price = pd.read_sql("select min(price), max(price) from books", database)
#print(price)

groupby = pd.read_sql("select genre, count(*) as count from books group by genre", database)
print(groupby)




