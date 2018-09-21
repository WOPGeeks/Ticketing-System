from app.database.connectDB import DatabaseConnectivity
from flask import flash


dbInstance = DatabaseConnectivity()
class Tickets:
    def add_user(self,first_name,last_name,email,address,user_phone,username,password):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("INSERT INTO users(user_first_name,user_last_name,user_email,user_address,user_phone,user_name,user_password) VALUES(%s,%s,%s,%s,%s,%s,%s)",(first_name,last_name,email,address,user_phone,username,password))
            conn.commit()
            flash('User Added Successfully','success')
        except:
            flash('Error submiting the data to database','danger')

    def view_all_users(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT user_first_name,user_last_name,user_email,user_name,
            CASE WHEN user_status =1 THEN 'Admin' WHEN user_status=0 THEN 'Ordinary' ELSE 'Unknown' END AS Status,user_id FROM users
            """
            cur.execute(sql)
            self.theUsers = cur.fetchall()
            return self.theUsers
        except:
            flash('Error retrieving users from database','danger')

    def view_all_admin_users(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT user_first_name,user_last_name,user_email,user_name,
            CASE WHEN user_status =1 THEN 'Admin' WHEN user_status=0 THEN 'Ordinary' ELSE 'Unknown' END AS Status, user_id FROM users WHERE user_status=1
            """
            cur.execute(sql)
            self.theUsers = cur.fetchall()
            return self.theUsers
        except:
            flash('Error retrieving users from database','danger')
    def view_all_ordinary_users(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT user_first_name,user_last_name,user_email,user_name,
            CASE WHEN user_status =1 THEN 'Admin' WHEN user_status=0 THEN 'Ordinary' ELSE 'Unknown' END AS Status,user_id FROM users WHERE user_status=0
            """
            cur.execute(sql)
            self.theUsers = cur.fetchall()
            return self.theUsers
        except:
            flash('Error retrieving users from database','danger')

    def get_no_user(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT * FROM users WHERE user_id IS NULL"""
            cur.execute(sql)
            self.theUsers = cur.fetchall()
            return self.theUsers
        except:
            flash('Error retrieving users from database','danger')
    def delete_a_user(self, user_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("DELETE FROM users WHERE user_id=%s",[user_id])
            conn.commit()
            flash('User Deleted Successfully','success')
        except:
            flash('Error deleteing user from database','danger')
    def edit_a_user(self, user_id,user_first_name, user_last_name,user_email,user_phone,user_address,user_name,user_password):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql ="UPDATE users SET user_first_name=%s, user_last_name=%s,user_email=%s,user_phone=%s,user_address=%s,user_name=%s,user_password=%s WHERE user_id=%s"
            cur.execute(sql,[user_first_name, user_last_name,user_email,user_phone,user_address,user_name,user_password,user_id])
            conn.commit()
            flash('User Edited Successfully','success')
        except:
            flash('Error deleteing user from database','danger')

    def get_user_by_Id(self, user_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT * FROM users WHERE user_id=%s"""
            cur.execute(sql,[user_id])
            self.theUser = cur.fetchone()
            return self.theUser
        except:
            flash('Error retrieving user from database','danger')

    def get_work_order_types(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT work_order_type FROM work_orders"""
            cur.execute(sql)
            self.theTypes = cur.fetchall()
            return self.theTypes
        except:
            flash('Error retrieving work order types from database','danger')

    def get_engineers(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT CONCAT(engineer_first_name, ' ', engineer_last_name) FROM engineers"""
            cur.execute(sql)
            self.theTypes = cur.fetchall()
            return self.theTypes
        except:
            flash('Error retrieving engineers from database','danger')

    def get_clients(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT customer_name FROM customers"""
            cur.execute(sql)
            self.theTypes = cur.fetchall()
            return self.theTypes
        except:
            flash('Error retrieving customers from database','danger')

