import sqlite3

conn = sqlite3.connect('sales_assignment.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Customer')
cur.execute('DROP TABLE IF EXISTS Sales')
cur.execute('DROP TABLE IF EXISTS Items')
cur.execute('DROP TABLE IF EXISTS Orders')

cur.execute('''
CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER
)
''')

cur.execute('''
CREATE TABLE Sales (
    sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    FOREIGN KEY(customer_id) REFERENCES Customer(customer_id)
)
''')

cur.execute('''
CREATE TABLE Items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT
)
''')

cur.execute('''
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sales_id INTEGER,
    item_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(sales_id) REFERENCES Sales(sales_id),
    FOREIGN KEY(item_id) REFERENCES Items(item_id)
)
''')

cur.executemany('INSERT INTO Customer(age) VALUES (?)', [(21,), (23,), (35,)])

cur.executemany('INSERT INTO Items(item_name) VALUES (?)', [('x',), ('y',), ('z',)])

cur.executemany('INSERT INTO Sales(customer_id) VALUES (?)', [(1,), (1,), (2,), (2,), (3,), (3,)])

orders_data = [
    (1, 1, 5),
    (2, 1, 5),
    (3, 1, 1),
    (4, 2, 1),
    (4, 3, 1),
    (5, 3, 1),
    (6, 3, 1)
]

cur.executemany('INSERT INTO Orders(sales_id, item_id, quantity) VALUES (?, ?, ?)', orders_data)

conn.commit()
conn.close()

print("Dummy SQLite database created successfully.")
