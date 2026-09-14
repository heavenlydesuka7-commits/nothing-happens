import sqlite3
import pandas as pd


connection = sqlite3.connect("sports_team.db")



conn.execute(
    """
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER CHECK(age >= 18),
    team TEXT DEFAULT 'Free Agent'
)
"""
)


valid_players = [
    (1, "Alex", 24, "Warriors"),
    (2, "Jordan", 19, "Lakers"),
    (3, "Taylor", 30, None),  
]

for player in valid_players:
    conn.execute("INSERT OR IGNORE INTO players VALUES (?, ?, ?, ?)", player)
connection.commit()


try:
    
    conn.execute("INSERT INTO players VALUES (4, 'Sam', 15, 'Bulls')")
except sqlite3.IntegrityError as error:
    print("Blocked invalid entry successfully")
    print(error)


player_dataframe = pd.read_sql_query("SELECT * FROM players", connection)
print(player_dataframe)


player_dataframe["team"] = player_dataframe["team"].fillna("Free Agent")
print(player_dataframe)
