from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2704@localhost/vra'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))

# Create the table if it doesn't exist
with app.app_context():
    db.create_all()

@app.route('/')
def generate_pdf():
    # Fetch user details from the database
    user_details = User.query.first()

    # Create a PDF buffer using ReportLab
    pdf_buffer = generate_pdf_buffer(user_details)

    # Send the PDF as a response
    return send_pdf_response(pdf_buffer, filename='letter.pdf')

def generate_pdf_buffer(user_details):
    # Create a PDF buffer using ReportLab
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)

    # Draw company logo at the top right corner
    company_logo_path = './vra.png' 
    p.drawInlineImage(company_logo_path, 450, 750, width=2*inch, height=0.5*inch)

    # Company details (moved to the top left corner)
    p.setFont("Helvetica", 12)
    p.drawString(50, 720, "Company Name")
    p.drawString(50, 700, "123 Main Street")
    p.drawString(50, 680, "City, Country")
    p.drawString(50, 660, "Phone: +1 (555) 123-4567")
    p.drawString(50, 640, "Email: info@example.com")

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(50, 600, f"Dear {user_details.name},")
    p.drawString(50, 580, f"I hope this letter finds you well at the age of {user_details.age}.")
    p.drawString(50, 560, f"You are currently residing in {user_details.city}.")
    p.drawString(50, 540, "Thank you for being a valued member of our community.")

    # Add more content as needed

    # Draw sincerely and management
    p.drawString(50, 500, "Sincerely,")
    p.drawString(50, 480, "Management")

    # Draw signature lines and text under the lines
    p.line(100, 470, 300, 470)
    p.drawString(50, 460, " ")  # Text indicating it's a signature line
   

    p.line(400, 470, 600, 470)
    p.drawString(50, 460, "")  # Text indicating it's a signature line
    p.drawString(450, 440, "Your Signature")

    # Close the PDF object cleanly, and we're done.
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
    app.run(debug=True)
