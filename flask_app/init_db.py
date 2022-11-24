import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

current = connection.cursor()

current.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First Post', 'Content for the first post'))

current.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Second Post', 'Content for the second post'))

connection.commit()
connection.close()
