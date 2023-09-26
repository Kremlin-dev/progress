from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
app.secret_key = "krem"
app.static_folder = "static"
@app.route('/', methods=['GET'])
def signup():
    return render_template("signup.html")



if __name__ == '__main__':
    app.run()