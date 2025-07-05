
import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)''')

cursor.executemany("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", [
    ("Alice", "Engineering", 80000),
    ("Bob", "Marketing", 60000),
    ("Charlie", "Engineering", 75000),
    ("David", "Sales", 50000)
])

conn.commit()
conn.close()
