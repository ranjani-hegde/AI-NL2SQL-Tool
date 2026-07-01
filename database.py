import sqlite3

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    category TEXT,
    month TEXT,
    quantity INTEGER,
    sales_amount INTEGER
)
""")

data = [
    ("Laptop", "Electronics", "January", 5, 250000),
    ("Phone", "Electronics", "January", 10, 300000),
    ("Shoes", "Fashion", "February", 20, 80000),
    ("Watch", "Accessories", "March", 15, 120000),
    ("Bag", "Fashion", "January", 12, 60000)
]

cursor.executemany("""
INSERT INTO sales (product, category, month, quantity, sales_amount)
VALUES (?, ?, ?, ?, ?)
""", data)

conn.commit()
conn.close()

print("Database created successfully!") 