from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2704@localhost:3306/vra_internship_data'

db.init_app(app)

@app.route('/filter', methods=['POST'])
def filter_data():
    data = request.get_json()

    if 'key' not in data or 'value' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    key = data['key']
    value = data['value']

    valid_keys = ['FirstName', 'LastName', 'Email', 'Residence', 'institution', 'Level', 'inst_location', 'IndexNumber', 'Programme', 'StartDate', 'EndDate']
    if key not in valid_keys:
        return jsonify({'error': 'Invalid key'}), 400

    # Use SQLAlchemy to query the database with case-insensitive comparison
    query = Student.query.filter(getattr(Student, key).ilike(f'%{value}%')).all()

    # Serialize the query result to JSON
    filtered_data = [{'StudentId': student.StudentId, 'FirstName': student.FirstName, 'LastName': student.LastName, 'Email': student.Email, 'Residence': student.Residence, 'institution': student.institution, 'Level': student.Level, 'inst_location': student.inst_location, 'IndexNumber': student.IndexNumber, 'Programme': student.Programme, 'StartDate': student.StartDate, 'EndDate': student.EndDate} for student in query]

    return jsonify({'result': filtered_data})

if __name__ == '__main__':
    app.run(debug=True)
