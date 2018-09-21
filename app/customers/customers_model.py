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

    def get_all_clients(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("SELECT * FROM customers")
            self.theClients = cur.fetchall()
            return self.theClients
        except:
            flash('Error retrieving clients from database','danger')

    def get_no_client(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT * FROM customers WHERE customer_id IS NULL"""
            cur.execute(sql)
            self.theUsers = cur.fetchall()
            return self.theUsers
        except:
            flash('Error retrieving users from database','danger')
    def delete_a_client(self, client_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("DELETE FROM customers WHERE customer_id=%s",[client_id])
            conn.commit()
            flash('Client Deleted Successfully','success')
        except:
            flash('Error deleteing client from database','danger')
    def edit_a_client(self, client_id,customer_name, customer_product,customer_address,customer_phone,customer_email):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql ="UPDATE customers SET customer_name=%s, customer_product=%s,customer_address=%s,customer_phone=%s,customer_email=%s WHERE customer_id=%s"
            cur.execute(sql,[customer_name, customer_product,customer_address,customer_phone,customer_email,client_id])
            conn.commit()
            flash('Client Edited Successfully','success')
        except:
            flash('Error editing the Client from database','danger')

    def get_client_by_Id(self, client_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT * FROM customers WHERE customer_id=%s"""
            cur.execute(sql,[client_id])
            self.theClient = cur.fetchone()
            return self.theClient
        except:
            flash('Error retrieving the Client from database','danger')
