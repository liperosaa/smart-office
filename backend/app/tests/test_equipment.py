def test_create_equipment(client):

    # Criar sala necessária para o equipamento
    room_response = client.post(
        "/rooms/",
        json={
            "nome": "Sala Equipamentos",
            "tipo": "Reunião",
            "capacidade": 20,
            "andar": 1
        }
    )

    assert room_response.status_code == 200

    room = room_response.json()


    # Criar equipamento
    response = client.post(
        "/equipments/",
        json={
            "nome": "Ar Condicionado",
            "categoria": "Climatização",
            "consumo_watts": 1500,
            "ligado": True,
            "room_id": room["id"]
        }
    )


    assert response.status_code == 200


    data = response.json()


    assert data["nome"] == "Ar Condicionado"
    assert data["categoria"] == "Climatização"
    assert data["consumo_watts"] == 1500
    assert data["ligado"] is True
    assert data["room_id"] == room["id"]