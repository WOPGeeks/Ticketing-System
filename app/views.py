from flask import Flask, render_template, request, jsonify, flash, session
from app.database.connectDB import DatabaseConnectivity
from app.users.users_model import Users
from app.customers.customers_model import Customers
from app.engineers.engineers_models import Engineers
from passlib.hash import sha256_crypt


dbInstance = DatabaseConnectivity()
usersInstance = Users()
custInstance = Customers()
engineersInstance = Engineers()

app = Flask(__name__)


@app.route('/login')
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password_candidate = request.form['password']

    conn = dbInstance.connectToDatabase()
    cur =conn.cursor()
    result = cur.execute("SELECT * from users WHERE user_name=%s", [username])

    if result >0:
        data = cur.fetchone()
        password = data[5]
        if sha256_crypt.verify(password_candidate,password):
            return render_template('dashboard.html')
            
        flash('Invalid Password', 'danger')
        return render_template('index.html')
    else:
        flash('No User Found', 'danger')
        return render_template('index.html')

@app.route('/new_ticket')
def new_ticket():
    return render_template('new_ticket.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/client')
def new_customer():
    return render_template('new_customer.html')

@app.route('/user')
def new_users():
    return render_template('new_users.html')

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
    return render_template('new_users.html')

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


