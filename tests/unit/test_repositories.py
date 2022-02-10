from operator import pos
from typing import ValuesView
from website.repository.postsRepository import PostsRepository
from website.models.Post import Post
import pytest

post = Post(1, "Post1",
                "Duis sit amet turpis a ante blandit tristique vitae non nisl. Nullam non laoreet magna. Donec volutpat aliquet \
                lacus ut egestas. Praesent in leo eget nisl vehicula viverra sed vel tortor. Praesent eget vehicula sem, eu feugiat \
                tellus. Nulla et nibh lacinia neque fermentum tristique. Aliquam feugiat blandit placerat. Phasellus elit nunc, \
                sagittis at aliquet nec, consequat et elit. Vivamus feugiat libero quis turpis tincidunt tempus. Ut luctus sem ut \
                quam semper aliquam. Curabitur pellentesque, eros et tempus ultrices, nulla metus cursus metus, quis vestibulum \
                dolor ipsum vestibulum felis. Suspendisse pellentesque eu augue non porttitor. Sed tempus, dolor eu convallis \
                laoreet, mi velit vehicula felis, non imperdiet mauris sem eget dui. Sed sagittis ligula sed dignissim euismod. \
                Curabitur magna dui, pellentesque eget suscipit ac, euismod eget erat."
                ,"Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")

def test_new_post_repository():
    repo = PostsRepository()
    assert repo.counter == 0

def test_findById():
    repo = PostsRepository()
    repo.create(post)
    assert repo.counter == 1
    assert repo.findById(1) == post

def test_findById_post_shouldReturnNone():
    repo = PostsRepository()
    repo.create(post)
    assert repo.counter == 1
    assert repo.findById(2) == None

def test_findById_shouldReturnError():
    repo = PostsRepository()
    with pytest.raises(TypeError):
        assert repo.findById() == None

def test_getAll():
    repo = PostsRepository()
    repo.create(post)
    assert repo.getAll() == repo.repo

def test_getAll_ShouldReturnError():
    repo = PostsRepository()
    repo.create(post)
    repo2 = PostsRepository()
    assert repo.getAll() != repo2.getAll()

def test_getAllPreviews():
    repo = PostsRepository()
    repo.create(post)
    tempRepo = repo.getAllPreviews() 
    assert len(tempRepo[0].content) == 460
    assert tempRepo[0].title == "Post1"

def test_assignId_Black_Box():
    repo = PostsRepository()
    post1 = Post(5, "Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    repo.create(post)
    repo.create(post1)
    assert repo.repo[0].id == 1
    assert repo.repo[1].id == 2

def test_assignId_Black_Box():
    repo = PostsRepository()
    post1 = Post(5, "Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    repo.create(post)
    repo.create(post1)
    assert repo.repo[0].id == 1
    assert repo.repo[1].id == 2

def test_assignOwner_Black_Box():
    repo = PostsRepository()
    post1 = Post(5, "Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    repo.create(post)
    repo.create(post1)
    assert repo.repo[0].owner == "Owner 1"
    assert repo.repo[1].owner == "Owner 2"

def test_create_directly():
    repo = PostsRepository()
    post1 = Post(5, "Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    repo.create(post)
    repo.create(post1)
    assert repo.repo[1].id == 2
    assert repo.repo[1].title == "Post1"
    assert repo.repo[1].content == "This is a post."
    assert repo.repo[1].owner == "Owner 2"
    assert repo.repo[1].created_at == "2022-02-08 04:07:07"
    assert repo.repo[1].modified_at == "2022-02-08 04:07:07"

def test_update():
    repo = PostsRepository()
    repo.create(post)
    post.title = "Post name updated"
    repo.update(post)
    assert repo.repo[0].id == 1
    assert repo.repo[0].title == "Post name updated"
    assert repo.repo[0].content == post.content
    assert repo.repo[0].owner == "Owner 1"
    assert repo.repo[0].created_at == "2022-02-08 04:07:07"
    assert repo.repo[0].modified_at == "2022-02-08 04:07:07"

def test_update_shouldReturnError():
    repo = PostsRepository()
    post1 = Post(5, "Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    repo.create(post)
    with pytest.raises(ValueError):
        assert repo.update(post1)


def test_delete():
    repo = PostsRepository()
    repo.create(post)
    repo.delete(post)
    assert len(repo.repo) == 0

def test_delete_withMorePosts():
    repo = PostsRepository()
    repo.create(post)
    post1 = Post(5, "Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    repo.create(post1)
    repo.delete(post)
    assert len(repo.repo) == 1

def test_delete():
    repo = PostsRepository()
    repo.create(post)
    post1 = Post(5, "Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    with pytest.raises(ValueError):
        assert repo.delete(post1)