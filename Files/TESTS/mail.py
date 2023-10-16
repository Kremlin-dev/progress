# This piece of code is used to send an external document via email 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#imported  libraries need 

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'yawamp27@gmail.com'
smtp_password = 'qmiatkbgtzghitya' 
#
subject = 'Internship form'
message = 'I am trying it out'

msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = 'johnmyles523@gmail.com'
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))
path = file_path = './m.pdf'  

with open(path, 'rb') as attachment:
    part = MIMEApplication(attachment.read(), Name='m.pdf')

part['Content-Disposition'] = f'attachment; filename="m.pdf"'
msg.attach(part)

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, 'johnmyles523@gmail.com', msg.as_string())
    server.quit()
    print("Email with attachment sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")