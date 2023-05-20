import mysql.connector
#connecting to the database
db = mysql.connector.connect(user = "sqluser", password = "password", host = "localhost", database = "med_bag")
cursor = db.cursor()
if db.is_connected():
    print("Connected to MySQL database")
else: 
    print("Connection failed")
#super admin login
admin_username = "admin"
admin_password = "admin"
# CLI interface
while True:
    print("Welcome to the MedBag")
    print("1. Admin login")
    print("2. Customer login")
    print("3. run custom queries")
    print("4. exit")
    choice = int(input("Enter your choice: "))
    if choice==1: 
        print("Admin login")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == admin_username and password == admin_password:
            print("Welcome Admin" )
            print("What all actions would you like to perform?")
            print("1.   Generate data (randomly genrated data for testing)")
            print("2.   add new employee")
            print("3.   add new customer")
            print("4.   add new membership")
            print("5.   Upgrade the customer membership")
            print("6.   Add a new product to the database")
            print("7.   Remove the product from the database")
            print("8.   view purchases")
            print("9.   update stocks")
            print("10.  view stocks for certain product")

            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                import datagen
            elif choice2 == 2:
                #add new employee
                print("Enter employee ID: ")
                emp_id = int(input())
                print("Enter employee name: ")
                emp_name = input()
                print("Enter employee address: ")
                emp_address = input()
                print("Enter employee zipcode: ")
                emp_zipcode = input()
                print("Enter street: ")
                emp_street = input()
                print("Enter city: ")
                emp_city = input()
                print("Enter state: ")
                emp_state = input()
                print("Enter employee phone: ")
                emp_phone = input()
                print("Enter employee email: ")
                emp_email = input()
                print("Enter employee position: ")
                emp_position = input()
                print("Enter employee salary: ")
                emp_salary = input()
                cursor.execute("INSERT INTO employee (employee_id, employee_name, employee_address, employee_zipcode, employee_street, employee_city, employee_state, employee_phone, employee_email, employee_position, employee_salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (emp_id, emp_name, emp_address, emp_zipcode, emp_street, emp_city, emp_state, emp_phone, emp_email, emp_position, emp_salary))
                db.commit()
                if cursor.rowcount == 1:
                    print("Employee added successfully")
                else: 
                    print("Employee addition failed")
                
            elif choice2 == 3:
                #adding customers at the database
                print("Enter customer ID: ")
                cust_id = int(input())
                print("Enter customer name: ")
                cust_name = input()
                print("Enter phone number: ")
                cust_phone = input()
                print("Enter customer email: ")
                cust_email = input()
                print("Enter customer Gender: ")
                cust_gender = input()
                print("Enter customer address: ")
                cust_address = input()
                print("Enter customer zipcode: ")
                cust_zipcode = input()
                print("Enter street: ")
                cust_street = input()
                print("Enter city: ")
                cust_city = input()
                print("Enter state: ")
                cust_state = input()
                #adding the data to database
                cursor.execute("INSERT INTO customer (customer_name, customer_email, customer_gender, customer_phone, customer_address, customer_zipcode, customer_street, customer_city, customer_state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(cust_name, cust_email, cust_gender, cust_phone, cust_address, cust_zipcode, cust_street, cust_city, cust_state))
                if cursor.rowcount==1: 
                    print("Customer data entered sucessfully")
                else: 
                    print("Error in adding data")
            if choice2 ==4: 
                print("Enter customer id which is needed to be upgraded")
                cust_id = int(input())
                membership_type = input("Enter membership type: ")
                discount_percentage = float(input("Enter discount percentage: "))
                membership_startdate = input("Enter membership start date (YYYY-MM-DD): ")
                membership_enddate = input("Enter membership end date (YYYY-MM-DD): ")
                sql = "INSERT INTO membership (membership_type, customer_id, discount_percentage, membership_startdate, membership_enddate) VALUES (%s, %s, %s, %s, %s)"
                val = (membership_type, cust_id, discount_percentage, membership_startdate, membership_enddate)
                cursor.execute(sql, val)
                db.commit()
            if choice2 ==5: 
                #upgrade the customer membership
                print("Enter customer id which is needed to be upgraded")
                cust_id = int(input())
                membership_type = input("Enter membership type: ")
                discount_percentage = float(input("Enter discount percentage: "))
                membership_startdate = input("Enter membership start date (YYYY-MM-DD): ")
                membership_enddate = input("Enter membership enddate (YYYY-MM-DD): ")
                sql = "UPDATE membership SET membership_type = %s, discount_percentage = %s, membership_startdate = %s, membership_enddate = %s WHERE customer_id = %s"
                val = (membership_type, discount_percentage, membership_startdate, membership_enddate, cust_id)
                cursor.execute(sql, val)
                db.commit()
                print("Membership upgraded successfully")
            if choice2 ==6:
                drug_name = input("Enter drug name: ")
                drug_manufacturer = input("Enter drug manufacturer: ")
                stock_quantity = int(input("Enter stock quantity: "))
                batch_id = int(input("Enter batch ID: "))
                price = int(input("Enter drug price: "))
                date_expiry = input("Enter expiry date (yyyy-mm-dd): ")
                # insert new drug into drug table
                sql = "INSERT INTO drug (drug_name, drug_manufacturer) VALUES (%s, %s)"
                val = (drug_name, drug_manufacturer)
                cursor.execute(sql, val)
                db.commit()
                # retrieve drug ID for the new drug
                drug_id = cursor.lastrowid
                # insert new drug into stock table
                sql = "INSERT INTO stock (stock_quantity, drug_id, batch_id, price, date_expiry) VALUES (%s, %s, %s, %s, %s)"
                val = (stock_quantity, drug_id, batch_id, price, date_expiry)
                cursor.execute(sql, val)
                db.commit()
                print("New drug added successfully!")
            if choice2 == 7:
                # create a cursor object to execute SQL queries
                mycursor = db.cursor()
                # get the drug ID to delete from the user
                drug_id = input("Enter the drug ID to delete: ")
                
                try:
                    # delete the corresponding rows from the cart table first
                    cart_delete_query = "DELETE FROM cart WHERE drug_id = %s"
                    cart_delete_val = (drug_id,)
                    mycursor.execute(cart_delete_query, cart_delete_val)
                    db.commit()
                    
                    # delete the corresponding rows from the stock table
                    stock_delete_query = "DELETE FROM stock WHERE drug_id = %s"
                    stock_delete_val = (drug_id,)
                    mycursor.execute(stock_delete_query, stock_delete_val)
                    db.commit()
                    
                    # delete the row from the drug table
                    drug_delete_query = "DELETE FROM drug WHERE drug_id = %s"
                    drug_delete_val = (drug_id,)
                    mycursor.execute(drug_delete_query, drug_delete_val)
                    db.commit()
                    
                    print("Drug deleted successfully!")
                except mysql.connector.errors.IntegrityError as e:
                    print("Error: ", e)
                    print("Cannot delete drug as it has related records in the stock table.")
            if choice2 ==8:
                cursor.execute("SELECT * FROM orders_med")
                result = cursor.fetchall()
                for row in result:
                    print(row)
            if choice2==9: 
                #update the stocks for the drugs
                print("Enter drug id which is needed to be updated")
                drug_id = int(input())
                stock_quantity = int(input("Enter stock quantity: "))
                batch_id = int(input("Enter batch ID: "))
                price = int(input("Enter drug price: "))
                date_expiry = input("Enter expiry date (yyyy-mm-dd): ")
                sql = "UPDATE stock SET stock_quantity = %s, batch_id = %s, price = %s, date_expiry = %s WHERE drug_id = %s"
                val = (stock_quantity, batch_id, price, date_expiry, drug_id)
                cursor.execute(sql, val)
                db.commit()
                print("Stock updated successfully")

            if choice2 ==10:
                #view the stocks for the drugs by entering the drug id with proper heading
                print("Enter drug id which is needed to be viewed")
                drug_id = int(input())
                cursor.execute("SELECT * FROM stock WHERE drug_id = %s", (drug_id,))
                result = cursor.fetchall()
                for row in result:
                    print("Drug ID: ", row[0], "Stock Quantity: ", row[1], "Batch ID: ", row[2], "Price: ", row[3], "Expiry Date: ", row[4])    
        else: 
            print("Invalid username or password")


    if choice == 2:
        #login
        print("1. Sign-up")
        print("2. login")
        cus = int(input())
        if cus==1: 
            print("Please provide the following information to sign up:")
            name = input("Name: ")
            email = input("Email: ")
            gender = input("Gender: ")
            phone = input("Phone number: ")
            address = input("Address: ")
            zipcode = input("Zipcode: ")
            street = input("Street: ")
            city = input("City: ")
            state = input("State: ")
            # insert user information into database
            sql = "INSERT INTO customer (customer_name, customer_email, customer_gender, customer_phone, customer_address, customer_zipcode, customer_street, customer_city, customer_state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name, email, gender, phone, address, zipcode, street, city, state)
            cursor.execute(sql, val)
            db.commit()
            print("do you wish to continue ? (y/n)")
            choice100 = input()
            if choice100 == 'y':
                continue
            else:
                break

        if cus==2:
            print("Enter your name") 
            name = input()
            print("Enter your email")
            email = input()
            #compare the mail and name from database and if it is present then proceed to the next step
            cursor.execute("SELECT * FROM customer WHERE customer_name = %s AND customer_email = %s", (name, email))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Invalid username or email")
                continue
            else: 
                print("Welcome ", name)
                print("1.   View all drugs")
                print("2.   Search drugs")
                print("3.   Add to cart")
                print("4.   View cart")
                print("5.   Delete from cart")
                print("6.   Add money to the wallet")
                print("7.   View orders")
                print("8.   update membership") 
                print("9.   View wallet")
                print("10.  Checkout")
                print("11.  Exit")
                choice3 = int(input("Enter your choice: "))
                if choice3 == 1:
                    #showcasing all the drugs
                    cursor.execute("SELECT * FROM drug")
                    result = cursor.fetchall()
                    for row in result:
                        print("Drug name: ", row[1], "Drug manufacturer: ", row[2],"price: ", row[3])
                if choice3 == 2:
                #searching the drugs by name
                    print("Enter the drug name")
                    drug_name = input()
                    cursor.execute("SELECT * FROM drug WHERE drug_name = %s", (drug_name,))
                    result = cursor.fetchall()
                    for row in result:
                        print("Drug name: ", row[1], "Drug manufacturer: ", row[2],"price: ", row[3])
                if choice3 == 3:
                    #adding the drugs to the cart with checking if the drug is available or not
                    print("Enter the drug name")
                    drug_name = input()
                    print("Enter the quantity")
                    quantity = int(input())
                    cursor.execute("SELECT * FROM drug WHERE drug_name = %s", (drug_name,))
                    result = cursor.fetchall()
                    for row in result:
                        drug_id = row[0]
                        price = row[3]
                        total = quantity * price
                        print("Drug name: ", row[1], "Drug manufacturer: ", row[2],"price: ", row[3])
                    sql = "INSERT INTO cart (customer_id, drug_id, quantity, total) VALUES (%s, %s, %s, %s)"
                    val = (cust_id, drug_id, quantity, total)
                    cursor.execute(sql, val)
                    db.commit()
                    print("Added to cart successfully!")
                if choice3 == 4:
                    #viewing the cart
                    cursor.execute("SELECT * FROM cart")
                    result = cursor.fetchall()
                    for row in result:
                        print("Drug name: ", row[1], "Drug manufacturer: ", row[2],"price: ", row[3])
                    #print the total price 
                    cursor.execute("SELECT SUM(total) FROM cart")
                    result = cursor.fetchall()
                    for row in result:
                        print("Total: ", row[0])
                if choice3 == 5:
                    #deleting the drugs from the cart
                    print("Enter the drug name")
                    drug_name = input()
                    cursor.execute("SELECT * FROM drug WHERE drug_name = %s", (drug_name,))
                    result = cursor.fetchall()
                    for row in result:
                        drug_id = row[0]
                    cursor.execute("DELETE FROM cart WHERE drug_id = %s", (drug_id,))
                    db.commit()
                    print("Deleted from cart successfully!")
                if choice3 == 6:
                    customer_name = input("Enter customer name: ")
                    # Query to get customer ID
                    cursor.execute("SELECT customer_id FROM customer WHERE customer_name=%s", (customer_name,))
                    result = cursor.fetchone()
                    if not result:
                        print("Customer not found")
                    customer_id = result[0]
                    # Get new wallet amount from user input
                    wallet_amount = float(input("Enter new wallet amount: "))
                    # Update wallet amount in database
                    cursor.execute("UPDATE wallet SET wallet_amount=%s WHERE customer_id=%s", (wallet_amount, customer_id))
                    db.commit()
                    print("Wallet amount updated successfully")
                                
                if choice3 == 7:
                    #viewing the orders
                    print("Enter the customer name")
                    customer_name = input()
                    cursor.execute("SELECT * FROM customer WHERE customer_name = %s", (customer_name,))
                    result = cursor.fetchall()
                    for row in result:
                        customer_id = row[0]
                    cursor.execute("SELECT * FROM orders WHERE customer_id = %s", (customer_id,))
                    result = cursor.fetchall()
                    for row in result:
                        print("Order ID: ", row[0], "Customer ID: ", row[1], "Order Date: ", row[2], "Order Status: ", row[3])
                if choice3 == 8:
                    #updating the membership
                    print("Enter the customer name")
                    customer_name = input()
                    cursor.execute("SELECT * FROM customer WHERE customer_name = %s", (customer_name,))
                    result = cursor.fetchall()
                    for row in result:
                        customer_id = row[0]
                    print("Enter the membership type")
                    membership_type = input()
                    type= {"Gold":100,"Silver":50,"Platinum":150}
                    if membership_type in type:
                        #check if the price for the membership is available in the wallet
                        cursor.execute("SELECT wallet_amount FROM wallet WHERE customer_id=%s", (customer_id,))
                        result = cursor.fetchone()
                        if not result:
                            print("Customer not found")
                        wallet_amount = result[0]
                        if wallet_amount >= type[membership_type]:
                            #substrat the amount as well based on the type of membership
                            wallet_amount = wallet_amount - type[membership_type]
                            cursor.execute("UPDATE customer SET membership_type=%s WHERE customer_id=%s", (membership_type, customer_id))
                            db.commit()
                            print("Membership updated successfully")
                    else:
                        #in case the person has not registered for membership 
                        print("which membership you want to register")
                        #print the type of membership
                        print("Gold")
                        print("Silver")
                        print("Platinum")
                        membership_type = input()
                        type= {"Gold":100,"Silver":50,"Platinum":150}
                        if membership_type in type:
                            #check if the price for the membership is available in the wallet
                            cursor.execute("SELECT wallet_amount FROM wallet WHERE customer_id=%s", (customer_id,))
                            result = cursor.fetchone()
                            if not result:
                                print("Customer not found")
                            wallet_amount = result[0]
                            if wallet_amount >= type[membership_type]:
                                #substrat the amount as well based on the type of membership
                                wallet_amount = wallet_amount - type[membership_type]
                                cursor.execute("UPDATE customer SET membership_type=%s WHERE customer_id=%s", (membership_type, customer_id))
                                db.commit()
                                print("Membership updated successfully")

                if choice3 == 9:
                    #printing out the bill 
                    print("Enter the customer name")
                    customer_name = input()
                    cursor.execute("SELECT * FROM customer WHERE customer_name = %s", (customer_name,))
                    result = cursor.fetchall()
                    for row in result:
                        customer_id = row[0]
                    cursor.execute("SELECT * FROM cart")
                    result = cursor.fetchall()
                    for row in result:
                        print("Drug name: ", row[1], "Drug manufacturer: ", row[2],"price: ", row[3])
                    #print the total price
                    cursor.execute("SELECT SUM(total) FROM cart")   
                    result = cursor.fetchall()
                    for row in result:
                        print("Total: ", row[0])
                    #inserting the order details into the orders table
                    cursor.execute("SELECT * FROM cart")
                    result = cursor.fetchall()
                    for row in result:
                        drug_id = row[1]
                        quantity = row[2]
                        total = row[3]
                        sql = "INSERT INTO orders (customer_id, drug_id, quantity, total) VALUES (%s, %s, %s, %s)"
                        val = (customer_id, drug_id, quantity, total)
                        cursor.execute(sql, val)
                        db.commit()
                    #delete the cart details
                    cursor.execute("DELETE FROM cart")
                    db.commit()
                    print("Order placed successfully!")
                if choice3 == 10:
                    #checking out and printing the bill 
                    print("Enter the customer name")
                    customer_name = input()
                    cursor.execute("SELECT * FROM customer WHERE customer_name = %s", (customer_name,))
                    result = cursor.fetchall()
                    for row in result:
                        customer_id = row[0]
                    cursor.execute("SELECT * FROM cart")
                    result = cursor.fetchall()
                    for row in result:
                        print("Drug name: ", row[1], "Drug manufacturer: ", row[2],"price: ", row[3])
                    #print the total price
                    cursor.execute("SELECT SUM(total) FROM cart")
                    result = cursor.fetchall()
                    for row in result:
                        print("Total: ", row[0])
                    #inserting the order details into the orders table
                    cursor.execute("SELECT * FROM cart")
                    result = cursor.fetchall()
                    for row in result:
                        drug_id = row[1]
                        quantity = row[2]
                        total = row[3]
                        sql = "INSERT INTO orders (customer_id, drug_id, quantity, total) VALUES (%s, %s, %s, %s)"
                        val = (customer_id, drug_id, quantity, total)
                        cursor.execute(sql, val)
                        db.commit()
                    #delete the cart details
                    cursor.execute("DELETE FROM cart")
                    db.commit()
                    print("Order placed successfully!")
                    #exit the program
                if choice3 == 11:
                    break
    if choice == 3: 
        print("Which type of query do you want to perform?")
        print("1. run 4 transation queries")
        print("2. run 4 non conflicting queries")
        print("3. Run olap queries")
        print("4. Run embedded queries")
        print("5. Run triggers ")
        print("6. Transations with  two schedules which are conflict serializable and non-conflict serializable")
        print("7. Exit")
        choice4 = int(input())
        if choice4 == 1:
            try:
                # Start transaction 1: Add a new drug to the database
                cursor.execute("START TRANSACTION")
                add_drug_query = "INSERT INTO drug (drug_name, drug_manufacturer) VALUES (%s, %s)"
                add_drug_val = ("Aspirin", "Bayer")
                cursor.execute(add_drug_query, add_drug_val)
                db.commit()
                print("Transaction 1 completed successfully")
                #viewing the transaction
                cursor.execute("SELECT * FROM drug")
                result = cursor.fetchall()
                for row in result:
                    print(row)
            except:
                db.rollback()
                print("Transaction 1 failed \n ")

            try:
                # Start transaction 2: Update the stock of a drug in the database
                cursor.execute("START TRANSACTION")
                update_stock_query = "UPDATE stock SET stock_quantity = stock_quantity + %s WHERE drug_id = %s"
                update_stock_val = (50, 1)
                cursor.execute(update_stock_query, update_stock_val)
                db.commit()
                print("Transaction 2 completed successfully")
                #viewing the change 
                cursor.execute("SELECT * FROM stock")
                result = cursor.fetchall()
                for row in result:
                    print("Drug ID: ", row[1], " Stock Quantity: ", row[0])

            except Exception as e:
                db.rollback()
                #printing the error 
                print(e)

            try:
                # Start transaction 5: Update stock quantity and price for a particular drug
                cursor.execute("START TRANSACTION")
                
                # Get the drug_id, batch_id, and new values for stock quantity and price from the user
                drug_id = input("Enter the drug ID: ")
                batch_id = input("Enter the batch ID: ")
                stock_quantity = input("Enter the new stock quantity: ")
                price = input("Enter the new price: ")
                
                # Update the stock table with the new values
                stock_update_query = "UPDATE stock SET stock_quantity = %s, price = %s WHERE drug_id = %s AND batch_id = %s"
                stock_update_val = (stock_quantity, price, drug_id, batch_id)
                cursor.execute(stock_update_query, stock_update_val)
                db.commit()
                print("Transaction 3 completed successfully")
                
            except:
                db.rollback()
                print("Transaction 3 failed")
            try:
                # Start transaction 1: Add a new drug to the database
                cursor.execute("START TRANSACTION")
                drug_insert_query = "INSERT INTO drug (drug_name, drug_manufacturer) VALUES (%s, %s)"
                drug_insert_val = ("Ibuprofen", "Advil")
                cursor.execute(drug_insert_query, drug_insert_val)
                # Start transaction 2: Add a new stock of the drug to the database
                stock_insert_query = "INSERT INTO Stock (stock_quantity, drug_id, batch_id, price, date_expiry) VALUES (%s, %s, %s, %s, %s)"
                stock_insert_val = (100, cursor.lastrowid, 1, 10, "2023-04-30")
                cursor.execute(stock_insert_query, stock_insert_val)
                # Commit both transactions
                db.commit()
                print("Both transactions completed successfully")
            except:
                # Rollback both transactions in case of any errors
                db.rollback()
                print(" transactions 4 failed")
        if choice4== 2: 
            try:
                # Start transaction 1: Add 100 units to stock for drug with ID 1
                cursor.execute("START TRANSACTION")
                stock_query = "UPDATE stock SET stock_quantity = stock_quantity + 100 WHERE drug_id = %s AND batch_id = %s"
                stock_val = (1, 123)
                cursor.execute(stock_query, stock_val)
                db.commit()
                print("Transaction 1 completed successfully")
            except:
                db.rollback()
                print("Transaction 1 failed")
            try:
                # Start transaction 2: Reduce stock by 50 units for drug with ID 1
                cursor.execute("START TRANSACTION")
                stock_query = "UPDATE stock SET stock_quantity = stock_quantity - 50 WHERE drug_id = %s AND batch_id = %s"
                stock_val = (1, 123)
                cursor.execute(stock_query, stock_val)
                db.commit()
                print("Transaction 2 completed successfully")
            except:
                db.rollback()
                print("Transaction 2 failed")
        if choice4 ==3: 
            #running the olap query of olap file 
            import olap 
        if choice4 ==4:
            #running the embedded query of embedded file 
            import query    
        if choice4 ==5:
            #importing and runnioing the trigger file
            import triggers
        if choice4 ==6:
            try:
                cursor = db.cursor()
                cursor.execute("START TRANSACTION")
                # Insert new customer into the database
                customer_insert_query = "INSERT INTO customer (customer_name, customer_email, customer_gender, customer_phone, customer_address, customer_zipcode, customer_street, customer_city, customer_state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                customer_insert_val = ("John Doe", "johndoe@gmail.com", "M", 1234567890, "123 Main St", 12345, "Main St", "Anytown", "CA")
                cursor.execute(customer_insert_query, customer_insert_val)
                customer_id = cursor.lastrowid
                # Update customer's wallet with 100
                wallet_insert_query = "INSERT INTO wallet (customer_id, wallet_amount) VALUES (%s, %s)"
                wallet_insert_val = (customer_id, 100)
                cursor.execute(wallet_insert_query, wallet_insert_val)
                # Commit transaction 1
                db.commit()
                print("Transaction 1 completed successfully")
            except:
                # Rollback transaction 1 in case of any errors
                db.rollback()
                print("Transaction 1 failed")
            # Start transaction 2: Place an order for a drug and update the stock quantity
            try:
                cursor.execute("START TRANSACTION")
                # Insert new order into the database
                order_insert_query = "INSERT INTO orders_med (order_date, order_price, customer_id, drug_id) VALUES (%s, %s, %s, %s)"
                order_insert_val = ("2023-04-23", 50, customer_id, 1)
                cursor.execute(order_insert_query, order_insert_val)
                # Update stock quantity
                stock_update_query = "UPDATE Stock SET stock_quantity = stock_quantity - %s WHERE drug_id = %s"
                stock_update_val = (10, 1)
                cursor.execute(stock_update_query, stock_update_val)
                # Commit transaction 2
                db.commit()
                print("Transaction 2 completed successfully")
            except:
                # Rollback transaction 2 in case of any errors
                db.rollback()
                print("Transaction 2 failed")
        # Schedule 1: T1 followed by T2
            try: 
                cursor.execute("START TRANSACTION")
                # Execute T1
                customer_insert_query = "INSERT INTO customer (customer_name, customer_email, customer_gender, customer_phone, customer_address, customer_zipcode, customer_street, customer_city, customer_state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                customer_insert_val = ("Jane Smith", "janesmith@gmail.com", "F", 9876543210, "456 Main St", 54321, "Main St", "Anytown", "CA")
                cursor.execute(customer_insert_query, customer_insert_val)
                customer_id = cursor.lastrowid
                wallet_insert_query = "INSERT INTO wallet (customer_id, wallet_amount) VALUES (%s, %s)"
                wallet_insert_val = (customer_id, 200)
                cursor.execute(wallet_insert_query, wallet_insert_val)
                # Execute T2
                order_insert_query = "INSERT INTO orders_med (order_date, order_price, customer_id, drug_id) VALUES (%s, %s, %s, %s)"
                order_insert_val = ("2023-04-23", 50, customer_id, 1)
                cursor.execute(order_insert_query, order_insert_val)
                stock_update_query = "UPDATE Stock SET stock_quantity = stock_quantity - %s WHERE drug_id = %s"
                stock_update_val = (10, 1)
                cursor.execute(stock_update_query, stock_update_val)
                # Commit both transactions
                db.commit()
                print("Both transactions completed successfully")
            except:
                # Rollback both transactions in case of any errors
                db.rollback()
                print("Both transactions failed")
            # Schedule 2: T2 followed by T1
            try:
                cursor.execute("START TRANSACTION")
                # Execute T2
                order_insert_query = "INSERT INTO orders_med (order_date, order_price, customer_id, drug_id) VALUES (%s, %s, %s, %s)"
                order_insert_val = ("2023-04-23", 50, customer_id, 1)
                cursor.execute(order_insert_query, order_insert_val)
                stock_update_query = "UPDATE Stock SET stock_quantity = stock_quantity - %s WHERE drug_id = %s"
                stock_update_val = (10, 1)
                cursor.execute(stock_update_query, stock_update_val)
                # Execute T1
                order_insert_query = "INSERT INTO orders_med (order_date, order_price, customer_id, drug_id) VALUES (%s, %s, %s, %s)"
                order_insert_val = ("2023-04-23", 50, customer_id, 1)
                cursor.execute(order_insert_query, order_insert_val)
                wallet_insert_query = "INSERT INTO wallet (customer_id, wallet_amount) VALUES (%s, %s)"
                wallet_insert_val = (customer_id, 200)
                cursor.execute(wallet_insert_query, wallet_insert_val)
                # Commit both transactions
                db.commit()
                print("Both transactions completed successfully")
            except:
                # Rollback both transactions in case of any errors
                db.rollback()
                print("Both transactions failed")
        if choice4 ==7:
            break; 

                    
 
            


        
        
        
        
        


            
            


        

        
    


