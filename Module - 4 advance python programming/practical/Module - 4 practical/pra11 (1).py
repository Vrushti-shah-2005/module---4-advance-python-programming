import sqlite3

conn = sqlite3.connect("my_database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
print("Table 'students' created successfully.")

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Dhruvi", 21))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Raj", 22))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Priya", 20))
print("Data inserted successfully.")

conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)

conn.close()
