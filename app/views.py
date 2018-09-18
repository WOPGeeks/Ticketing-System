from flask import Flask, render_template, request, jsonify, flash, session
from app.database.connectDB import DatabaseConnectivity

dbInstance = DatabaseConnectivity()

app = Flask(__name__)


@app.route('/login')
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password_candidate = request.form['password']

    cur = dbInstance.connectToDatabase()
    result = cur.execute("SELECT * from users WHERE user_name=%s", [username])

    if result >0:
        data = cur.fetchone()
        password = data[5]
        if password_candidate == password:
            return render_template('dashboard.html')
            
        flash('Invalid Password', 'danger')
        return render_template('index.html')
    else:
        flash('No User Found', 'danger')
        return render_template('index.html')

