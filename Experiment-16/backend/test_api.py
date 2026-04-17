import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_users():
    res = requests.get(f"{BASE_URL}/users")
    assert res.status_code == 200

def test_add_user():
    res = requests.post(f"{BASE_URL}/users", json={"name": "Himanshu"})
    assert res.status_code == 201