from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_all_type():
    response = client.get("/types")
    assert response.status_code == 200


def test_get_type_id_exists():
    response = client.get("/types/1")
    assert response.status_code == 200


def test_get_type_id_not_found():
    response = client.get("/types/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Type with id: 2 is not available"}
