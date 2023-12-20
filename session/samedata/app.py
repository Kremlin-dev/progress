from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2704@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key
db = SQLAlchemy(app)

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class SessionModel(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_token = db.Column(db.String(32), unique=True, nullable=False)
    expiration_time = db.Column(db.DateTime, nullable=False)

def load_session_data():
    session_token = request.cookies.get('session_token')

    if session_token:
        session_data = SessionModel.query.filter_by(session_token=session_token).first()

        if session_data:
            if session_data.expiration_time > datetime.utcnow():
                session_data.expiration_time = datetime.utcnow() + timedelta(seconds=30)
                db.session.commit()
                return session_data
            else:
                print("Session Data has expired.")
                return None
        else:
            print("No Session Data found for the given token.")

    return None


def generate_session_token(user_id):
    unique_identifier = secrets.token_hex(8)
    return f"{user_id}_{unique_identifier}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        user = UserModel.query.filter_by(email=email, password=password).first()

        if user:
            session_token = generate_session_token(user.id)
            expiration_time = datetime.utcnow() + timedelta(seconds=30)

            session_data = SessionModel(user_id=user.id, session_token=session_token, expiration_time=expiration_time)
            db.session.add(session_data)
            db.session.commit()

            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('session_token', session_token)
            return response
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    session_data = load_session_data()

    if session_data:
        user_id = session_data.user_id

        if user_id == 1:
            content = "Welcome User 1! This is your personalized dashboard."
        elif user_id == 2:
            content = "Greetings User 2! Explore your unique dashboard experience."
        else:
            content = "Welcome! This is a generic dashboard for all other users."

        return render_template('dashboard.html', content=content)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('session_token')
    return response

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
