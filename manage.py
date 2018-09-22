from app.views import app
from app.database.connectDB import DatabaseConnectivity

dbInstance = DatabaseConnectivity()
dbInstance.create_users_table()
dbInstance.create_default_user()

if __name__ == '__main__':
    app.secret_key='mysecretkey'
    app.run(debug=True, port=8080)