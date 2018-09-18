class DatabaseConnectivity:
    def connectToDatabase(self):
        import MySQLdb
        conn = MySQLdb.connect(db='tickets', user='root', password='mysql', host='localhost')
        self.cur =conn.cursor()
        return self.cur