from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL']=''
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    firstName = db.Column(db.string, nullable=False)
    lastName = db.Column(db.string, nullable=False)
    Email = db.Column(db.string, nullable=False)


if __name__ == "__main__":
    db.create_all()
    app.run()