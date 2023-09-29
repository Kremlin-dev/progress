from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'Preflight request received'}), 200

    data = request.get_json()
    print('Received signup request:', data)

    username = data.get('username')
    password = data.get('password')
    print(f"Username: {username}, Password: {password}")

    return jsonify({'message': 'User signed up successfully'})

if __name__ == '__main__':
    app.run(debug=True)
