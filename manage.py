from app.views import app



if __name__ == '__main__':
    app.secret_key='mysecretkey'
    app.run(debug=True, port=8080)