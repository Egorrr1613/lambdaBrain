class Deque:
    def __init__(self):
        self.array = []

    def addFront(self, item):
        self.array.insert(0, item)

    def addTail(self, item):
        self.array.insert(self.size(), item)

    def removeFront(self):
        if self.size() == 0:
            return None
        return self.array.pop(0)

    def removeTail(self):
        if self.size() == 0:
            return None
        return self.array.pop(self.size() - 1)

    def size(self):
        return len(self.array)
