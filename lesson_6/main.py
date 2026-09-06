import sqlite3

import pandas as pd


conn = sqlite3.connect('database2.db')

try:
    conn.execute("CREATE TABLE recipe (recipe_id INTEGER PRIMARY KEY, recipe_name TEXT NOT NULL, cuisine TEXT NOT NULL, prep_mins INTEGER NOT NULL)")

    conn.execute("CREATE TABLE ingredient (ingredient_id INTEGER PRIMARY KEY, recipe_id INTEGER NOT NULL, item TEXT NOT NULL, quantity_g INTEGER NOT NULL)")

    conn.executemany("INSERT INTO recipe VALUES (?, ?, ?, ?)", [

    (1, 'Pasta', 'Italian', 20),

    (2, 'Tacos', 'Mexican', 15),

    (3, 'Sushi', 'Japanese', 45),

    (4, 'Pizza', 'Italian', 30),

    (5, 'Salad', 'Greek', 10),

    ])

    conn.executemany("INSERT INTO ingredient VALUES (?, ?, ?, ?)", [

    (1, 1, 'Pasta', 200),

    (2, 1, 'Sauce', 150),

    (3, 2, 'Tortilla', 80),

    (4, 2, 'Beef', 120),

    (5, 3, 'Salmon', 180),

    (6, 4, 'Dough', 250),

    (7, 5, 'Lettuce', 50),

    (8, 5, 'Feta', 40),

    ])

    conn.commit()

except:
    conn.rollback()
    print("invalid")

a=pd.read_sql("select * from recipe",conn)
print(a)

b=pd.read_sql("select * from ingredient",conn)
print(b)

c=pd.read_sql("select recipe_id as restaurent_id,cuisine as style,prep_mins as time,recipe_name as restaurent_name from recipe",conn)
print(c)

d=pd.read_sql("select R.recipe_name, R.cuisine, I.item, I.quantity_g from recipe  as R inner join ingredient as I on R.recipe_id = I.recipe_id",conn)
print(d)

e=pd.read_sql("select recipe_name,cuisine from recipe where recipe_id  IN(select recipe_id from ingredient where quantity_g >100)",conn)
print(e)

f=pd.read_sql("select recipe_name,cuisine from recipe where prep_mins=(select  MIN( prep_mins) from recipe)",conn)
print(f)