class Repository:
    def __init__(self):
        self.repo = list()

    def findById(self, id):
        for post in self.repo:
            if id == post.id:
                return post
        else:
            return None
        
    def findAll(self):
        return self.repo

    def save(self, item):
        self.repo.append(item)
        return True
        