from app.database.connectDB import DatabaseConnectivity
from flask import flash

dbInstance = DatabaseConnectivity()
class Users:
    def add_user(self,first_name,last_name,email,address,user_phone,username,password):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("INSERT INTO users(user_first_name,user_last_name,user_email,user_address,user_phone,user_name,user_password) VALUES(%s,%s,%s,%s,%s,%s,%s)",(first_name,last_name,email,address,user_phone,username,password))
            conn.commit()
            flash('User Added Successfully','success')
        except:
            flash('Error submiting the data to database','danger')