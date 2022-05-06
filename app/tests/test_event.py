from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_all_event():
    response = client.get("/event")
    assert response.status_code == 200
