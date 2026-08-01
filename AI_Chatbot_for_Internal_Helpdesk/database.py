import sqlite3

connection = sqlite3.connect("helpdesk.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS faq(
id INTEGER PRIMARY KEY AUTOINCREMENT,
question TEXT,
answer TEXT
)
""")

connection.commit()

connection.close()