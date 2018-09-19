from app.database.connectDB import DatabaseConnectivity
from flask import flash

dbInstance = DatabaseConnectivity()
class Engineers:
    def add_engineer(self,engineer_first_name,engineer_last_name,engineer_phone,engineer_email,engineer_address,engineer_field_ATM,engineer_field_AIR,engineer_field_TEL):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("INSERT INTO engineers(engineer_first_name,engineer_last_name,engineer_phone,engineer_email,engineer_address,engineer_field_ATM,engineer_field_AIR,engineer_field_TEL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(engineer_first_name,engineer_last_name,engineer_phone,engineer_email,engineer_address,engineer_field_ATM,engineer_field_AIR,engineer_field_TEL))
            conn.commit()
            flash('Engineer Added Successfully','success')
        except:
            flash('Error saving engineer to database','danger')