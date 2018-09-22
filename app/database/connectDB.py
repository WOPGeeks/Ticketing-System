import psycopg2

class DatabaseConnectivity:
    # def connectToDatabase(self):
    #     import MySQLdb
    #     self.conn = MySQLdb.connect(db='tickets', user='postgres', password='mysql', host='localhost')
    #     return self.conn

    def connectToDatabase(self):

# Using PostgreSQL Database

        connectionString = "dbname='dvongibre1dlc' user='icnkxihfghzzbr' password='36fcebf5fe408a4816adef83c47233bb31bcd2436a6f0715322c04c783c82805' host='ec2-54-83-27-165.compute-1.amazonaws.com' port='5432'"
        try:
            self.conn = psycopg2.connect(connectionString)
            print("Connection established")
            return self.conn
            
        except:
            print('Cannot connect to database')
            return jsonify({'Message' : 'Cannot connect to database'})


# Using MySQL Database    
        # try:
        #     import MySQLdb
        #     conn = MySQLdb.connect(host='localhost', user='root', password='mysql', db='stackoverflow')
        #     print("Connected Successfully")
        #     return conn
            
        # except:
        #     print('Cannot connect to database')
        #     return jsonify({'Message' : 'Cannot connect to database'})
        
        

    def create_questions_table(self):
        sqlcommandforQuestions =(
            """
            CREATE TABLE IF NOT EXISTS questions(question_id INT PRIMARY KEY, question_title VARCHAR(250),
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
              user_name VARCHAR(250),user_email VARCHAR(250), user_password VARCHAR(100), user_phone VARCHAR(250), user_status smallint, user_address VARCHAR(250))
            """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforUsers)
        self.conn.commit()
    
    def create_default_user(self):
        sqlcommandforQuestions =(
            """
            INSERT INTO users(user_first_name,user_last_name,user_name,user_email,user_phone,user_address,user_password) VALUES(
                'Walter','Nyeko','@Walter','walter@gmail.com','0786277071','Koro','walter123'
            )
            """
        )
        self.conn = self.connectToDatabase()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforQuestions)
        self.conn.commit()
    def create_answers_table(self):
        sqlcommandforAnswers =(
            """
            CREATE TABLE IF NOT EXISTS answers(answer_id INT PRIMARY KEY, answer_body VARCHAR(250),
             answer_author VARCHAR(250), answer_status smallint, answer_votes INTEGER, question_id INTEGER,
             FOREIGN KEY (question_id) REFERENCES questions(question_id))
            """
        )
        self.conn = self.connectToDatabases()
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcommandforAnswers)
        self.conn.commit()