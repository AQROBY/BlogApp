class Post:
    def __init__(self, idPost, title, content, owner, created_at, modified_at):
        self.id = idPost
        self.title = title
        self.content = content
        self.owner = owner
        self.created_at = created_at
        self.modified_at = modified_at