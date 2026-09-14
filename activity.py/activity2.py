import sqlite3
import pandas as pd

conn = sqlite3.connect("memory")  
conn.execute(
    "CREATE TABLE animals (id INT, name TEXT, habitat TEXT, age INT, count INT)"
)


data = [
    (1, "Lion", "Savannah", 5, 12),
    (2, "Zebra", "Savannah", 3, 25),
    (3, "Penguin", "Polar", 2, 40),
    (4, "Polar Bear", "Polar", 6, 8),
]
conn.executemany("INSERT INTO animals VALUES (?,?,?,?,?)", data)

df = pd.read_sql_query("SELECT * FROM animals", conn)


print(" Unique Habitats ", df["habitat"].unique())
print("Sorted by Age ", df.sort_values(by="age"))
print(" Total Animals  ", df["count"].sum())
print(" Average Age ", df["age"].mean())
print("Grouped by Habitat (Counts)", df.groupby("habitat").size())