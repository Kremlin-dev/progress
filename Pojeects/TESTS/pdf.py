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

name_to_insert = 'Isaac Yaw Amponsah'
name_to_insert1 = 'Computer Engineering'
name_to_insert2 = '0558507341'
name_to_insert3 = '19th September, 2023'
name_to_insert4 = '19th September, 2023 to 19th October, 2023'
custom_page = 'custom_page.pdf'
c = canvas.Canvas(custom_page, pagesize=letter)
c.drawString(140, 420, f"{name_to_insert}")
c.drawString(142, 397, f"{name_to_insert1}")
c.drawString(145, 400, f"{name_to_insert2}")
c.drawString(410, 522, f" {name_to_insert3}")
c.drawString(180, 540, f"{name_to_insert4}")
c.save()

pdf_path = 'm.pdf'
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
msg['To'] = 'kremlin2704@gmail.com'
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

with open(output_pdf_path, 'rb') as attachment:
    part = MIMEApplication(attachment.read(), Name='modified_m.pdf')

part['Content-Disposition'] = f'attachment; filename="modified_m.pdf"'
msg.attach(part)


try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, 'kremlin2704@gmail.com', msg.as_string())
    server.quit()
    print("Email with attachment sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")

os.remove(custom_page)
