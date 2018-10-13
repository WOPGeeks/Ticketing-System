from app.database.connectDB import DatabaseConnectivity
from flask import flash
import psycopg2

dbInstance = DatabaseConnectivity()
class Users:
    def add_user(self,first_name,last_name,email,address,user_phone,username,password,
    user_can_add_user,user_can_delete_user,user_can_edit_user,user_can_edit_his_info,
    user_can_open_tickets,user_can_edit_tickets,user_can_delete_tickets,user_can_view_all_tickets,
    user_can_view_his_tickets,user_can_edit_his_tickets,user_can_view_his_tasks,user_can_view_all_tasks,
    user_can_view_his_reports,user_can_view_all_reports,user_can_add_delete_edit_client,
    user_can_add_delete_edit_engineer,user_can_add_delete_edit_equipment,user_can_add_delete_edit_workorder):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql ="""
            INSERT INTO users(user_first_name,user_last_name,user_email,user_address,user_phone,user_name,user_password,
            user_can_add_user,user_can_delete_user,user_can_edit_user,user_can_edit_his_info,
            user_can_open_tickets,user_can_edit_tickets,user_can_delete_tickets,user_can_view_all_tickets,
            user_can_view_his_tickets,user_can_edit_his_tickets,user_can_view_his_tasks,user_can_view_all_tasks,
            user_can_view_his_reports,user_can_view_all_reports,user_can_add_delete_edit_client_info,
            user_can_add_delete_edit_engineer_info,user_can_add_delete_edit_equipment_info,user_can_add_delete_edit_workorder_info) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cur.execute(sql,
            (first_name,last_name,email,address,user_phone,username,password,
            user_can_add_user,user_can_delete_user,user_can_edit_user,user_can_edit_his_info,
            user_can_open_tickets,user_can_edit_tickets,user_can_delete_tickets,user_can_view_all_tickets,
            user_can_view_his_tickets,user_can_edit_his_tickets,user_can_view_his_tasks,user_can_view_all_tasks,
            user_can_view_his_reports,user_can_view_all_reports,user_can_add_delete_edit_client,
            user_can_add_delete_edit_engineer,user_can_add_delete_edit_equipment,user_can_add_delete_edit_workorder))
            conn.commit()
            flash('User {} Added Successfully'.format(first_name),'success')
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)

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
    def edit_a_user(self, user_id,user_first_name, user_last_name,user_email,user_phone,user_address,user_name,user_password,
    user_can_add_user,user_can_delete_user,user_can_edit_user,user_can_edit_his_info,
    user_can_open_tickets,user_can_edit_tickets,user_can_delete_tickets,user_can_view_all_tickets,
    user_can_view_his_tickets,user_can_edit_his_tickets,user_can_view_his_tasks,user_can_view_all_tasks,
    user_can_view_his_reports,user_can_view_all_reports,user_can_add_delete_edit_client,
    user_can_add_delete_edit_engineer,user_can_add_delete_edit_equipment,user_can_add_delete_edit_workorder):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql ="""
            UPDATE users SET user_first_name=%s, user_last_name=%s,user_email=%s,user_phone=%s,user_address=%s,user_name=%s,user_password=%s,
            user_can_add_user=%s,user_can_delete_user=%s,user_can_edit_user=%s,user_can_edit_his_info=%s,
            user_can_open_tickets=%s,user_can_edit_tickets=%s,user_can_delete_tickets=%s,user_can_view_all_tickets=%s,
            user_can_view_his_tickets=%s,user_can_edit_his_tickets=%s,user_can_view_his_tasks=%s,user_can_view_all_tasks=%s,
            user_can_view_his_reports=%s,user_can_view_all_reports=%s,user_can_add_delete_edit_client_info=%s,
            user_can_add_delete_edit_engineer_info=%s,user_can_add_delete_edit_equipment_info=%s,user_can_add_delete_edit_workorder_info=%s WHERE user_id=%s
            """
            cur.execute(sql,[user_first_name, user_last_name,user_email,user_phone,user_address,user_name,user_password,
            user_can_add_user,user_can_delete_user,user_can_edit_user,user_can_edit_his_info,
            user_can_open_tickets,user_can_edit_tickets,user_can_delete_tickets,user_can_view_all_tickets,
            user_can_view_his_tickets,user_can_edit_his_tickets,user_can_view_his_tasks,user_can_view_all_tasks,
            user_can_view_his_reports,user_can_view_all_reports,user_can_add_delete_edit_client,
            user_can_add_delete_edit_engineer,user_can_add_delete_edit_equipment,user_can_add_delete_edit_workorder,user_id])
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

    def checkUserRights(self, current_user):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT * FROM users WHERE user_name=%s"""
            cur.execute(sql,[current_user])
            self.theUser = cur.fetchone()
            return self.theUser
        except:
            flash('Error retrieving the user from database','danger')


