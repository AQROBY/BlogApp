from tests.conftest import app

def test_index(client, app):
    response = client.get('/')
    assert response.status_code == 302

def test_index_redirect(client, app):
    response = client.get('/')
    assert '/posts' in response.location