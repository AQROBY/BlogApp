from ..models.previewPost import PreviewPost

class PostsRepository:
    def __init__(self):
        self.repo = list()
        self.counter = 0

    def findById(self, idPost):
        for post in self.repo:
            if idPost == post.id:
                return post
        return None
        
    def getAll(self):
        return self.repo

    def getAllPreviews(self):
        tempRepo = list()
        for post in self.repo:
            tempRepo.append(PreviewPost(post))
        return tempRepo

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
        index = self.repo.index(item)
        self.repo.remove(item)
        self.repo.insert(index, item)
        return True

    def delete(self, post):
        self.repo.remove(post)