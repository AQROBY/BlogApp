class PostsRepository:
    def __init__(self):
        self.repo = list()
        self.counter = 0

    def findById(self, id):
        for post in self.repo:
            if id == post.id:
                return post
        else:
            return None
        
    def getAll(self):
        return self.repo

    def __assignId(self):
        self.counter += 1
        return self.counter

    def __assignOwner(self):
        return "Owner " + str(self.counter)

    def create(self, item):
        item.id = self.__assignId()
        item.owner = self.__assignOwner()
        self.repo.append(item)
        return True

    def update(self, item):
        self.repo.remove(item)
        self.repo.append(item)
        return True

    def delete(self, post):
        self.repo.remove(post)