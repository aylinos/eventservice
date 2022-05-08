from fastapi.testclient import TestClient

from ..main.main import app

client = TestClient(app)


def test_get_all_type():
    response = client.get("/type")
    assert response.status_code == 200


def test_get_type_id_exists():
    response = client.get("/type/1")
    assert response.status_code == 200


def test_get_type_id_not_found():
    response = client.get("/type/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Type with id: 2 is not available"}
