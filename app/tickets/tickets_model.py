from app.database.connectDB import DatabaseConnectivity
from flask import flash
import datetime
import psycopg2

dbInstance = DatabaseConnectivity()
class Tickets:
    def add_ticket(self,ticket_assigned_to,ticket_opening_time,
        ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
        ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,
        ticket_priority,username,ticket_type,ticket_site_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """
            INSERT INTO tickets(ticket_assigned_to,ticket_opening_time,
            ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
            ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,
            ticket_priority,username,ticket_type,ticket_site_id) VALUES(
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cur.execute(sql,(ticket_assigned_to,ticket_opening_time,
            ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
            ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,
            ticket_priority,username,ticket_type,ticket_site_id))
            conn.commit()
            flash('Ticket Opened Successfully','success')
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error submiting the data to database','danger')
    def sqlStatment(self):
            # self.sql = """
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

            # ELSE ticket_status END AS Ticket, ticket_priority, CASE WHEN ticket_type=1 THEN 'ATM Ticket' WHEN ticket_type=2 THEN 'Airport Ticket' WHEN ticket_type=3 THEN 'Telecom Ticket' WHEN ticket_type=4 
            # THEN 'Fleet Ticket' ELSE 'Unknown Ticket' END AS ticket_types from tickets
            # """

            self.sql = """
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
            ticket_priority, CASE WHEN ticket_type=1 THEN 'ATM Ticket' WHEN ticket_type=2 THEN 'Airport Ticket' WHEN ticket_type=3 THEN 'Telecom Ticket' WHEN ticket_type=4 THEN 'Fleet Ticket' ELSE 'Unknown Ticket' END AS ticket_types from tickets
            """
            return self.sql



    def view_all_tickets(self):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            finalSQL = theSql + " ORDER BY ticket_id DESC"
            cur.execute(finalSQL)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except:
            flash('Error retrieving tickets from database','danger')


    def view_all_my_tickets(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            cur.execute(theSql+' Where ticket_priority is not null ORDER BY ticket_id DESC')
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')




    def view_all_closed_tickets(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')
    def view_all_my_closed_tickets(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')

    def view_all_open_tickets(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')
    def view_all_my_open_tickets(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')

    def view_all_tickets_due_in_2_hours(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')

    def view_all_my_tickets_due_in_2_hours(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')
    def view_all_tickets_due_in_1_hour(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')
    
    def view_all_my_tickets_due_in_1_hour(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')

    def view_all_overdue_tickets(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')
    def view_all_low_priority_tickets(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')

    def view_all_my_overdue_tickets(self,current_user):
        try:
            # import MySQLdb
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')
    def view_all_my_low_priority_tickets(self,current_user):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            theSql = Tickets().sqlStatment()
            theWhere = " Where ticket_status is not null ORDER BY ticket_id DESC"
            cur.execute(theSql+theWhere)
            self.theTickets = cur.fetchall()
            return self.theTickets
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            flash('Error retrieving my tickets from database','danger')


    def edit_ticket(self,ticket_assigned_to,
    ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
    ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,ticket_client_visit_note,
    ticket_priority,ticket_root_cause,
    ticket_action_taken,ticket_pending_reason,ticket_additional_note,ticket_site_id,ticket_closing_time,
    ticket_dispatch_time,ticket_arrival_time,ticket_start_time,ticket_complete_time,ticket_return_time,ticket_type,ticket_id):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            sql = """
            UPDATE tickets SET ticket_assigned_to=%s,
            ticket_status=%s,ticket_overdue_time=%s,ticket_planned_visit_date=%s,ticket_actual_visit_date=%s,
            ticket_client=%s,ticket_po_number=%s,ticket_wo_type=%s,ticket_reason=%s,ticket_client_visit_note=%s,
            ticket_priority=%s,ticket_root_cause=%s,
            ticket_action_taken=%s,ticket_pending_reason=%s,ticket_additional_note=%s,ticket_site_id=%s,ticket_closing_time=%s,
            ticket_dispatch_time=%s,ticket_arrival_time=%s,ticket_start_time=%s,ticket_complete_time=%s,ticket_return_time=%s,ticket_type=%s WHERE ticket_id=%s
            """
            cur.execute(sql,(ticket_assigned_to,
            ticket_status,ticket_overdue_time,ticket_planned_visit_date,ticket_actual_visit_date,
            ticket_client,ticket_po_number,ticket_wo_type,ticket_reason,ticket_client_visit_note,
            ticket_priority,ticket_root_cause,
            ticket_action_taken,ticket_pending_reason,ticket_additional_note,ticket_site_id,ticket_closing_time,
            ticket_dispatch_time,ticket_arrival_time,ticket_start_time,ticket_complete_time,ticket_return_time,ticket_type,ticket_id))
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
    
    def general_function(self, sql):
        try:
            conn = dbInstance.connectToDatabase()
            cur = conn.cursor()
            cur.execute(sql)
            self.theTypes = cur.fetchall()
            return self.theTypes
        except:
            flash('Error retrieving customers from database','danger')

    def get_ATM_running_tasks(self):
        self.ticket_counts = Tickets().general_function("SELECT COUNT(*) FROM tickets WHERE ticket_dispatch_time IS NOT NULL AND ticket_complete_time IS NULL AND ticket_type=1")
        return self.ticket_counts
    def get_Airport_running_tasks(self):
        self.ticket_counts = Tickets().general_function("SELECT COUNT(*) FROM tickets WHERE ticket_dispatch_time IS NOT NULL AND ticket_complete_time IS NULL AND ticket_type=2")
        return self.ticket_counts
    def get_Telecom_running_tasks(self):
        self.ticket_counts = Tickets().general_function("SELECT COUNT(*) FROM tickets WHERE ticket_dispatch_time IS NOT NULL AND ticket_complete_time IS NULL AND ticket_type=3")
        return self.ticket_counts
    def get_Fleet_running_tasks(self):
        self.ticket_counts = Tickets().general_function("SELECT COUNT(*) FROM tickets WHERE ticket_dispatch_time IS NOT NULL AND ticket_complete_time IS NULL AND ticket_type=4")
        return self.ticket_counts

    def get_ATM_completed_tasks(self):
        self.ticket_counts = Tickets().general_function("SELECT COUNT(*) FROM tickets WHERE ticket_dispatch_time IS NOT NULL AND ticket_complete_time IS NOT NULL AND ticket_type=1")
        return self.ticket_counts
    def get_Airport_completed_tasks(self):
        self.ticket_counts = Tickets().general_function("SELECT COUNT(*) FROM tickets WHERE ticket_dispatch_time IS NOT NULL AND ticket_complete_time IS NOT NULL AND ticket_type=2")
        return self.ticket_counts
    def get_Telecom_completed_tasks(self):
        self.ticket_counts = Tickets().general_function("SELECT COUNT(*) FROM tickets WHERE ticket_dispatch_time IS NOT NULL AND ticket_complete_time IS NOT NULL AND ticket_type=3")
        return self.ticket_counts
    def get_Fleet_completed_tasks(self):
        self.ticket_counts = Tickets().general_function("SELECT COUNT(*) FROM tickets WHERE ticket_dispatch_time IS NOT NULL AND ticket_complete_time IS NOT NULL AND ticket_type=4")
        return self.ticket_counts

    def setOverdueSQL(self):
        self.sql = "SELECT COUNT(*) FROM tickets WHERE DATE_PART('hour', ticket_overdue_time::timestamp - now()::timestamp)<1 AND DATE_PART('hour', ticket_overdue_time::timestamp - now()::timestamp)>0 AND"
        # self.sql = "SELECT COUNT(*) FROM tickets WHERE TIMESTAMPDIFF(HOUR,ticket_overdue_time,NOW())<1 AND TIMESTAMPDIFF(HOUR,ticket_overdue_time,NOW())>0 AND"
        return self.sql

    def setDisrespectedSQL(self):
        self.sql = "SELECT COUNT(*) FROM tickets WHERE DATE_PART('hour', ticket_overdue_time::timestamp - now()::timestamp)<0 AND ticket_complete_time IS NULL AND"
        # self.sql = "SELECT COUNT(*) FROM tickets WHERE TIMESTAMPDIFF(HOUR,ticket_overdue_time,NOW())>0 AND ticket_complete_time IS NULL AND"
        return self.sql

    def get_ATM_due_soon_tasks(self):
        sql = Tickets().setOverdueSQL()
        finalSQL =sql + " ticket_type=1"
        self.ticket_counts = Tickets().general_function(finalSQL)
        return self.ticket_counts
    def get_Airport_due_soon_tasks(self):
        sql = Tickets().setOverdueSQL()
        finalSQL =sql + " ticket_type=2"
        self.ticket_counts = Tickets().general_function(finalSQL)
        return self.ticket_counts
    def get_Telecom_due_soon_tasks(self):
        sql = Tickets().setOverdueSQL()
        finalSQL =sql + " ticket_type=3"
        self.ticket_counts = Tickets().general_function(finalSQL)
        return self.ticket_counts
    def get_Fleet_due_soon_tasks(self):
        sql = Tickets().setOverdueSQL()
        finalSQL =sql + " ticket_type=4"
        self.ticket_counts = Tickets().general_function(finalSQL)
        return self.ticket_counts


    def get_ATM_overdue_tasks(self):
        sql = Tickets().setDisrespectedSQL()
        finalSQL =sql + " ticket_type=1"
        print(finalSQL)
        self.ticket_counts = Tickets().general_function(finalSQL)
        return self.ticket_counts
    def get_Airport_overdue_tasks(self):
        sql = Tickets().setDisrespectedSQL()
        finalSQL =sql + " ticket_type=2"
        self.ticket_counts = Tickets().general_function(finalSQL)
        return self.ticket_counts
    def get_Telecom_overdue_tasks(self):
        sql = Tickets().setDisrespectedSQL()
        finalSQL =sql + " ticket_type=3"
        self.ticket_counts = Tickets().general_function(finalSQL)
        return self.ticket_counts
    def get_Fleet_overdue_tasks(self):
        sql = Tickets().setDisrespectedSQL()
        finalSQL =sql + " ticket_type=4"
        self.ticket_counts = Tickets().general_function(finalSQL)
        return self.ticket_counts


    def get_tickets_for_reports(self):
        self.ticket_counts = Tickets().general_function("""
        SELECT ticket_id,ticket_po_number,ticket_status,
        ticket_opening_time,ticket_site_id,ticket_client,
        CASE WHEN ticket_type=1 THEN 'ATM Product' WHEN ticket_type=2
        THEN 'Airport Product' WHEN ticket_type=3 THEN 'Telecom Product'
        WHEN ticket_type=4 THEN 'Fleet Product' ELSE 'Unknown Product' 
        END AS ticket_types,ticket_reason,ticket_root_cause,ticket_assigned_to,
        ticket_dispatch_time,ticket_arrival_time,ticket_start_time,ticket_complete_time,
        ticket_return_time FROM tickets ORDER BY ticket_opening_time DESC""")
        return self.ticket_counts