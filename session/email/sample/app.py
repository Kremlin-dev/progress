from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail with your provided settings
app.config['MAIL_SERVER'] = 'live.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'api'
app.config['MAIL_PASSWORD'] = 'c7b73a7d202902f288d83eb9b8ac479b'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'kremlin2704@gmail.com'

mail = Mail(app)

# @app.route('/send_email', methods=['POST'])
# def send_email():
#     data = request.json
#     email = data.get('email')
#     subject = data.get('subject')
#     message = data.get('message')

#     if not email or not subject or not message:
#         return jsonify({"error": "Email, subject, and message are required"}), 400

#     msg = Message(subject, recipients=[email])
#     msg.body = message

#     try:
#         mail.send(msg)
#         print(f"Email sent to {email} successfully!")
#         return jsonify({"message": f"Email sent to {email} successfully!"}), 200
#     except Exception as e:
#         print(f"Failed to send email: {str(e)}")
#         return jsonify({"error": f"Failed to send email: {str(e)}"}), 500


from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'live.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'api'
app.config['MAIL_PASSWORD'] = 'c7b73a7d202902f288d83eb9b8ac479b'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/send_email", methods=['POST'])
def send_email_to_multiple_recipients():
    data = request.json
    print(data)
    recipients = data.get('recipients')
    subject = data.get('subject')
    message = data.get('message')


    if not recipients or not subject or not message:
        return jsonify({"error": "Recipients, subject, and message are required"}), 400

    # Creating the message
    msg = Message(subject,
                  sender="iyamponsah@st.knust.edu.gh",
                  recipients=recipients)
    msg.body = message
    
    # Sending the email
    try:
        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send email: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
