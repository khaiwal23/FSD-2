from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(["Himanshu", "User2"])

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)