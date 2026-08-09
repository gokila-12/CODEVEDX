import sqlite3

def init_db():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""

CREATE TABLE IF NOT EXISTS favorites(

id INTEGER PRIMARY KEY AUTOINCREMENT,

email TEXT,

movie TEXT

)

""")