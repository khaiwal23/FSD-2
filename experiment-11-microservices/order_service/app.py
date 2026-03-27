from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Order Service is Running 🚀"

# In-memory order data
orders = [
    {"id": 1, "customer_id": 101, "item": "Laptop", "status": "Pending"},
    {"id": 2, "customer_id": 102, "item": "Phone", "status": "Shipped"},
]

# Get orders by customer ID
@app.route('/orders/<int:customer_id>', methods=['GET'])
def get_orders(customer_id):
    result = [o for o in orders if o["customer_id"] == customer_id]
    return jsonify(result)

# Update order status
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    for order in orders:
        if order["id"] == order_id:
            order["status"] = data.get("status", order["status"])
            return jsonify({"message": "Order updated", "order": order})
    return jsonify({"message": "Order not found"}), 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)