class Repository:
    def __init__(self):
        self.repo = list()

    def findById(self, id):
        if not (id in self):
            return None
        else:
            return self.repo[id]
        
    def findAll(self):
        return self.repo

    def save(self, item):
        self.repo.append(item)
        return True
        