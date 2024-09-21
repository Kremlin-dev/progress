from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'yawamp27@gmail.com'  
app.config['MAIL_PASSWORD'] = 'vuvpuyuihrcltyld'  
app.config['MAIL_DEFAULT_SENDER'] = 'yawamp27@gmail.com'  
mail = Mail(app)

@app.route("/send_email")
def send_email():
    msg = Message('Hello from Flask',
                  recipients=['kremlin2704@gmail.com'])  
    msg.body = 'This is a simple email sent from a Flask application using Gmail.'
    
    mail.send(msg)
    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
