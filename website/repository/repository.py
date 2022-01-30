class repository:
    def __init__(self, id):
        self.id = id

    def add(self, content):
        print(self.id)
        print(self.contents)
        self.contents.append(content)
        print(self.contents)
