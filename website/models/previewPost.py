from .Post import Post


class PreviewPost(Post):
    def __init__(self, post):
        self.id = post.id
        self.title = post.title
        self.content = post.content[0:460]
        self.owner = post.owner
        self.created_at = post.created_at
        self.modified_at = post.modified_at

    def previewContent(self):
        if len(self.content) < 260:
            return self.content

        return self.content[0:260] + "..."

    def previewBigContent(self):
        if len(self.content) < 460:
            return self.content
        return self.content[0:460] + "..."
