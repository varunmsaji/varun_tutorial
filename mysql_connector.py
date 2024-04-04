import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user ='root',
    password ='root',
    database ='varun'
)

if conn:
    print("connection sucessfull")
else:
    print("connection not sucessfull")    

cursor = conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS users(
               id INT,
               name VARCHAR(225),
               age INT
)''')

cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('John', 30))

conn.commit()

cursor.execute("SELECT * FROM users")

rows= cursor.fetchall()
for row in rows:
    print(row)

    