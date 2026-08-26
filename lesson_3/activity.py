import sqlite3
import pandas as pd 

database="database.sqlite"
conn=sqlite3.connect(database)
x=pd.read_sql("select * from sqlite_master",conn)
print(x)