from ..models.Post import Post

def seed(repo):
    post1 = Post(5, "Title","This is the content", "ownerrr", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    text = "Text textText textText textText textText textText textText textText textText textText textText textText textText text \
        Text textText textText textText textText textText textText textText textText textText textText textText textText text"
    post2 = Post(10, "This is an article", text, "Another owner", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    post3 = Post(1, "This is a seeded article", text, "Yet another owner", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    repo.create(post1)
    repo.create(post2)
    repo.create(post3)
    return repo