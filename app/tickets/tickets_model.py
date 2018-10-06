from app.database.connectDB import DatabaseConnectivity
from flask import flash
import datetime


dbInstance = DatabaseConnectivity()
class Tickets:
    def add_ticket(self,ticket_assigned_to,ticket_opening_time,
        ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
        ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,
        ticket_priority,ticket_site_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """
            INSERT INTO tickets(ticket_assigned_to,ticket_opening_time,
            ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
            ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,
            ticket_priority,ticket_site_id) VALUES(
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cur.execute(sql,(ticket_assigned_to,ticket_opening_time,
            ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
            ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,
            ticket_priority,ticket_site_id))
            conn.commit()
            flash('Ticket Opened Successfully','success')
        except:
            flash('Error submiting the data to database','danger')

    def view_all_tickets(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            # sql = """
            # SELECT ticket_id,ticket_reason,ticket_assigned_to,ticket_client,
            # CASE WHEN TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW())>0 
            # THEN CONCAT('Expired at ','',ticket_overdue_time) ELSE 
            # CONCAT('Expires at ','',ticket_overdue_time) END AS Overdue,
            # CASE WHEN ticket_status='Closed' 
            # THEN CONCAT(ticket_status,' (',ticket_closing_time,')') 
            # WHEN ticket_status='Open' AND TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW())>0 AND TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW())<60 
            # THEN CONCAT('Overdue ','( Late By ',TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW()),' Minutes)') 
            
            # WHEN ticket_status='Open' AND TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW())>59 AND TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW())<1440 
            # THEN CONCAT('Overdue ','( Late By ',TIMESTAMPDIFF(HOUR,ticket_overdue_time,NOW()),' Hours ',TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW())%60, ' Minutes)')

            # WHEN ticket_status='Open' AND TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW())>1439 
            # THEN CONCAT('Overdue ','( Late By ',TIMESTAMPDIFF(DAY,ticket_overdue_time,NOW()),' Days ',TIMESTAMPDIFF(HOUR,ticket_overdue_time,NOW())%24, ' Hours ',TIMESTAMPDIFF(MINUTE,ticket_overdue_time,NOW())%60, ' Minutes)')

            # ELSE ticket_status END AS Ticket, ticket_priority from tickets
            # """

            sql = """
            SELECT ticket_id,ticket_reason,ticket_assigned_to,ticket_client,
            
            CASE WHEN (DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp)) * 60 +
            DATE_PART('minute', now()::timestamp - ticket_overdue_time::timestamp)>0 
            
            THEN CONCAT('Expired at',' ',ticket_overdue_time) 

            WHEN ticket_status='Closed' AND ((DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp)) * 60 +
            DATE_PART('minute', now()::timestamp - ticket_overdue_time::timestamp)<0 OR (DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp)) * 60 +
            DATE_PART('minute', now()::timestamp - ticket_overdue_time::timestamp)>0) 
            
            THEN CONCAT('Would expire at',' ',ticket_overdue_time) 

            ELSE CONCAT('Shall expire at ', ticket_overdue_time) END AS Overdue,
            
            CASE WHEN ticket_status='Closed' 
            THEN CONCAT(ticket_status,' (',ticket_closing_time,')') 
            
            WHEN ticket_status='Open' AND (DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp)) * 60 +
            DATE_PART('minute', now()::timestamp - ticket_overdue_time::timestamp)>0 AND 
            (DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp)) * 60 +
            DATE_PART('minute', now()::timestamp - ticket_overdue_time::timestamp)<60 
            
            THEN CONCAT('Overdue (Late By ',(DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp)) * 60 +
            DATE_PART('minute', now()::timestamp - ticket_overdue_time::timestamp),' Minutes)') 

            WHEN ticket_status='Open' AND (DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp)) * 60 +
            DATE_PART('minute', now()::timestamp - ticket_overdue_time::timestamp)>59 AND 
            (DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp)) * 60 +
            DATE_PART('minute', now()::timestamp - ticket_overdue_time::timestamp)<1440 

            THEN CONCAT('Overdue ','( Late By ',DATE_PART('day', now()::timestamp - ticket_overdue_time::timestamp) * 24 + 
            DATE_PART('hour', now()::timestamp - ticket_overdue_time::timestamp),' Hours)')
            
            ELSE ticket_status END AS Ticket,
            ticket_priority from tickets
            """
            cur.execute(sql)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except:
            flash('Error retrieving tickets from database','danger')

    def edit_ticket(self,ticket_assigned_to,
    ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
    ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,ticket_client_visit_note,
    ticket_priority,ticket_root_cause,
    ticket_action_taken,ticket_pending_reason,ticket_additional_note,ticket_site_id,ticket_closing_time,
    ticket_dispatch_time,ticket_arrival_time,ticket_start_time,ticket_complete_time,ticket_return_time,ticket_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """
            UPDATE tickets SET ticket_assigned_to=%s,
            ticket_status=%s,ticket_overdue_time=%s,ticket_planned_visit_date=%s,ticket_actual_visit_date=%s,
            ticket_client=%s,ticket_po_number=%s,ticket_wo_type=%s,ticket_reason=%s,ticket_client_visit_note=%s,
            ticket_priority=%s,ticket_root_cause=%s,
            ticket_action_taken=%s,ticket_pending_reason=%s,ticket_additional_note=%s,ticket_site_id=%s,ticket_closing_time=%s,
            ticket_dispatch_time=%s,ticket_arrival_time=%s,ticket_start_time=%s,ticket_complete_time=%s,ticket_return_time=%s WHERE ticket_id=%s
            """
            cur.execute(sql,(ticket_assigned_to,
            ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
            ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,ticket_client_visit_note,
            ticket_priority,ticket_root_cause,
            ticket_action_taken,ticket_pending_reason,ticket_additional_note,ticket_site_id,ticket_closing_time,
            ticket_dispatch_time,ticket_arrival_time,ticket_start_time,ticket_complete_time,ticket_return_time,ticket_id))
            conn.commit()
            if ticket_status == "Closed":
                flash('Ticket Closed Successfully','success')
            else:
                flash('Ticket Edited Successfully','success')
        except:
            flash('Error submiting the data to database','danger')


    def delete_a_user(self, user_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute("DELETE FROM users WHERE user_id=%s",[user_id])
            conn.commit()
            flash('User Deleted Successfully','success')
        except:
            flash('Error deleteing user from database','danger')

    def get_ticket_by_Id(self, ticket_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT * FROM tickets WHERE ticket_id=%s"""
            cur.execute(sql,[ticket_id])
            self.theTicket = cur.fetchone()
            return self.theTicket
        except:
            flash('Error retrieving ticket from database','danger')

    def get_ticket_overdue_time_by_Id(self, ticket_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """SELECT ticket_overdue_time FROM tickets WHERE ticket_id=%s"""
            cur.execute(sql,[ticket_id])
            self.theTicket = cur.fetchone()
            return self.theTicket
        except:
            flash('Error retrieving ticket from database','danger')


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

