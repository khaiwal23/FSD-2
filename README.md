# Microservices Backend Project

## 📌 Description
This project demonstrates a simple microservice-based backend using Flask.

Two services are created:
1. Customer Service
2. Order Service

---

## 🧱 Services

### 1️⃣ Customer Service
- Runs on Port: 5000
- API:
  GET /customers/<id>/orders

- Fetches customer orders from Order Service

---

### 2️⃣ Order Service
- Runs on Port: 5001
- APIs:
  GET /orders/<customer_id>
  PUT /orders/<order_id>

- Stores order data in memory
- Updates order status

---

## 🔗 Microservice Communication
Customer Service calls Order Service using HTTP requests.

---

## 🧪 Testing

### GET Request
http://127.0.0.1:5000/customers/101/orders

### PUT Request
http://127.0.0.1:5001/orders/1

Body:
{
  "status": "Delivered"
}

---

## ⚙️ Technologies Used
- Python
- Flask
- Requests library

---

## 📌 Notes
- Data is stored in-memory (no database)
- Tested using Postman