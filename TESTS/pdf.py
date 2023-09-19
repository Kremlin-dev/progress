import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from PyPDF2 import PdfReader, PdfWriter, PageObject
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'yawamp27@gmail.com'
smtp_password = 'qmiatkbgtzghitya'

subject = 'Modified Internship form'
message = 'I am trying it out'

name_to_insert = ' 26th August 2023 and 6th January 2024.'
name_to_insert1 = 'Kumasi'
name_to_insert2 = '6th September'

custom_page = 'custom_page.pdf'
c = canvas.Canvas(custom_page, pagesize=letter)
c.drawString(80, 389, f"Name: {name_to_insert}")
c.drawString(70, 650, f"Location: {name_to_insert1}")
c.drawString(180, 540, f"Date: {name_to_insert2}")
c.save()

pdf_path = 'mi.pdf'
pdf_reader = PdfReader(pdf_path)

pdf_writer = PdfWriter()

for page in pdf_reader.pages:
    custom_page_reader = PdfReader(custom_page)
    custom_page_obj = custom_page_reader.pages[0]

    # Merge the custom page with the current page
    page.merge_page(custom_page_obj)

    pdf_writer.add_page(page)

output_pdf_path = 'modified_m.pdf'
with open(output_pdf_path, 'wb') as output_pdf_file:
    pdf_writer.write(output_pdf_file)

msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = 'johnmyles523@gmail.com'
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

with open(output_pdf_path, 'rb') as attachment:
    part = MIMEApplication(attachment.read(), Name='modified_m.pdf')

part['Content-Disposition'] = f'attachment; filename="modified_m.pdf"'
msg.attach(part)

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, 'johnmyles523@gmail.com', msg.as_string())
    server.quit()
    print("Email with attachment sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")

os.remove(custom_page)
