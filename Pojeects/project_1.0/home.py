from flask import Flask, render_template, redirect, flash, session
from login import Login
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='E-Learning Platform/homepage')
# if 'username' in session:
# return render_template('base.html', title='E-Learning Platform',is_logged_in=True)
#   return render_template('base.html', title='E-Learning Platform',is_logged_in=False)


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
       flash('login Successful')
       return redirect('/home')
    return render_template('login.html', title = "E-Learning Platform/Login Page", form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/home')
if __name__ == "__main__":
    app.run()
