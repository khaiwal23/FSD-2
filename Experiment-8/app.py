from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

SECRET_KEY = "secret123"

USER_DATA = {
    "username": "admin",
    "password": "1234"
}

@app.route('/auth-header', methods=['GET'])
def auth_header():

    auth = request.authorization

    if auth and auth.username == USER_DATA["username"] and auth.password == USER_DATA["password"]:
        return jsonify({"message": "Authorization Header Authentication Successful"})

    return jsonify({"message": "Authentication Failed"}), 401

@app.route('/')
def home():
    return "Token Authentication API is running successfully"


@app.route('/custom-header', methods=['GET'])
def custom_header():

    username = request.headers.get('X-Username')
    password = request.headers.get('X-Password')

    if username == USER_DATA["username"] and password == USER_DATA["password"]:
        return jsonify({"message": "Custom Header Authentication Successful"})

    return jsonify({"message": "Authentication Failed"}), 401


@app.route('/login', methods=['POST'])
def login():

    data = request.json

    if data["username"] == USER_DATA["username"] and data["password"] == USER_DATA["password"]:

        token = jwt.encode({
            'user': data["username"],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS256")

        return jsonify({"token": token})

    return jsonify({"message": "Invalid Credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
def jwt_protected():

    auth_header = request.headers.get("Authorization")

    if auth_header:

        token = auth_header.split(" ")[1]

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return jsonify({"message": "JWT Authentication Successful", "user": data["user"]})

        except:
            return jsonify({"message": "Invalid Token"}), 401

    return jsonify({"message": "Token Missing"}), 401


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)