class Repository:
    def __init__(self):
        self.repo = list()
        self.counter = 0

    def findById(self, id):
        for post in self.repo:
            if id == post.id:
                return post
        else:
            return None
        
    def findAll(self):
        return self.repo

    def assignId(self):
        self.counter += 1
        return self.counter

    def assignOwner(self):
        return "Owner " + str(self.counter)

    def save(self, item):
        item.id = self.assignId()
        item.owner = self.assignOwner()
        self.repo.append(item)
        return True

    def delete(self, post):
        self.repo.remove(post)