import sqlite3
import pandas as pd 

database = sqlite3.connect("database.sqlite")
tables=pd.read_sql("select * from sqlite_master",database)
#print(tables)
student=pd.read_sql("select * from students",database)
#print(student)

distinct=pd.read_sql("select  DISTINCT city from students",database)
#print(distinct)

x=pd.read_sql("select name,city from students order by name ASC",database)
#print(x)

d=pd.read_sql("select name,city from students order by name DESC",database)
print(d)

c=pd.read_sql("select age,count(age) from students group by age",database)
print(c)

z=pd.read_sql("select age,count(age) ,sum(age),avg(age) from students group by age",database)
print(z)