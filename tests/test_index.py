def test_index(client):
    response = client.get('/')
    assert response.status_code == 302

def test_index_redirect(client):
    response = client.get('/')
    assert '/posts' in response.location