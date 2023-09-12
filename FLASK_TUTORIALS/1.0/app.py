from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zwuvjhek:I1AhzNgkSJr5Dp-sfvWe4NL3kKN9o1XT@dumbo.db.elephantsql.com/zwuvjhek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    bio = db.Column(db.Text)

if __name__ == "__main__":
    try:
        # Insert a student record
        student1 = Student(firstname='Isaac', lastname='Doe', email='Doe@example.com', age=25, bio='A Farmer')
        db.session.add(student1)
        db.session.commit()

        # Run the Flask application
        app.run()
    except Exception as e:
        print("An error occurred:", str(e))
