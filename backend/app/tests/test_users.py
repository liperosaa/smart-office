def test_create_user(client):

    response = client.post(
        "/users/",
        json={
            "nome": "Teste Usuario",
            "email": "teste_usuario_001@email.com",
            "cargo": "Administrador",
            "senha": "123456",
            "ativo": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["nome"] == "Teste Usuario"
    assert data["email"] == "teste_usuario_001@email.com"