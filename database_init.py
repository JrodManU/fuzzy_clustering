import sqlite3

conn = sqlite3.connect('laundromat.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS suggestion_groups(
                id INTEGER PRIMARY KEY,
                date_added TEXT
                )''')

c.execute('''CREATE TABLE IF NOT EXISTS suggestions(
                id INTEGER PRIMARY KEY,
                group_id INTEGER,
                name TEXT,
                date TEXT,
                customer_name TEXT,
                FOREIGN KEY (group_id) REFERENCES suggestion_groups (id)
                )''')
