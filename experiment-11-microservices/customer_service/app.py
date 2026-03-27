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
try:
    response = requests.get(f'https://order-service-hpiu.onrender.com/orders/{customer_id}')
    orders = response.json()
except Exception as e:
    return jsonify({"error": "Order service not available", "details": str(e)})

return jsonify({
    "customer_id": customer_id,
    "orders": orders
})
    
return jsonify({
        "customer_id": customer_id,
        "orders": response.json()
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)