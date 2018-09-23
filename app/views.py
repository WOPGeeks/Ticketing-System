from flask import Flask, render_template, request, jsonify, flash, session
from app.database.connectDB import DatabaseConnectivity
from app.users.users_model import Users
from app.customers.customers_model import Customers
from app.engineers.engineers_models import Engineers
from app.workorders.work_orders_model import WorkOrders
from app.tickets.tickets_model import Tickets
from passlib.hash import sha256_crypt


dbInstance = DatabaseConnectivity()
usersInstance = Users()
custInstance = Customers()
engineersInstance = Engineers()
ordersInstance = WorkOrders()
ticketInstance = Tickets()

app = Flask(__name__)
app.secret_key = 'mysecretkeyghjngdssdfghjhdfhghhsffdtrdddvdvbggdsewwessaae'

@app.route('')
def home():
    return render_template('index.html')

@app.route('/login')
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password_candidate = request.form['password']

    conn = dbInstance.connectToDatabase()
    cur =conn.cursor()
    result = cur.execute("SELECT user_name,user_password from users WHERE user_name=%s", [username])

    data = cur.fetchone()
    usernameDB = data[0]
    if usernameDB == username:
        password = data[1]
        if sha256_crypt.verify(password_candidate,password):
            return render_template('dashboard.html')
            
        else:
            flash('Invalid Password', 'danger')
            return render_template('index.html')
    else:
        flash('{} is not registered'.format(username), 'danger')
        return render_template('index.html')

@app.route('/new_ticket')
def new_ticket():
    theClients = ticketInstance.get_clients()
    theEngineers = ticketInstance.get_engineers()
    theWorkOrderTypes = ticketInstance.get_work_order_types()
    return render_template('new_ticket.html',theWorkOrderTypes=theWorkOrderTypes, theEngineers=theEngineers, theClients=theClients)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/client')
def new_customer():
    return render_template('new_customer.html')

@app.route('/user')
def new_users():
    theReturnedUser = usersInstance.get_no_user()
    return render_template('new_users.html', allTheUsers=theReturnedUser)

@app.route('/engineer')
def new_engineer():
    return render_template('new_engineer.html')

@app.route('/equipment')
def new_equipment():
    return render_template('new_equipment.html')

@app.route('/workorder')
def new_workorder():
    return render_template('new_workorder.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    firstName = request.form['user_first_name']
    lastName = request.form['user_last_name']
    userName = request.form['user_name']
    email = request.form['user_email']
    userAddress = request.form['user_address']
    userPhone = request.form['user_phone']
    userPassword = request.form['user_password']
    encryptedPassword = sha256_crypt.encrypt(str(userPassword))
    usersInstance.add_user(firstName,lastName,email,userAddress,userPhone,userName,encryptedPassword)
    theReturnedUsers = usersInstance.view_all_users()
    return render_template('view_users.html', allTheUsers=theReturnedUsers)

@app.route('/add_client', methods=['POST'])
def add_client():
    customer_name = request.form['customer_name']
    customer_email = request.form['customer_email']
    customer_phone = request.form['customer_phone']
    customer_address = request.form['customer_address']
    customer_product = request.form['customer_product']
    custInstance.add_client(customer_name,customer_phone,customer_email,customer_address,customer_product)
    return render_template('new_customer.html')

@app.route('/add_engineer', methods=['POST'])
def add_engineer():
    engineer_first_name = request.form['engineer_first_name']
    engineer_last_name = request.form['engineer_last_name']
    engineer_email = request.form['engineer_email']
    engineer_phone = request.form['engineer_phone']
    engineer_address = request.form['engineer_address']
    engineer_field_ATM = request.form.get('engineer_field_ATM')
    if engineer_field_ATM:
        engineer_field_ATM_Value = 1
    else:
        engineer_field_ATM_Value = 0

    engineer_field_AIR = request.form.get('engineer_field_AIR')
    if engineer_field_AIR:
        engineer_field_AIR_Value = 1
    else:
        engineer_field_AIR_Value = 0

    engineer_field_TEL = request.form.get('engineer_field_TEL')
    if engineer_field_TEL:
        engineer_field_TEL_Value = 1
    else:
        engineer_field_TEL_Value = 0

    engineersInstance.add_engineer(engineer_first_name,engineer_last_name,engineer_phone,engineer_email,engineer_address,engineer_field_ATM_Value,engineer_field_AIR_Value,engineer_field_TEL_Value)
    return render_template('new_engineer.html')


@app.route('/all_users', methods=['GET'])
def all_users():
    theReturnedUsers = usersInstance.view_all_users()
    return render_template('view_users.html', allTheUsers=theReturnedUsers)

@app.route('/all_admin_users', methods=['GET'])
def all_admin_users():
    theReturnedUsers = usersInstance.view_all_admin_users()
    return render_template('view_users.html', allTheUsers=theReturnedUsers)

@app.route('/all_ordinary_users', methods=['GET'])
def all_ordinary_users():
    theReturnedUsers = usersInstance.view_all_ordinary_users()
    return render_template('view_users.html', allTheUsers=theReturnedUsers)

@app.route('/all_the_users/<int:user_id>', methods=['GET','DELETE'])
def delete_user(user_id):
    usersInstance.delete_a_user(user_id)
    theReturnedUsers = usersInstance.view_all_users()
    return render_template('view_users.html', allTheUsers=theReturnedUsers)

@app.route('/the_user/<int:user_id>', methods=['GET'])
def get_user_by_Id(user_id):
    theReturnedUser = usersInstance.get_user_by_Id(user_id)
    return render_template('new_users.html', allTheUsers=theReturnedUser)

@app.route('/edit_the_user/<int:user_id>', methods=['GET'])
def get_user_details_for_edit(user_id):
    theReturnedUser = usersInstance.get_user_by_Id(user_id)
    return render_template('edit_user.html', allTheUsers=theReturnedUser)

@app.route('/edit_user/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    firstName = request.form['user_first_name_edit']
    lastName = request.form['user_last_name_edit']
    userName = request.form['user_name_edit']
    email = request.form['user_email_edit']
    userAddress = request.form['user_address_edit']
    userPhone = request.form['user_phone_edit']
    userPassword = request.form['user_password_edit']
    encryptedPassword = sha256_crypt.encrypt(str(userPassword))
    usersInstance.edit_a_user(user_id,firstName, lastName,email,userPhone,userAddress,userName,encryptedPassword)
    theReturnedUsers = usersInstance.view_all_users()
    return render_template('view_users.html', allTheUsers=theReturnedUsers)

# WORK ORDERS

@app.route('/edit_the_work_order/<int:work_order_id>', methods=['GET'])
def edit_the_work_order(work_order_id):
    theReturnedOrder = ordersInstance.get_work_order_by_Id(work_order_id)
    return render_template('edit_work_order.html', allTheOrders=theReturnedOrder)

@app.route('/add_work_order', methods=['POST'])
def add_work_order():
    work_order_type = request.form['work_order_type']
    ordersInstance.add_work_order(work_order_type)
    theReturnedOrders = ordersInstance.view_all_work_orders()
    return render_template('view_work_order.html', allTheOrders=theReturnedOrders)

@app.route('/edit_the_work_order/<int:work_order_id>', methods=['POST'])
def edit_work_order(work_order_id):
    workOrderType = request.form['work_order_type_edit']
    ordersInstance.edit_a_work_order(work_order_id,workOrderType)
    theReturnedOrders = ordersInstance.view_all_work_orders()
    return render_template('view_work_order.html', allTheOrders=theReturnedOrders)

@app.route('/all_the_work_orders/<int:work_order_id>', methods=['GET','DELETE'])
def delete_work_order(work_order_id):
    ordersInstance.delete_a_work_order(work_order_id)
    theReturnedOrders = ordersInstance.view_all_work_orders()
    return render_template('view_work_order.html', allTheOrders=theReturnedOrders)

@app.route('/all_work_orders', methods=['GET'])
def all_work_orders():
    theReturnedOrders = ordersInstance.view_all_work_orders()
    return render_template('view_work_order.html', allTheOrders=theReturnedOrders)

@app.route('/all_work_orders_completed', methods=['GET'])
def all_work_orders_completed():
    theReturnedOrders = ordersInstance.view_all_work_orders()
    return render_template('view_work_order.html', allTheOrders=theReturnedOrders)

@app.route('/all_work_orders_pending', methods=['GET'])
def all_work_orders_pending():
    theReturnedOrders = ordersInstance.view_all_work_orders()
    return render_template('view_work_order.html', allTheOrders=theReturnedOrders)

# OUR CLIENTS

@app.route('/all_clients', methods=['GET'])
def all_clients():
    theReturnedClients = custInstance.get_all_clients()
    return render_template('view_clients.html', allTheClients=theReturnedClients)

@app.route('/all_the_clients/<int:client_id>', methods=['GET','DELETE'])
def delete_client(client_id):
    custInstance.delete_a_client(client_id)
    theReturnedClients = custInstance.get_all_clients()
    return render_template('view_clients.html', allTheClients=theReturnedClients)

@app.route('/the_client/<int:client_id>', methods=['GET'])
def get_client_by_Id(client_id):
    theReturnedClient = custInstance.get_user_by_Id(client_id)
    return render_template('new_customer.html', allTheClients=theReturnedClient)

@app.route('/edit_the_client/<int:client_id>', methods=['GET'])
def get_client_details_for_edit(client_id):
    theReturnedClient = custInstance.get_client_by_Id(client_id)
    return render_template('edit_client.html', allTheClients=theReturnedClient)

@app.route('/edit_client/<int:client_id>', methods=['POST'])
def edit_client(client_id):
    clientName = request.form['customer_name_edit']
    clientProduct = request.form['customer_product_edit']
    clientAddress = request.form['customer_address_edit']
    clientPhone = request.form['customer_phone_edit']
    clientEmail = request.form['customer_email_edit']
   
    custInstance.edit_a_client(client_id,clientName, clientProduct,clientAddress,clientPhone,clientEmail)
    theReturnedClients = custInstance.get_all_clients()
    return render_template('view_clients.html', allTheClients=theReturnedClients)

# OUR ENGINEERS

@app.route('/all_engineers', methods=['GET'])
def all_engineers():
    theReturnedEngineers = engineersInstance.get_all_engineers()
    return render_template('view_engineers.html', allTheEngineers=theReturnedEngineers)

@app.route('/all_the_engineers/<int:engineer_id>', methods=['GET','DELETE'])
def delete_engineer(engineer_id):
    engineersInstance.delete_a_engineer(engineer_id)
    theReturnedEngineers = engineersInstance.get_all_engineers()
    return render_template('view_engineers.html', allTheEngineers=theReturnedEngineers)

@app.route('/the_engineer/<int:engineer_id>', methods=['GET'])
def get_engineer_by_Id(engineer_id):
    theReturnedEngineer = custInstance.get_user_by_Id(engineer_id)
    return render_template('new_engineer.html', allTheEngineers=theReturnedEngineer)

@app.route('/edit_the_engineer/<int:engineer_id>', methods=['GET'])
def get_engineer_details_for_edit(engineer_id):
    theReturnedEngineer = engineersInstance.get_engineer_by_Id(engineer_id)
    return render_template('edit_engineer.html', allTheEngineers=theReturnedEngineer)

@app.route('/edit_engineer/<int:engineer_id>', methods=['POST'])
def edit_engineer(engineer_id):
    engineer_first_name = request.form['engineer_first_name_edit']
    engineer_last_name = request.form['engineer_last_name_edit']
    engineer_email = request.form['engineer_email_edit']
    engineer_phone = request.form['engineer_phone_edit']
    engineer_address = request.form['engineer_address_edit']
    engineer_field_ATM = request.form.get('engineer_field_ATM_edit')
    if engineer_field_ATM:
        engineer_field_ATM_Value = 1
    else:
        engineer_field_ATM_Value = 0

    engineer_field_AIR = request.form.get('engineer_field_AIR_edit')
    if engineer_field_AIR:
        engineer_field_AIR_Value = 1
    else:
        engineer_field_AIR_Value = 0

    engineer_field_TEL = request.form.get('engineer_field_TEL_edit')
    if engineer_field_TEL:
        engineer_field_TEL_Value = 1
    else:
        engineer_field_TEL_Value = 0

    engineersInstance.edit_an_engineer(engineer_id,engineer_first_name,engineer_last_name,engineer_address,engineer_phone,engineer_email,engineer_field_ATM_Value,engineer_field_AIR_Value,engineer_field_TEL_Value)
    theReturnedEngineers = engineersInstance.get_all_engineers()
    return render_template('view_engineers.html', allTheEngineers=theReturnedEngineers)
