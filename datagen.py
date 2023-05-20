import mysql.connector
import random
from faker import Faker
fake = Faker()
def generate_random_customer(cursor,mydb):
    for i in range(100): 
        customer_name = fake.name()
        customer_email = fake.email()
        customer_gender = fake.random_element(elements=('M', 'F', 'O'))
        customer_phone = fake.random_int(min=1000000000, max=9999999999)
        customer_address = fake.secondary_address()
        customer_zipcode = fake.zipcode()
        customer_street = "Main Street"
        customer_city = "Delhi"
        customer_state = "Delhi"
        query = "INSERT INTO customer (customer_name, customer_email, customer_gender, customer_phone, customer_address, customer_zipcode, customer_street, customer_city, customer_state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (customer_name, customer_email, customer_gender, customer_phone, customer_address, customer_zipcode, customer_street, customer_city, customer_state)
        cursor.execute(query, values)
        mydb.commit()
def generate_random_employee(cursor,mydb):
    job_titles = ["cleaner", "cashier", "storage manager", "store manager", "stock maintainer"]
    indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    for i in range(100):
        employee_name = fake.name()
        employee_address = fake.address()
        employee_zipcode = fake.zipcode()
        employee_phone = fake.random_int(min=1000000000, max=9999999999)
        employee_email = fake.email()
        employee_Salary = fake.pydecimal(left_digits=5, right_digits=2, positive=True)
        employee_street = "Main Street"
        employee_city = "DELHI"
        employee_state = random.choice(indian_states)
        employee_position = random.choice(job_titles)
        query = "INSERT INTO employee (employee_name, employee_address, employee_zipcode, employee_phone, employee_email, employee_Salary, employee_street, employee_city, employee_state, employee_position) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (employee_name, employee_address, employee_zipcode, employee_phone, employee_email, employee_Salary, employee_street, employee_city, employee_state, employee_position)
        cursor.execute(query, values)
        mydb.commit()
def generate_random_medicine(cursor,mydb):
    drug_names = ["Lipitor", "Nexium", "Plavix", "Advair Diskus", "Abilify", "Humira", "Crestor", "Epogen", "Rituxan", "Enbrel","Zoloft", "Prozac", "Wellbutrin", "Lexapro", "Paxil", "Effexor", "Celexa", "Cymbalta", "Zyprexa", "Seroquel","Lamictal", "Neurontin", "Lyrica", "Topamax", "Keppra", "Depakote", "Tegretol", "Dilantin", "Luminal", "Fioricet","Synthroid", "Levoxyl", "Armour Thyroid", "Cytomel", "Levothroid", "Tirosint", "Euthyrox", "Unithroid", "Synthroid 125mcg", "Eltroxin","Norvasc", "Lasix", "Cozaar", "Zestril", "Diovan", "Altace", "Tenormin", "Coreg", "Lopressor", "Inderal","Nasonex", "Flonase", "Singulair", "Claritin", "Zyrtec", "Allegra", "Pataday", "Optivar", "Astelin", "Dymista","Lantus", "Humalog", "Novolog", "Levemir", "Apidra", "Tresiba", "Toujeo", "Fiasp", "Afrezza", "Basaglar","Xarelto", "Eliquis", "Pradaxa", "Savaysa", "Lovenox", "Fragmin", "Arixtra", "Coumadin", "Heparin", "Argatroban","Ambien", "Lunesta", "Sonata", "Rozerem", "Belsomra", "Intermezzo", "Edluar", "Zolpimist", "Halcion", "Restoril","Celebrex", "Mobic", "Naprosyn", "Relafen", "Indocin", "Arthrotec", "Voltaren", "Feldene", "Cataflam", "Clinoril"]
    manufacturers = ["Pfizer", "AstraZeneca", "Merck", "GlaxoSmithKline", "Bristol-Myers Squibb", "AbbVie", "Amgen", "Novartis", "Roche", "Eli Lilly","Sanofi", "Johnson & Johnson", "Abbott Laboratories", "Boehringer Ingelheim", "Bayer", "Gilead Sciences", "Genentech", "Teva Pharmaceutical", "Sandoz", "Mylan","Abbott", "Actavis", "Aurobindo Pharma", "Baxter International", "Biogen Idec", "Celgene", "Cipla", "Daiichi Sankyo", "Dr. Reddy's Laboratories", "Eisai","Fresenius", "Glenmark Pharmaceuticals", "Hikma Pharmaceuticals", "Intas Pharmaceuticals", "Ipca Laboratories", "Jubilant Life Sciences", "Lupin Limited", "Menarini", "Mitsubishi Tanabe Pharma", "Mylan","Nichi-Iko Pharmaceutical", "Nippon Chemiphar", "Novo Nordisk", "Otsuka Pharmaceutical", "Perrigo", "Purdue Pharma", "Ranbaxy Laboratories", "Sankyo", "Sawai Pharmaceutical", "Solvay","Sun Pharmaceutical", "Takeda Pharmaceutical", "Taro Pharmaceuticals", "Torrent Pharmaceuticals", "UCB", "Valeant Pharmaceuticals", "Zydus Cadila", "Dabur", "Himalaya Herbals", "Charak Pharma","Baidyanath", "Patanjali Ayurved", "Hamdard Laboratories", "Dey's Medical", "Forest Laboratories", "Schering-Plough", "Abbott India", "Unichem Laboratories", "Cadila Healthcare", "Laurus Labs","Ajanta Pharma", "Alkem Laboratories", "Emcure Pharmaceuticals", "Sun Pharma Advanced Research", "Alembic Pharmaceuticals", "Biocon", "Torrent Research Centre", "Biocon Biologics", "Laurus Bio", "Wockhardt","Divi's Laboratories", "Natco Pharma", "Astron Research", "Neuland Laboratories", "Jubilant Generics", "Sequent Scientific", "Indoco Remedies", "Laurus Synthesis", "Gufic Biosciences", "Caplin Point Laboratories"]
    for i in range(100): 
        drug_name = random.choice(drug_names)
        drug_manufacturer = random.choice(manufacturers)
        sql = "INSERT INTO drug (drug_name, drug_manufacturer) VALUES (%s, %s)"
        val = (drug_name, drug_manufacturer)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")
        stock_quantity = random.randint(10, 100)
        batch_id = random.randint(1000, 9999)
        price = random.randint(1, 1000)
        year = random.randint(2023, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date_expiry = f"{year}-{month}-{day}"
        drug_id = cursor.lastrowid
        sql = "INSERT INTO Stock (stock_quantity, drug_id, batch_id, price, date_expiry) VALUES (%s, %s, %s, %s, %s)"
        val = (stock_quantity, drug_id, batch_id, price, date_expiry)
        cursor.execute(sql, val)
        mydb.commit()
def generate_random_membership(cursor,mydb): 
    membership_types = {"Gold": 0.10,"Silver": 0.05,"Platinum": 0.20}
    query = "SELECT customer_id FROM customer"
    cursor.execute(query)
    customer_ids = [row[0] for row in cursor.fetchall()]
    for i in range(100):
        membership_type, discount_percentage = random.choice(list(membership_types.items()))
        customer_id = random.choice(customer_ids)
        year = random.randint(2023, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        membership_startdate = f"{year}-{month}-{day}"
        membership_enddate = f"{year+1}-{month}-{day}"
        sql = "INSERT INTO membership (membership_type, customer_id, discount_percentage, membership_startdate, membership_enddate) VALUES (%s, %s, %s, %s, %s)"
        val = (membership_type, customer_id, discount_percentage, membership_startdate, membership_enddate)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")
def generate_random_order(cursor,mydb):
    query = "SELECT customer_id FROM customer"
    cursor.execute(query)
    customer_ids = [row[0] for row in cursor.fetchall()]
    query = "SELECT drug_id FROM drug"
    cursor.execute(query)
    drug_ids = [row[0] for row in cursor.fetchall()]
    for i in range (100):
        order_date = f"{random.randint(2000, 2023)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        order_price = random.randint(100, 1000)
        customer_id = random.choice(customer_ids)
        drug_id = random.choice(drug_ids)
        query = "INSERT INTO orders_med (order_date, order_price, customer_id, drug_id) VALUES (%s, %s, %s, %s)"
        values = (order_date, order_price, customer_id, drug_id)
        cursor.execute(query, values)
        mydb.commit()
def generate_random_bill(cursor,mydb):
    query = "SELECT customer_id FROM customer"
    cursor.execute(query)
    customer_ids = [row[0] for row in cursor.fetchall()]
    for i in range (100):
        bill_date = f"{random.randint(2000, 2023)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        bill_price = random.randint(100, 1000)
        bill_payment = random.choice(["Cash", "Credit Card", "Debit Card"])
        customer_id = random.choice(customer_ids)
        query = "INSERT INTO Bill (bill_date, bill_price, bill_payment, customer_id) VALUES (%s, %s, %s, %s)"
        values = (bill_date, bill_price, bill_payment, customer_id)
        cursor.execute(query, values)
        mydb.commit()
def generate_random_cart(cursor,mydb):
    query = "SELECT customer_id FROM customer"
    cursor.execute(query)
    customer_ids = [row[0] for row in cursor.fetchall()]
    query = "SELECT drug_id FROM drug"
    cursor.execute(query)
    drug_ids= [row[0] for row in cursor.fetchall()]
    for i in range (100):
        item_quantity = random.randint(1, 10)
        item_price = random.randint(100, 1000)
        customer_id = random.choice(customer_ids)
        drug_id = random.choice(drug_ids)
        query = "INSERT INTO CART (item_quantity, item_price, customer_id, drug_id) VALUES (%s, %s, %s, %s)"
        values = (item_quantity, item_price, customer_id, drug_id)
        cursor.execute(query, values)
        cart_id = cursor.lastrowid
        medicine_name = f"Medicine_{random.randint(1, 5)}"
        query = "INSERT INTO CART_MEDICINE (cart_id, medicine_name) VALUES (%s, %s)"
        values = (cart_id, medicine_name)
        cursor.execute(query, values)
        mydb.commit()
def insert_wallet(cursor,mydb):
    query = "SELECT customer_id FROM customer"
    cursor.execute(query)
    customer_ids = [row[0] for row in cursor.fetchall()]
    for i in range (100):
        wallet_amount = random.randint(100, 10000)
        customer_id = random.choice(customer_ids)
        query = "INSERT INTO WALLET (wallet_amount, customer_id) VALUES (%s, %s)"
        values = (wallet_amount, customer_id)
        cursor.execute(query, values)
        mydb.commit()
    
mydb = mysql.connector.connect(user = "sqluser", password = "password", host = "localhost", database = "med_bag")
cursor = mydb.cursor()
if mydb.is_connected():
    print("Connected to MySQL database")
else:
    print("Connection failed")
print("Entering the data for the customer\n")
generate_random_customer(cursor,mydb)
print("Data entered successfully\n")
print("Entering the data for the employee\n")
generate_random_employee(cursor,mydb)
print("Data entered successfully\n")
print("Entering the data for the medicine\n")
generate_random_medicine(cursor,mydb)
print("Data entered successfully\n")
print("Entering the data for the membership\n")
generate_random_membership(cursor,mydb)
print("Data entered successfully\n")
print("Entering the data for the cart\n")
generate_random_cart(cursor,mydb)
print("Data entered successfully\n")
print("Entering the data for the bill\n")
generate_random_bill(cursor,mydb)
print("Data entered successfully\n")
print("Entering the data for the order\n")
generate_random_order(cursor,mydb)
print("Data entered successfully\n")
print("Entering the data for the value wallet\n")
insert_wallet(cursor,mydb)
print("Data entered successfully\n")
# show the tables in the database
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)
