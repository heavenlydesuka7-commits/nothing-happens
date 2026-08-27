import sqlite3
import pandas as pd 
 
database=sqlite3.connect("database.sqlite")
tables=pd.read_sql("select * from sqlite_master",database)
#print(tables)

students=pd.read_sql("select * from students",database)
#print(students)

courses=pd.read_sql("select * from courses",database)
#print(courses)


enrollments=pd.read_sql("select * from enrollments",database)
#print(enrollments)

distinct=pd.read_sql("select DISTINCT city from students",database)
#print(distinct)

age=pd.read_sql("select name, age from students where age >=17",database)
#print(age)

name=pd.read_sql("select name from students where name like '%a%'",database)
#print(name)


age2=pd.read_sql("select  min(age), max(age)  from students",database)
#print(age2)


groupby=pd.read_sql("select count(age) as  count_of_ages, age from students group by age",database)
print(groupby)