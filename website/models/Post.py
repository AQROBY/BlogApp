class Post:
    def __init__(self, id, title, content, owner, created_at, modified_at):
        self.id = id
        self.title = title
        self.content = content
        self.owner = owner
        self.created_at = created_at
        self.modified_at = modified_at

    def previewContent(self):
        return "   " + self.content[0:260] + "..."

    def previewBigContent(self):
        return "   " + self.content[0:460] + "..."