import sqlite3
import pandas as pd

conn = sqlite3.connect("country.db")
conn.execute("""
create table  if not exists city(
city_ID INT PRIMARY KEY,
city_name varchar(255) NOT null unique,
country text NOT null unique,
population INT,
IS_CAPITAL text default 'no'
);
""")
conn.commit()
conn.execute("insert into city values(11,'boston','masschuets',364646364646464646,'no');"),
conn.execute("insert into city values(29,'queens','USA',57384757382388,'yes');"),
conn.execute("insert into city values(49,'doha','qatar',1,'no');"),
conn.execute("insert into city values(649,'barcelona','spain',7583958,'');"),
conn.execute("insert into city values(77,'ni hoa','china',7583958,'');")
conn.execute("insert into city (city_ID,city_name,country) values(101,'california','antartica')")


#x=pd.read_sql("select * from city",conn)
#print(x)
x=pd.read_sql("select * from city",conn)
print(x)

try:
    conn.execute("insert into city values(11,'mumbai','india',838393,'sathvik')")
    conn.execute("insert into city values(12,'delhi', NULL , 57483884,'yes')")
    conn.commit()

except:
    print("data insertiona failed due to duplication of unique id")
    print("cannot be null please insert ur country")
    conn.rollback()

