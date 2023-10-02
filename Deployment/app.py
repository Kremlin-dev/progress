from flask import Flask, jsonify, request, session, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "supports_credentials": True}})
app.secret_key = "krem"

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == "OPTIONS":
        # Handle preflight request
        response = make_response()
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response

    if request.method == "POST":
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if username and password:
            print("Received data:", username, password)
            session["sample_data"] = {
                "username": username,
                "password": password,
            }

            return jsonify({'message': 'User signed up successfully'})

    return jsonify({'error': 'Invalid data'}), 400

@app.route('/get_session', methods=["GET"])
def get_session():
    sample_data = session.get("sample_data")
    print("session:", sample_data)

    if sample_data:
        return jsonify(sample_data)
    else:
        return jsonify({'message': 'No session data available'})

if __name__ == '__main__':
    app.run(debug=True)
