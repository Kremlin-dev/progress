from flask import Flask, session, redirect, url_for
import uuid
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def generate_random_username():
    # Generate a random username using letters and digits
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@app.route('/login')
def login():
    # Generate a random username for demonstration purposes
    username = generate_random_username()

    # Simulate user authentication
    # In a real application, you would check the username and password
    # and generate a unique session token for the authenticated user

    # For simplicity, we are using a UUID as a session token
    session['token'] = str(uuid.uuid4())

    # Set other user-specific information in the session
    session['username'] = username

    return f"User {username} logged in with session token: {session['token']}"

@app.route('/dashboard')
def dashboard():
    # Access user-specific information from the session
    username = session.get('username', 'Guest')
    session_token = session.get('token', 'No session token')

    return f"Welcome to the dashboard, {username}! Your session token is: {session_token}"

@app.route('/logout')
def logout():
    # Clear user-specific information on logout
    session.pop('token', None)
    session.pop('username', None)

    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
