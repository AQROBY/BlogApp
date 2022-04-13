class PreviewPost:
    def __init__(self, post):
        self.id = post.id
        self.title = post.title
        self.content = post.content[0:400]
        self.owner = post.owner
        self.created_at = post.created_at
        self.modified_at = post.modified_at
