from app.database.connectDB import DatabaseConnectivity
from flask import flash

dbInstance = DatabaseConnectivity()
class Customers:
    def add_client(self,customer_name,customer_phone,customer_email,customer_address,customer_product):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("INSERT INTO customers(customer_name,customer_phone,customer_email,customer_address,customer_product) VALUES(%s,%s,%s,%s,%s)",(customer_name,customer_phone,customer_email,customer_address,customer_product))
            conn.commit()
            flash('Client Added Successfully','success')
        except:
            flash('Error saving client to database','danger')