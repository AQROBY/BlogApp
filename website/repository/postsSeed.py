from ..models.Post import Post

def seed(repo):
    post1 = Post(5, "Title","This is the content", "ownerrr", 11111, 12312312)
    text = "Text textText textText textText textText textText textText textText textText textText textText textText textText text \
        Text textText textText textText textText textText textText textText textText textText textText textText textText text"
    post2 = Post(10, "This is an article", text, "Another owner", 11111, 12312312)
    post3 = Post(1, "This is a seeded article", text, "Yet another owner", 222, 123333312312)
    repo.create(post1)
    repo.create(post2)
    repo.create(post3)
    return repo