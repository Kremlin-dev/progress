#!/usr/bin/python3

from flask import Flask, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:krem@localhost/flasktry'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'krem'

db = SQLAlchemy(app)

class name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(20), unique=True, nullable=False)
    color = db.Column(db.String(20), nullable=False)

    def __init__(self, pname,color):
        self.pname = pname
        self.color = color


@app.route('/')
def home():
     return '<a href="/addperson"><button> Click here </button></a>'
@app.route('/addperson')
def addperson():
    return render_template('index.html')

@app.route('/personadd', methods=['POST'])
def personadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = name(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template('index.html')


if __name__ == "__main__":
    db.create_all()
    app.run()


