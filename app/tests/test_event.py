from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_all_event():
    response = client.get("/events")
    assert response.status_code == 200
