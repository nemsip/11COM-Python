import sqlite3

conn = sqlite3.connect('login.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    generator_usage INTEGER DEFAULT 0
);''')
print("Table created successfully")

conn.close()