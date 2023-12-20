from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch  
from datetime import datetime
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2704@localhost/vra'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    internship_start_date = db.Column(db.String(20))
    internship_end_date = db.Column(db.String(20))
    schoolname = db.Column(db.String(50))  
    location = db.Column(db.String(50))  
    department = db.Column(db.String(50))  
    department_location = db.Column(db.String(50)) 
    date = db.Column(db.String(20))

with app.app_context():
    db.create_all()

@app.route('/')
def generate_pdf():
    user_details = User.query.first()
    pdf_buffer = generate_pdf_buffer(user_details)
    return send_pdf_response(pdf_buffer, filename='internship_letter.pdf')

def generate_pdf_buffer(user_details):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    company_logo_path = './724e9731-85bb-498f-a191-daee61fdcb9c.jpeg'
    p.drawInlineImage(company_logo_path, 50, 750, width=2*inch, height=0.5*inch)
    current_date = datetime.now().strftime('%Y-%m-%d')

    p.drawRightString(520, 770, f'Our ref: ')
    p.drawRightString(525, 750, f'Your ref: ')
    p.drawRightString(570, 730, f'Date: {current_date}')
    p.line(50, 720, 550, 720)


    p.drawRightString(140, 700, f'{user_details.name}')
    p.drawRightString(90, 680, f' {user_details.schoolname}')
    p.drawRightString(90, 660, f' {user_details.location}')
    p.drawString(50, 645, f'Dear {user_details.name},')

    p.drawString(350, 280, f'Yours sincerely,')
    p.drawString(350, 245, f'Eric Mensah Bonsu,')
    p.drawString(350, 230, f'DIRECTOR, HUMAN RESOURCES')

    p.drawString(50, 200, f'I hereby accept the offer of internship with the VRA on the terms and conditions stated above')
    p.drawString(420, 170, f'....................... Signature')
    p.drawString(420, 150, f'....................... Date')
    p.drawString(50, 100, f'Cc: VRA Management')


    p.drawString(40, 38, f'Electro Volta House, 28th February Road, P.O. Box MB 77, Accra, Ghana. Phone: +233 302 666 941- 9')
    p.drawString(170, 20, f'Digital Address: GA 145-7445 website: www.vra.com')





    p.line(50, 720, 550, 720)
    center_x = (550 - p.stringWidth('PERMISSION TO UNDERTAKE AN INTERNSHIP WITH VRA', "Helvetica", 12)) / 2
    p.drawString(center_x, 625, 'PERMISSION TO UNDERTAKE AN INTERNSHIP WITH VRA')


    lines = [
    f'We are pleased to inform you that your request to undertake an internship with the Volta River Authority '
    f'has been accepted. Accordingly, your internship period is effective '
    f'{user_details.internship_start_date} to {user_details.internship_end_date}',
    f'You will be attached to the {user_details.department} Department in {user_details.department_location}.',
    'You will report to the administrator, who will provide you with an orientation about the '
    'Department and the Authority in general.',
    'You will strictly abide by the prescribed rules governing the work environment within the Authority.',
    'You will be allowed to ride on the staff bus to and from work. However, '
    'you will not be paid any allowance, and accommodation or meals will not be provided.',
    'You are required to dress decently at all times.',
    'This internship offer is subject to you signing the attached indemnity form, '
    'covering the period of your training with the Authority.',
    f'If this offer is acceptable to you under the foregoing conditions, '
    'kindly sign in the space provided below and return the duplicate of this letter along with '
    f'the signed Indemnity Form to the Director, Human Resources, by {user_details.date}.',
    'We hope you will make good use of the opportunity offered to you and apply yourself diligently to the job.',
]

    max_words_per_line = 17
    lines = [line.split() for line in lines]
    lines = [' '.join(line[i:i + max_words_per_line]) for line in lines for i in range(0, len(line), max_words_per_line)]
    y_position = 600

    for line in lines:
        upper_line_width = 550 - 50

        while len(line) > 0:
            next_line_width = min(upper_line_width, p.stringWidth(line, "Helvetica", 12))
            p.drawString(50, y_position, line[:int(next_line_width)])
            line = line[int(next_line_width):]
            y_position -= 20

    p.line(50, 50, 550, 50)
    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

def send_pdf_response(pdf_buffer, filename='document.pdf'):
    response = make_response(pdf_buffer.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'inline; filename={filename}'
    return response

if __name__ == '__main__':
    with app.app_context():
     app.run(debug=True)
