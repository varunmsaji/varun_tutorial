# sqlite stores the database in the system itself and not ussing any local host 
#kind of system

import sqlite3

conn = sqlite3.connect('varun.db')

if conn:
    print('suceess')
else:
    print("no")   


cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER
)''')

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John', 30))

conn.commit()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()
for row in rows:
    print(row)
