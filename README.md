# Sales Assignment – Snehal Shirture

## Overview
This project uses a SQLite database to calculate the total quantity of each item bought by customers aged 18–35.  
It includes two approaches:  
1. **Pure SQL** – Direct SQL query to fetch the results.  
2. **Pandas** – Using Python Pandas with SQL for processing.

---

## Folder Structure
data/       → Database file & script to create dummy data  
scripts/    → SQL and Pandas solutions  
output/     → Result CSV files  

---

## Requirements
- Python 3.x  
- Pandas  

Install dependencies:
pip install pandas

---

## How to Run
1. Create the database:  
python data/create_dummy_db.py  

2. Run the SQL version:  
python scripts/solution_sql.py  

3. Run the Pandas version:  
python scripts/solution_pandas.py  

---

## Sample Output
Customer;Age;Item;Quantity  
1;21;x;10  
2;23;x;1  
2;23;y;1  
2;23;z;1  
3;35;z;2  

---

**GitHub:** [SnehalShirture](https://github.com/SnehalShirture)
