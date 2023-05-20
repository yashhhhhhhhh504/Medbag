import mysql.connector

# establish a connection to the database
db = mysql.connector.connect(user = "sqluser", password = "password", host = "localhost", database = "med_bag")

# create a cursor object
cursor = db.cursor()
cart_query = """
CREATE TABLE IF NOT EXISTS CART (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_quantity INT NOT NULL,
    item_price INT NOT NULL,
    drug_id INT NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY (drug_id) REFERENCES drug(drug_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
)
"""
cursor.execute(cart_query)

# Retrieve data from the CART table
select_query = """
SELECT item_quantity, item_price
FROM CART
WHERE customer_id = 1;
"""
cursor.execute(select_query)
results = cursor.fetchall()

# Print the query results
for result in results:
    print(result)


# Retrieve data from the customer table
select_query = """
SELECT customer_name, customer_email
FROM customer;
"""
cursor.execute(select_query)
results = cursor.fetchall()

# Print the query results
for result in results:
    print(result)
db.close()
