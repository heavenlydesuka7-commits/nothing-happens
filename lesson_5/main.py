import sqlite3

import pandas as pd


conn = sqlite3.connect('database.db')

try:

    conn.execute("""CREATE TABLE author (

    author_id INTEGER PRIMARY KEY,

    author_name TEXT NOT NULL UNIQUE

    )""")

    conn.execute("""CREATE TABLE book (

    book_id INTEGER PRIMARY KEY,

    book_title TEXT NOT NULL,

    author_id INTEGER

    )""")

    conn.executemany("INSERT INTO author VALUES (?, ?)", [

    (1, 'Roald Dahl'),

    (2, 'J.K. Rowling'),

    (3, 'Rick Riordan'),

    (4, 'Jeff Kinney'),

    (5, 'Dav Pilkey'),

    (6, 'Lemony Snicket'),

    ])

    conn.executemany("INSERT INTO book VALUES (?, ?, ?)", [

    (1, 'Charlie and the Chocolate Factory', 1),

    (2, 'James and the Giant Peach', 1),

    (3, 'fullmetal reference and the Philosophers Stone', 2),

    (4, 'Harry Potter and the Chamber of Secrets', 2),

    (5, 'The Lightning Thief', 3),

    (6, 'The Sea of Monsters', 3),

    (7, 'Diary of a Wimpy Kid', 4),

    ])

except:
    conn.rollback()
    print("invalid.............")

conn.commit()

a= pd.read_sql("select * from author ", conn)
print(a)

b= pd.read_sql("select * from author ", conn)
print(b)

c=pd.read_sql("select * from book inner join author on book.author_id=author.author_id",conn)
print(c)

d=pd.read_sql("select * from book left join  author on book.author_id=author.author_id",conn)
print(d)

e=pd.read_sql("select * from book cross join  author on book.author_id=author.author_id",conn)
print(e)

f=pd.read_sql("select * from book union select * from author ",conn)
print(f)

try:
    conn.execute("""CREATE TABLE subjects(

    subject_id INTEGER PRIMARY KEY,

    subject_name TEXT NOT NULL UNIQUE,

    subject_author TEXT NOT NULL UNIQUE


    )""")

    conn.executemany("INSERT INTO subjects VALUES (?, ?,?)", [
        (1,"maths","NCERT")
        (2,"physics","NERCT")
        (3,"mushshsh","suiiiiiiii") 

        ])
    conn.commit()

except:
    print("invalid")



g=pd.read_sql("select * from book union select * from subjects",conn)
print(g)

