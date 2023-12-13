from fastapi.testclient import TestClient
from main import app
from fastapi import status
import json

client= TestClient(app)

def test_register_user():
    data= {
  "name": "kishore",
  "email": "kishore1008@gmail.com",
  "password": "kishore1008"
}
    response= client.post("/register-user",json=data)
    assert response.status_code == 201
    assert response.json()["name"]=="kishore"
    assert response.json()["email"]=="kishore1008@gmail.com"
    assert response.json()["password"]=="kishore1008"
