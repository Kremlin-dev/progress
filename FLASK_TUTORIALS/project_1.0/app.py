#!/usr/in/python3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:krem@localhost/flasktry'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(40), nullable=False)
    LastName = db.Column(db.String(40), nullable= False)

    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName =LastName

@app.route('/')
def homepage():
    return ' <a href="/login"><button>Click Here</button></a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    FirstName =request.form["FirstName"]
    LastName =request.form["LastName"]
    entry = Person(FirstName, LastName)
    db.session.add(entry)
    db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
    db.create_all()
    app.run()
