class DatabaseConnectivity:
    def connectToDatabase(self):
        import MySQLdb
        self.conn = MySQLdb.connect(db='tickets', user='root', password='mysql', host='localhost')
        return self.conn