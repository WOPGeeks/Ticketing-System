import psycopg2
from flask import jsonify

class DatabaseConnectivity:
# Using MySQL Database
    # def connectToDatabase(self):
    #     try:
    #         import MySQLdb
    #         self.conn = MySQLdb.connect(host='localhost', user='root', password='mysql', db='tickets')
    #         print("Connected Successfully")
    #         return self.conn
            
    #     except:
    #         print('Cannot connect to database')
    #         return jsonify({'Message' : 'Cannot connect to database'})

# Using PostgreSQL Database
    def connectToDatabase(self):
        
        try:
            connectionString = "postgres://lhzxcyfuehqwcw:129faa08ef955acc4144bd7bbf2e4e697ca8faa0a4f319fa73ddeb31584fda47@ec2-54-227-241-179.compute-1.amazonaws.com:5432/d6humsp52ioadf"
            # connectionString = "host='localhost' user='postgres' password='password' dbname='tickets' port='5432'"
            self.conn = psycopg2.connect(connectionString)
            print("Connection established")
            return self.conn
            
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)

    def create_tickets_table(self):
        sqlcommandforQuestions =(
            """
            CREATE TABLE IF NOT EXISTS tickets(ticket_id SERIAL PRIMARY KEY, ticket_assigned_to VARCHAR(250),
             ticket_status VARCHAR(250), ticket_opening_time TIMESTAMP,ticket_closing_time TIMESTAMP,ticket_overdue_time TIMESTAMP,
             ticket_client VARCHAR(200), ticket_po_number VARCHAR(200),ticket_wo_type VARCHAR(200),ticket_reason VARCHAR(250),
             ticket_client_visit_note VARCHAR(200),ticket_planned_visit_date DATE,ticket_actual_visit_date DATE,
             ticket_priority VARCHAR(100),ticket_root_cause VARCHAR(250),ticket_action_taken VARCHAR(250),
             ticket_pending_reason VARCHAR(250),ticket_dispatch_time TIME,ticket_arrival_time TIME,ticket_start_time TIME,
             ticket_complete_time TIME,ticket_return_time TIME,ticket_additional_note VARCHAR(250),ticket_site_id VARCHAR(200))
             """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforQuestions)
        self.conn.commit()
    
    
    def create_users_table(self):
        sqlcommandforUsers =(
            """
            DROP TABLE users
            """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforUsers)
        self.conn.commit()
    
    def create_engineers_table(self):
        sqlcommandforQuestions =(
            """
            CREATE TABLE IF NOT EXISTS engineers(engineer_id SERIAL PRIMARY KEY, 
            engineer_first_name VARCHAR(200),engineer_last_name VARCHAR(200),
            engineer_email VARCHAR(200), engineer_phone VARCHAR(100),
            engineer_field_ATM smallint,engineer_field_AIR smallint, 
            engineer_field_TEL smallint,engineer_address VARCHAR(200))
            """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforQuestions)
        self.conn.commit()
    def create_clients_table(self):
        sqlcommandforAnswers =(
            """
            CREATE TABLE IF NOT EXISTS customers(customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(250),
            customer_product VARCHAR(250),
            customer_address VARCHAR(250),
            customer_email VARCHAR(250),
            customer_phone VARCHAR(250))
            """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforAnswers)
        self.conn.commit()

    def create_work_orders_table(self):
        sqlcommandforAnswers =(
            """
            CREATE TABLE IF NOT EXISTS work_orders(work_order_id SERIAL PRIMARY KEY,
            work_order_type VARCHAR(250))
            """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforAnswers)
        self.conn.commit()