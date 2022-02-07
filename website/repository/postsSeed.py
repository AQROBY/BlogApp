from ..models.Post import Post

def seed(repo):
    post1 = Post("Title","This is the content",11111, 12312312)
    text = "Text textText textText textText textText textText textText textText textText textText textText textText textText text \
        Text textText textText textText textText textText textText textText textText textText textText textText textText text"
    post2 = Post("This is an article", text, 11111, 12312312)
    post3 = Post("This is a seeded article", text, 222, 123333312312)
    repo.create(post1)
    repo.create(post2)
    repo.create(post3)
    return repo