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
            flash('Engineer {} Added Successfully'.format(engineer_first_name),'success')
        except:
            flash('Error saving engineer to database','danger')
    
    def get_all_engineers(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("SELECT * FROM engineers")
            self.theengineers = cur.fetchall()
            return self.theengineers
        except:
            flash('Error retrieving engineers from database','danger')

    def get_no_engineer(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT * FROM engineers WHERE engineer_id IS NULL"""
            cur.execute(sql)
            self.theEngineer = cur.fetchall()
            return self.theEngineer
        except:
            flash('Error retrieving users from database','danger')
    def delete_a_engineer(self, engineer_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("DELETE FROM engineers WHERE engineer_id=%s",[engineer_id])
            conn.commit()
            flash('Engineer Deleted Successfully','success')
        except:
            flash('Error deleteing engineer from database','danger')
    def edit_an_engineer(self, engineer_id,engineer_first_name,engineer_last_name,engineer_address,engineer_phone,engineer_email,engineer_field_ATM,engineer_field_AIR,engineer_field_TEL):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql ="UPDATE engineers SET engineer_first_name=%s, engineer_last_name=%s,engineer_address=%s,engineer_phone=%s,engineer_email=%s,engineer_field_ATM=%s,engineer_field_AIR=%s,engineer_field_TEL=%s WHERE engineer_id=%s"
            cur.execute(sql,[engineer_first_name,engineer_last_name,engineer_address,engineer_phone,engineer_email,engineer_field_ATM,engineer_field_AIR,engineer_field_TEL,engineer_id])
            conn.commit()
            flash('Engineer Edited Successfully','success')
        except:
            flash('Error editing the engineer from database','danger')

    def get_engineer_by_Id(self, engineer_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT * FROM engineers WHERE engineer_id=%s"""
            cur.execute(sql,[engineer_id])
            self.theengineer = cur.fetchone()
            return self.theengineer
        except:
            flash('Error retrieving the engineer from database','danger')