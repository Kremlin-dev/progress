from flask import Flask, render_template
from login import Login
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html', title='E-Learning Platform')

@app.route('/login')
def login():
    form = Login()
    return render_template('login.html', title = "E-Learning Platform/Login Page", form=form)


if __name__ == "__main__":
    app.run()
