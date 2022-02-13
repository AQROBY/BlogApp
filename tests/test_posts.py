def test_index_works(client):
    response = client.get('posts/')
    assert response.status_code == 200

def test_index_try_post_method_should_fail(client):
    response = client.post('posts/')
    assert response.status_code == 405

def test_index_seededContent_exists(client):
    response = client.get('posts/').get_data(as_text=True)
    assert "This is an article" in response
    assert "Minimal Post" in response

def test_create_works(client):
    response = client.get('posts/create')
    assert response.status_code == 200

def test_create_post(client):
    client.post('posts/create', data={"title": "Fallout 4", "content": "One more tommorow"})
    response = client.get('posts/').get_data(as_text=True)
    assert "Fallout 4" in response
    assert "One more tommorow" in response
    assert "Post created!" in response

def test_create_titleEmptyError(client):
    post = client.post('posts/create', data={"content": "One more tommorow"})
    response = post.get_data(as_text=True)
    assert "Title cannot be empty" in response
    assert "One more tommorow" in response

def test_create_contentEmptyError(client):
    post = client.post('posts/create', data={"title": "Fallout 4"})
    response = post.get_data(as_text=True)
    assert "Content cannot be empty" in response
    assert "Fallout 4" in response

def test_read_works(client):
    response = client.get('posts/3')
    assert response.status_code == 200

def test_create_z_read_post(client):
    post = client.get('posts/4')
    response = post.get_data(as_text=True)
    assert post.status_code == 200
    assert "Fallout 4" in response
    assert "One more tommorow" in response
    assert "Anything else content contetttttttnnttt" not in response

def test_read_wrongId(client):
    post = client.get('posts/50')
    assert post.status_code == 302
    responseFromIndex = client.get('posts/').get_data(as_text=True)
    assert "Post does not exist." in responseFromIndex

def test_edit_works(client):
    post = client.get('posts/edit/4')
    assert post.status_code == 200

def test_edit_post(client):
    post = client.post('posts/edit/4', data={"title": "Fallout 5", "content": "One more tommorow"})
    response = client.get('posts/').get_data(as_text=True)
    assert "Fallout 5" in response
    assert "One more tommorow" in response
    assert "Post edited" in response
    assert "Fallout 4" not in response
    assert post.status_code == 302

def test_edit_wrongid(client):
    post = client.post('posts/edit/50', data={"title": "Fallout 5", "content": "One more tommorow"})
    assert post.status_code == 302
    responseFromIndex = client.get('posts/').get_data(as_text=True)
    assert "Post does not exist." in responseFromIndex

def test_edit_titleEmptyError(client):
    post = client.post('posts/edit/3', data={"title":"", "content": "One more tommorow"})
    response = post.get_data(as_text=True)
    assert "Title cannot be empty" in response

def test_edit_contentEmptyError(client):
    post = client.post('posts/edit/3', data={"title":"Fallout 5", "content": ""})
    response = post.get_data(as_text=True)
    assert "Content cannot be empty" in response

def test_delete_works(client):
    client.post('posts/create', data={"title": "Fallout 4", "content": "One more tommorow"})
    post = client.get('posts/delete/5')
    responseFromIndex = client.get('posts/').get_data(as_text=True)
    assert post.status_code == 302
    assert "Post deleted!" in responseFromIndex

def test_delete_wrongId(client):
    post = client.get('posts/delete/700')
    responseFromIndex = client.get('posts/').get_data(as_text=True)
    assert post.status_code == 302
    assert "Post does not exist." in responseFromIndex