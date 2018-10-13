from app.database.connectDB import DatabaseConnectivity
from flask import flash

dbInstance = DatabaseConnectivity()
class Equipments():
    def add_equipment(self,equipment_serial,equipment_serial_id,equipment_model,equipment_class,
        equipment_type,equipment_category,equipment_resolution,equipment_response,equipment_installation_date,
        equipment_installation_address,equipment_installation_city,equipment_supplier):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """
            INSERT INTO equipments
            (equipment_serial_number,equipment_serial_id,equipment_class,equipment_model,equipment_category,
            equipment_type,equipment_resolution,equipment_response,equipment_installation_date,equipment_address,
            equipment_city,equipment_supplier) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cur.execute(sql,(equipment_serial,equipment_serial_id,equipment_model,equipment_class,
            equipment_type,equipment_category,equipment_resolution,
            equipment_response,equipment_installation_date,
            equipment_installation_address,equipment_installation_city,equipment_supplier))
            conn.commit()
            flash('Equipment Added Successfully','success')
        except Exception as e:
            print(e)
            flash('Error saving equipment to database','danger')
    