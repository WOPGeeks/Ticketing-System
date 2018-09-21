from app.database.connectDB import DatabaseConnectivity
from flask import flash


dbInstance = DatabaseConnectivity()
class WorkOrders:
    def add_work_order(self,work_order_type):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("INSERT INTO work_orders(work_order_type) VALUES(%s)",[work_order_type])
            conn.commit()
            flash('Work Order Added Successfully','success')
        except:
            flash('Error submiting the data to database','danger')

    def view_all_work_orders(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT work_order_type, work_order_id FROM work_orders"""
            cur.execute(sql)
            self.theUsers = cur.fetchall()
            return self.theUsers
        except:
            flash('Error retrieving work orders from database','danger')

    def delete_a_work_order(self, work_order_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("DELETE FROM work_orders WHERE work_order_id=%s",[work_order_id])
            conn.commit()
            flash('Work Order Deleted Successfully','success')
        except:
            flash('Error deleteing user from database','danger')
    def edit_a_work_order(self, work_order_id, work_order_type):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql ="UPDATE work_orders SET work_order_type=%s WHERE work_order_id=%s"
            cur.execute(sql,[work_order_type, work_order_id])
            conn.commit()
            flash('Work Order Type Edited Successfully','success')
        except:
            flash('Error deleteing work order type from database','danger')

    def get_work_order_by_Id(self, work_order_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT work_order_type, work_order_id FROM work_orders WHERE work_order_id=%s"""
            cur.execute(sql,[work_order_id])
            self.theOrder = cur.fetchone()
            return self.theOrder
        except:
            flash('Error retrieving the work order from database','danger')
