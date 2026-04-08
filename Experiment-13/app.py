from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="testuser",
    password="1234",
    database="student_db"
)

cursor = db.cursor(dictionary=True)

# CREATE
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    age = data.get('age')

    # Validation
    if not name or not email or not age:
        return jsonify({"error": "All fields required"}), 400

    if age <= 0:
        return jsonify({"error": "Invalid age"}), 400

    cursor.execute(
        "INSERT INTO student (name, email, age) VALUES (%s,%s,%s)",
        (name, email, age)
    )
    db.commit()

    return jsonify({"message": "Student added successfully"})


# READ
@app.route('/students', methods=['GET'])
def get_students():
    cursor.execute("SELECT * FROM student")
    return jsonify(cursor.fetchall())


# UPDATE
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    cursor.execute(
        "UPDATE student SET name=%s,email=%s,age=%s WHERE id=%s",
        (data['name'], data['email'], data['age'], id)
    )
    db.commit()

    return jsonify({"message": "Student updated successfully"})


# DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cursor.execute("DELETE FROM student WHERE id=%s", (id,))
    db.commit()

    return jsonify({"message": "Student deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)