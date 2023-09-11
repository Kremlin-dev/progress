from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zwuvjhek:I1AhzNgkSJr5Dp-sfvWe4NL3kKN9o1XT@dumbo.db.elephantsql.com/zwuvjhek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, nullable=False)


if __name__ == "__main__":
    db.create_all()
    app.run()