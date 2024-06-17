import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

# select
cursor.execute("SELECT * FROM posts")
rows = cursor.fetchall()
print(rows)

new_rows = [(None, "fake blog 1"), (None, "fake blog 2")]

# insert
cursor.executemany("INSERT INTO posts VALUES (?,?)", new_rows)
connection.commit()
