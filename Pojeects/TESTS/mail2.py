import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'yawamp27@gmail.com'
smtp_password = 'qmiatkbgtzghitya' 

subject = 'Greetings'
message = 'Hello Myles'

msg = MIMEMultipart()       
msg['From'] = smtp_username
msg['To'] = 'kremlin2704@gmail.com'
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, 'kremlin2704@gmail.com', msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")