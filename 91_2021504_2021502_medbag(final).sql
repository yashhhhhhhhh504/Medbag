CREATE DATABASE IF NOT EXISTS med_bag;
USE med_bag;
CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_email VARCHAR(255) NOT NULL,
    customer_gender CHAR(255) NOT NULL,
    customer_phone BIGINT NOT NULL, 
    customer_address VARCHAR(255) NOT NULL,
    customer_zipcode INT NOT NULL,
    customer_street VARCHAR(255) NOT NULL,
    customer_city VARCHAR(255) NOT NULL,
    customer_state VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    employee_address VARCHAR(255) NOT NULL,
    employee_zipcode BIGINT NOT NULL,
    employee_phone BIGINT NOT NULL,
    employee_email VARCHAR(255) NOT NULL,
    employee_Salary DECIMAL(10,2) NOT NULL,
    employee_street VARCHAR(255) NOT NULL,
    employee_city VARCHAR(255) NOT NULL,
    employee_state VARCHAR(255) NOT NULL,
    employee_position VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS membership (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    membership_type VARCHAR(255) NOT NULL,
    customer_id INT NOT NULL,
    discount_percentage DECIMAL(5,2) NOT NULL,
    membership_startdate DATE NOT NULL,
    membership_enddate DATE NOT NULL,
    
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
CREATE TABLE IF NOT EXISTS drug (
    drug_id INT AUTO_INCREMENT PRIMARY KEY,
    drug_name VARCHAR(255) NOT NULL,
    drug_manufacturer VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Stock(
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    stock_quantity INT NOT NULL,
    drug_id INT NOT NULL,
    batch_id INT NOT NULL,
    price INT NOT NULL,
    date_expiry DATE NOT NULL,
    FOREIGN KEY (drug_id) REFERENCES drug(drug_id)
);

CREATE TABLE IF NOT EXISTS orders_med (
order_id INT AUTO_INCREMENT PRIMARY KEY,
order_date DATE NOT NULL,
order_price INT NOT NULL,
customer_id INT NOT NULL,
drug_id INT NOT NULL,
FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
FOREIGN KEY (drug_id) REFERENCES drug(drug_id)
ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS CART (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_quantity INT NOT NULL,
    item_price INT NOT NULL,
    drug_id INT NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY (drug_id) REFERENCES drug(drug_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
CREATE TABLE IF NOT EXISTS CART_MEDICINE (
    cart_id INT NOT NULL,
    medicine_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (cart_id, medicine_name),
    FOREIGN KEY (cart_id) REFERENCES CART(item_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Bill(
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    bill_date DATE NOT NULL,
    bill_price INT NOT NULL,
    bill_payment VARCHAR(255) NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
CREATE TABLE IF NOT EXISTS wallet (
    wallet_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    wallet_amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);



