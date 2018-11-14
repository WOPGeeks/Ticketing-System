from app.views import app
from app.database.connectDB import DatabaseConnectivity

dbInstance = DatabaseConnectivity()
dbInstance.create_users_table()
dbInstance.create_clients_table()
dbInstance.create_work_orders_table()
dbInstance.create_tickets_table()
dbInstance.create_equipments_table()
dbInstance.create_engineers_table()

if __name__ == '__main__':
    app.secret_key = 'mysecretkeyghjngdssdfghjhdfhghhsffdtrdddvdvbggdsewwessaae'
    app.run(debug=True, port=8080)