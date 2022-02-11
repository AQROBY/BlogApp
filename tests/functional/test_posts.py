from tests.conftest import app
import pytest
from website.models.Post import Post

def test_posts_index(client, app):
    response = client.get('posts/')
    assert response.status_code == 200

def test_posts_index(client, app):
    response = client.get('posts/').data
    text = "Text textText textText textText textText textText textText textText textText textText textText textText textText text \
    Text textText textText textText textText textText textText textText textText textText textText textText textText text"
    post = Post(3, "This is a seeded article", text, "Owner 3", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    assert post in response.data