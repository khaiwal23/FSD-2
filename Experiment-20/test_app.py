import pytest

import app as app_module
from app import app


@pytest.fixture(autouse=True)
def reset_storage():
    app_module.students = []
    app_module.current_id = 1
    app.testing = True
    yield
    app_module.students = []
    app_module.current_id = 1


@pytest.fixture
def client():
    return app.test_client()


def test_create_student(client):
    response = client.post("/students", json={"name": "Student-1"})
    assert response.status_code == 201
    assert response.json["name"] == "Student-1"


def test_get_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_student(client):
    create_response = client.post("/students", json={"name": "Student-2"})
    student_id = create_response.json["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json["name"] == "Student-2"


def test_update_student(client):
    create_response = client.post("/students", json={"name": "Student-3"})
    student_id = create_response.json["id"]

    response = client.put(
        f"/students/{student_id}",
        json={"name": "Student-3 Updated"},
    )
    assert response.status_code == 200
    assert response.json["name"] == "Student-3 Updated"


def test_delete_student(client):
    create_response = client.post("/students", json={"name": "Student-4"})
    student_id = create_response.json["id"]

    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 200

    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 404
