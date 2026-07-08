from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_room():

    response = client.post(
        "/rooms/",
        json={
            "nome": "Sala Reunião",
            "tipo": "Reunião",
            "capacidade": 10,
            "andar": 1
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["nome"] == "Sala Reunião"
    assert data["capacidade"] == 10



def test_get_rooms():

    response = client.get("/rooms/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)