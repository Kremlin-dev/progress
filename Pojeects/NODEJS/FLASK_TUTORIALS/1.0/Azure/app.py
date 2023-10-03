from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB_SERVER = 'demoserver27.database.windows.net,1433'
DB_DATABASE = 'Demo'
DB_AUTHENTICATION = 'Active Directory Default'


connection_string = (
    f'DRIVER=ODBC Driver 17 for SQL Server;'
    f'SERVER={DB_SERVER};'
    f'DATABASE={DB_DATABASE};'
    f'Authentication={DB_AUTHENTICATION};'
    f'Encrypt=yes;'
    f'TrustServerCertificate=no;'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=' + connection_string

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()

        return 'User signed up successfully!'

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
