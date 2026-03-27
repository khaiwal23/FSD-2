from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Customer Service is Running 🚀"
# In-memory customers
customers = [
    {"id": 101, "name": "Himanshu"},
    {"id": 102, "name": "Rahul"},
]

# Fetch customer orders from Order Service
@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
def get_customer_orders(customer_id):
    response = requests.get(f'http://127.0.0.1:5001/orders/{customer_id}')
    
    return jsonify({
        "customer_id": customer_id,
        "orders": response.json()
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)