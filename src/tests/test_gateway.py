from fastapi.testclient import TestClient
from src.main import app
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

client = TestClient(app)


def test_home():
    """ Test if the API is running """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Gateway"}


def test_generate_token():
    """ Test token generation """
    response = client.post("/auth/token")
    assert response.status_code == 200
    assert "access_token" in response.json()

    return response.json()["access_token"]


def test_protected_route_without_token():
    """ Test access to a protected route without authentication """
    response = client.get("/auth/me")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}


def test_protected_route_with_token():
    """ Test access to a protected route with authentication """
    token = test_generate_token()  # Generate a valid token

    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "user" in response.json()
