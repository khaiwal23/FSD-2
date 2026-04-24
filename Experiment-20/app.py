from flask import Flask, jsonify, request

students = []
current_id = 1


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return {"message": "Backend Server is running"}

    @app.route("/students", methods=["POST"])
    def create_student():
        global current_id

        data = request.get_json(silent=True) or {}

        if "name" not in data:
            return jsonify({"error": "Name is required"}), 400

        student = {
            "id": current_id,
            "name": data["name"],
            "age": data.get("age", None),
        }

        students.append(student)
        current_id += 1

        return jsonify(student), 201

    @app.route("/students", methods=["GET"])
    def get_students():
        return jsonify(students), 200

    @app.route("/students/<int:student_id>", methods=["GET"])
    def get_student(student_id):
        student = next((s for s in students if s["id"] == student_id), None)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        return jsonify(student), 200

    @app.route("/students/<int:student_id>", methods=["PUT"])
    def update_student(student_id):
        data = request.get_json(silent=True) or {}
        student = next((s for s in students if s["id"] == student_id), None)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        student["name"] = data.get("name", student["name"])
        student["age"] = data.get("age", student["age"])

        return jsonify(student), 200

    @app.route("/students/<int:student_id>", methods=["DELETE"])
    def delete_student(student_id):
        global students

        student = next((s for s in students if s["id"] == student_id), None)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        students = [s for s in students if s["id"] != student_id]

        return jsonify({"message": "Deleted successfully"}), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
