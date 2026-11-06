import sqlite3

#connect to database

connection = sqlite3.connect("retail_sales.db")
cursor = connection.cursor()

#query 1: total revenue

print("\n==== TOTAL REVENUE ====")
cursor.execute("""
SELECT SUM(total_amount)
FROM sales
""")
print("Total Revenue:", cursor.fetchone()[0])

#query 2: city-wise revenue

print("\n==== CITY-WISE REVENUE ====")
cursor.execute("""
SELECT city, SUM(total_amount) AS revenue
FROM sales
GROUP BY city
ORDER BY revenue DESC
""")

for row in cursor.fetchall():
    print(row)

#query 3: product-wise sales

print("\n==== PRODUCT-WISE SALES ====")
cursor.execute("""
SELECT product, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_quantity DESC
""")

for row in cursor.fetchall():
    print(row)

#query 4: highest revenue order

print("\n==== TOP REVENUE ORDER ====")
cursor.execute("""
SELECT order_id, customer_name, total_amount
FROM sales
ORDER BY total_amount DESC
LIMIT 1
""")
print(cursor.fetchone())

#query 5: average order value

print("\n==== AVERAGE ORDER VALUE ====")
cursor.execute("""
SELECT AVG(total_amount)
FROM sales
""")
print("Average Order Value:", cursor.fetchone()[0])

connection.close()