from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:****@localhost:3306/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    bio = db.Column(db.Text)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

if __name__ == "__main__":
    try:
       
        db.create_all()

        student1 = Student(firstname='Isaac', lastname='Doe', email='Doe@example.com', age=25, bio='A Farmer')
        db.session.add(student1)
        db.session.commit()


        app.run()
    except Exception as e:
        print("An error occurred:", str(e))
