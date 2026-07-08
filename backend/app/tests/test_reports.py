def test_general_report(client):

    response = client.get(
        "/reports/general"
    )

    assert response.status_code == 200