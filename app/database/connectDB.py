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
        connectionString = "dbname='d2q82jh8ooum09' user='nbdhugbosrnhca' password='8e782659b6c340b9ddcf207c6928ee721ea755173af11facf95349c3b768da08' host='ec2-174-129-18-98.compute-1.amazonaws.com' port='5432'"
        try:
            self.conn = psycopg2.connect(connectionString)
            print("Connection established")
            return self.conn
            
        except:
            print('Cannot connect to database')
            return jsonify({'Message' : 'Cannot connect to database'})
        

    def create_tickets_table(self):
        sqlcommandforQuestions =(
            """
            CREATE TABLE IF NOT EXISTS tickets(question_id INT PRIMARY KEY, question_title VARCHAR(250),
             question_body VARCHAR(250), question_author VARCHAR(100),
              question_ask_date TIMESTAMP)
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
              user_name VARCHAR(250),user_email VARCHAR(250), user_password VARCHAR(100), user_phone VARCHAR(250), user_status smallint DEFAULT 0, user_address VARCHAR(250))
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