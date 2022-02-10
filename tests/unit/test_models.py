from website.models.Post import Post
from website.models.previewPost import PreviewPost
import pytest


def test_new_post():
    post = Post(1, "Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    assert post.id == 1
    assert post.title == "Post1"
    assert post.content == "This is a post."
    assert post.owner == "Aurel"
    assert post.created_at == "2022-02-08 04:07:07"
    assert post.modified_at == "2022-02-08 04:07:07"

def test_new_post_wihout_a_parameter_shouldReturnTypeError():
    with pytest.raises(TypeError):
        post = Post("Post1", "This is a post.", "Aurel", "2022-02-08 04:07:07", "2022-02-08 04:07:07")

def test_new_previewPost():
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
        previewPost = PreviewPost(post)
        assert len(previewPost.content) == 460