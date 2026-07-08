from app.main import app


def test_create_energy(client):

    # Criar sala necessária para o equipamento
    room_response = client.post(
        "/rooms/",
        json={
            "nome": "Sala Energia Teste",
            "tipo": "Escritório",
            "capacidade": 10,
            "andar": 1
        }
    )

    assert room_response.status_code == 200


    # Criar equipamento vinculado à sala
    equipment_response = client.post(
        "/equipments/",
        json={
            "nome": "Computador Teste",
            "categoria": "Informática",
            "consumo_watts": 300,
            "ligado": True,
            "room_id": 1
        }
    )

    assert equipment_response.status_code == 200


    # Criar registro de energia
    response = client.post(
        "/energy/",
        json={
            "equipment_id": 1,
            "consumo_watts": 500,
            "temperatura": 25.5,
            "ligado": True
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert data["equipment_id"] == 1
    assert data["consumo_watts"] == 500
    assert data["temperatura"] == 25.5
    assert data["ligado"] is True