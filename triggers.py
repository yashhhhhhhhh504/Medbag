import mysql.connector
db = mysql.connector.connect(user = "sqluser", password = "password", host = "localhost", database = "med_bag")
cursor = db.cursor()
print("Eexcuting trigger 1\n")
query = '''
CREATE TRIGGER check_membership_discount
BEFORE INSERT ON membership
FOR EACH ROW
BEGIN
    IF NEW.discount_percentage > 0.5 THEN
        SET NEW.discount_percentage = 0.5;
    END IF;
END;
'''
cursor.execute(query)
print("Trigger 1 executed\n")
print("Executing trigger 2\n")
# create trigger to enforce minimum stock quantity
query = '''
CREATE TRIGGER enforce_min_stock
BEFORE INSERT ON Stock
FOR EACH ROW
BEGIN
  IF NEW.stock_quantity < 10 THEN
    SIGNAL SQLSTATE '45000' 
      SET MESSAGE_TEXT = 'Stock quantity cannot be less than 10';
  END IF;
END;
'''
cursor.execute(query)
print("Trigger 2 executed\n")