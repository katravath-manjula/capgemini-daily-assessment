from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector as mysql
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

try:
    db_connection = mysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='lol'
    )
    db_cursor = db_connection.cursor()
    
    if db_connection.is_connected():
        print('Database connected')

except Error as err:
    print('Error:', err)

@app.route('/students', methods=['GET'])
def get_all_students():
    db_cursor.execute('SELECT * FROM students')
    student_records = db_cursor.fetchall()
    return jsonify(student_records)

@app.route('/students', methods=['POST'])
def add_student():
    student_data = request.json
    name = student_data['name']
    email = student_data['email']
    age = student_data['age']
    roll_number = student_data['rollNumber']
    department = student_data['department']
    phone_number = student_data['phoneNumber']
    gender = student_data['gender']

    db_cursor.execute(
        '''INSERT INTO students 
        (name, email, age, rollNumber, department, phoneNumber, gender)
        VALUES (%s, %s, %s, %s, %s, %s, %s)''',
        (name, email, age, roll_number, department, phone_number, gender)
    )
    db_connection.commit()
    return jsonify({'message': 'Student added successfully'})

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    db_cursor.execute('SELECT * FROM students WHERE id = %s', (student_id,))
    student_record = db_cursor.fetchone()
    if student_record:
        return jsonify(student_record)
    return jsonify({'message': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student_data = request.json
    name = student_data['name']
    email = student_data['email']
    age = student_data['age']
    roll_number = student_data['rollNumber']
    department = student_data['department']
    phone_number = student_data['phoneNumber']
    gender = student_data['gender']

    db_cursor.execute(
        '''UPDATE students SET
        name=%s, email=%s, age=%s, rollNumber=%s, department=%s, phoneNumber=%s, gender=%s 
        WHERE id=%s''',
        (name, email, age, roll_number, department, phone_number, gender, student_id)
    )
    db_connection.commit()
    return jsonify({'message': 'Student updated successfully'})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    db_cursor.execute('DELETE FROM students WHERE id = %s', (student_id,))
    db_connection.commit()
    return jsonify({'message': 'Student deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
