#!/usr/bin/python3

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:krem@localhost/flasktry'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'krem'

db = SQLAlchemy(app)

class name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)

    def __init__(self, firstname, lastname):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/details', methods=['POST'])
def details():
    firstname=request.form["firstname"]
    lastname=request.form["lastName"]
    entry = name(firstname, lastname)
    db.session.add(entry)
    db.session.commit()
    
    return render_template('index.html')


if __name__ == "__main__":
    db.create_all()
    app.run()
    
