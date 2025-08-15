import sqlite3
import pandas as pd

conn = sqlite3.connect('sales_assignment.db')

query = '''
SELECT
    c.customer_id as Customer,
    c.age as Age,
    i.item_name as Item,
    COALESCE(SUM(o.quantity), 0) as Quantity
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

df = pd.read_sql_query(query, conn)
df.to_csv('output_pandas.csv', sep=';', index=False)

print("Pandas solution executed and CSV file created: output_pandas.csv")

conn.close()
