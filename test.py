from fastapi.testclient import TestClient
from main import app
from fastapi import status
import json

client= TestClient(app)

def test_root():
    response = client.get("/healthchecker")
    assert response.status_code == 200
    assert response.json() == {  "message": "Welcome to FastAPI with SQLAlchemy"
}


# def test_register_user():
#     data= {
#   "name": "kishore",
#   "email": "kishore1008@gmail.com",
#   "password": "kishore1008"
# }
#     response= client.post("/api/register-user",json=data)
#     assert response.status_code == 201
#     assert response.json()["name"]=="kishore"
#     assert response.json()["email"]=="kishore1008@gmail.com"
#     assert response.json()["password"]=="kishore1008"

def test_create_user():
    data = {
        "name": "kishore",
        "email": "kishore176443@gmail.com",
        "password": "kishore456",
    }
    response = client.post("/api/register-user/", json=data)
    assert response.status_code == 201
    assert response.json() == {
  "status": "success",
  "message": "User registered successfully"
}

def test_get_user():
     response = client.get("/api/get-user/")
     assert response.status_code == 200
     assert response.json() =={
  "id": "636618e0-49f1-4d9e-a35a-b12bdd4502df",
  "name": "kishore",
  "email": "kishorerayan2001@gmail.com",
  "is_approved": True,
  "is_email_verified": False
}