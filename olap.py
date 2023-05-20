import mysql.connector

# establish a connection to the database
mydb = mysql.connector.connect(user = "sqluser", password = "password", host = "localhost", database = "med_bag")
mycursor = mydb.cursor()
print("Query 1 results:")
# Query 1: Total sales revenue by drug and year, with subtotals by drug and overall total
query1 = """
    SELECT drug.drug_name, drug.drug_manufacturer, SUM(orders_med.order_price) AS total_revenue
    FROM orders_med
    JOIN drug ON orders_med.drug_id = drug.drug_id
    GROUP BY drug.drug_name, drug.drug_manufacturer WITH ROLLUP;
"""

# Execute query 1
mycursor.execute(query1)
result1 = mycursor.fetchall()
for row in result1:
    print(row)
print("\n")
# Query 2: Total sales revenue by state and city, with subtotals by state, city, and overall total
print("Query 2 results:")

query2 = """
    SELECT customer.customer_state, customer.customer_city, SUM(orders_med.order_price) AS total_sales
    FROM orders_med
    JOIN customer ON orders_med.customer_id = customer.customer_id
    GROUP BY customer.customer_state, customer.customer_city WITH ROLLUP;
"""

# Execute query 2
mycursor.execute(query2)
result2 = mycursor.fetchall()
for row in result2:
    print(row)

print("\n")
# Query 3: Average salary by employee position and department, with subtotals by position, department, and overall total
print("Query 3 results:")
query3 = """
    SELECT membership.membership_type, SUM(membership.discount_percentage) AS total_discount
    FROM membership
    GROUP BY membership.membership_type WITH ROLLUP;
"""

# Execute query 3
mycursor.execute(query3)
result3 = mycursor.fetchall()
for row in result3:
    print(row)
print("\n")
# Query 4: Total revenue by customer and membership type, with subtotals by customer, membership type, and overall total
mycursor.execute("""
SELECT customer.customer_name, membership.membership_type,
       SUM(orders_med.order_price) AS total_revenue
FROM orders_med
JOIN customer ON orders_med.customer_id = customer.customer_id
JOIN membership ON customer.customer_id = membership.customer_id
GROUP BY customer.customer_name, membership.membership_type
WITH ROLLUP;
""")
result4 = mycursor.fetchall()
print("Query 4 results:")
for row in result4:
    print(row)

# Close the database connection
mydb.close()