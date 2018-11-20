import psycopg2
from flask import jsonify

class DatabaseConnectivity:
# Using MySQL Database
    def connectToDatabase(self):
        try:
            import MySQLdb
            self.conn = MySQLdb.connect(host='localhost', user='root', password='walter123@Andela!', db='tickets')
            print("Connected Successfully")
            return self.conn
            
        except:
            print('Cannot connect to database')
            return jsonify({'Message' : 'Cannot connect to database'})

# Using PostgreSQL Database
    # def connectToDatabase(self):
        
    #     try:
    #         # connectionString = "postgres://xbkhddyykiqqtj:47bb54868364989b09ade3295411d8cf0371913acfed1784c5481d09480b4fa3@ec2-23-23-153-145.compute-1.amazonaws.com:5432/d965p4umfcab6f"
            
    #         connectionString = "host='localhost' user='postgres' password='password' dbname='tickets' port='5432'"
    #         self.conn = psycopg2.connect(connectionString)
    #         print("Connection established")
    #         return self.conn
            
    #     except(Exception, psycopg2.DatabaseError) as e:
    #         print(e)

    def create_tickets_table(self):
        sqlcommandforQuestions =(
            """
            CREATE TABLE IF NOT EXISTS tickets(ticket_id SERIAL PRIMARY KEY, ticket_assigned_to VARCHAR(250),
             ticket_status VARCHAR(250), ticket_opening_time TIMESTAMP,ticket_closing_time TIMESTAMP,ticket_overdue_time TIMESTAMP,
             ticket_client VARCHAR(200), ticket_po_number VARCHAR(200),ticket_wo_type VARCHAR(200),ticket_reason VARCHAR(250),
             ticket_client_visit_note VARCHAR(200),ticket_planned_visit_date DATE,ticket_actual_visit_date DATE,
             ticket_priority VARCHAR(100),ticket_root_cause VARCHAR(250),ticket_action_taken VARCHAR(250),
             ticket_pending_reason VARCHAR(250),ticket_dispatch_time TIME,ticket_arrival_time TIME,ticket_start_time TIME,
             ticket_complete_time TIME,ticket_return_time TIME,ticket_additional_note VARCHAR(250),ticket_site_id VARCHAR(200),username VARCHAR(100),
             ticket_type smallint, ticket_part_used VARCHAR(100),ticket_revisited VARCHAR(100), ticket_part_returned VARCHAR(100))
             """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforQuestions)
        self.conn.commit()
    
    
    def create_users_table(self):
        sqlcommandforUsers =(
            """
            CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, user_first_name VARCHAR(250), user_last_name VARCHAR(250),
            user_name VARCHAR(250),user_email VARCHAR(250), user_password VARCHAR(100), user_phone VARCHAR(250), user_status smallint DEFAULT 0, user_address VARCHAR(250),
            user_can_add_user smallint DEFAULT 0,user_can_delete_user smallint DEFAULT 0,user_can_edit_user smallint DEFAULT 0,
            user_can_edit_his_info smallint DEFAULT 0,user_can_open_tickets smallint DEFAULT 0,user_can_edit_tickets smallint DEFAULT 0,
            user_can_delete_tickets smallint DEFAULT 0,user_can_view_his_tickets smallint DEFAULT 0,
            user_can_view_all_tickets smallint DEFAULT 0,user_can_edit_his_tickets smallint DEFAULT 0,
            user_can_view_his_tasks smallint DEFAULT 0,user_can_view_all_tasks smallint DEFAULT 0,
            user_can_view_all_reports smallint DEFAULT 0,user_can_view_his_reports smallint DEFAULT 0,
            user_can_add_delete_edit_client_info smallint DEFAULT 0,user_can_add_delete_edit_engineer_info smallint DEFAULT 0,
            user_can_add_delete_edit_equipment_info smallint DEFAULT 0,user_can_add_delete_edit_workorder_info smallint DEFAULT 0,
            user_photo BYTEA)
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

    def create_equipments_table(self):
        sqlcommandforEquipments =(
            """
            CREATE TABLE IF NOT EXISTS equipments(equipment_serial_number VARCHAR(100), 
            equipment_serial_id VARCHAR(200),equipment_class VARCHAR(200),
            equipment_model VARCHAR(200), equipment_category VARCHAR(100),
            equipment_type VARCHAR(200), 
            equipment_response decimal(12,2),equipment_resolution decimal(12,2),equipment_installation_date DATE,
            equipment_address VARCHAR(200),equipment_city VARCHAR(200),equipment_supplier VARCHAR(200))
            """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforEquipments)
        self.conn.commit()

    def create_clients_table(self):
        sqlcommandforAnswers =(
            """
            CREATE TABLE IF NOT EXISTS customers(customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(250),
            customer_product VARCHAR(250),
            customer_address VARCHAR(250),
            customer_email VARCHAR(250),
            customer_phone VARCHAR(250),
            customer_contact_person VARCHAR(200),
            customer_contact_person_phone VARCHAR(200))
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

    def drop_equipment_table(self):
        sqlcommandforAnswers =(
            """
            DROP TABLE tickets
            """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforAnswers)
        self.conn.commit()
    