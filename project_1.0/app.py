from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='E-Learning Platform', name="Isaac")


if __name__ == "__main__":
    app.run()