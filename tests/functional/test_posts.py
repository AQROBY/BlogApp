from tests.conftest import app
import pytest
from website.models.Post import Post

def test_posts_index_works(client, app):
    response = client.get('posts/')
    assert response.status_code == 200

def test_posts_index_try_post_method_should_fail(client, app):
    response = client.post('posts/')
    assert response.status_code == 405

def test_posts_index_seededContent_exists(client, app):
    response = client.get('posts/').get_data(as_text=True)
    assert "This is an article" in response
    assert "Minimal Post" in response

def test_posts_create_works(client, app):
    response = client.get('posts/create')
    assert response.status_code == 200

def test_posts_create_post(client, app):
    post = client.post('posts/create', data={"title": "Fallout 4", "content": "One more tommorow"})
    response = client.get('posts/').get_data(as_text=True)
    assert "Fallout 4" in response
    assert "One more tommorow" in response
    assert "Post created!" in response

def test_posts_create_flashMessage_titleEmptyError(client, app):
    post = client.post('posts/create', data={"content": "One more tommorow"})
    response = post.get_data(as_text=True)
    assert "Title cannot be empty" in response
    assert "One more tommorow" in response

def test_posts_create_flashMessage_contentEmptyError(client, app):
    post = client.post('posts/create', data={"title": "Fallout 4"})
    response = post.get_data(as_text=True)
    assert "Content cannot be empty" in response
    assert "Fallout 4" in response

def test_posts_read(client, app):
    post = client.get('posts/4')
    response = post.get_data(as_text=True)
    assert post.status_code == 200
    assert "Fallout 4" in response
    assert "One more tommorow" in response
    assert "Anything else content contetttttttnnttt" not in response

def test_posts_read_wrongId(client, app):
    post = client.get('posts/50')
    response = post.get_data(as_text=True)
    assert post.status_code == 302
    responseFromIndex = client.get('posts/').get_data(as_text=True)
    assert "Post does not exist." in responseFromIndex