import sqlite3
import csv

conn = sqlite3.connect('sales_assignment.db')
cur = conn.cursor()

query = '''
SELECT
    c.customer_id as Customer,
    c.age as Age,
    i.item_name as Item,
    SUM(o.quantity) as Quantity
FROM Orders o
JOIN Sales s ON o.sales_id = s.sales_id
JOIN Customer c ON s.customer_id = c.customer_id
JOIN Items i ON o.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35
AND o.quantity IS NOT NULL
GROUP BY c.customer_id, c.age, i.item_name
HAVING SUM(o.quantity) > 0
ORDER BY c.customer_id, i.item_name
'''

cur.execute(query)
rows = cur.fetchall()

with open('output_sql.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Customer', 'Age', 'Item', 'Quantity'])
    writer.writerows(rows)

print("SQL solution executed and CSV file created: output_sql.csv")

conn.close()
