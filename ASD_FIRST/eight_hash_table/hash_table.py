class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str) -> int:
        return sum(i for i in str.encode(value)) % self.size

    def seek_slot(self, value: str) -> int | None:
        index = self.hash_fun(value)
        for _ in range(self.size // self.step + 1):
            if self.slots[index] is None or self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
        return None

    def put(self, value: str) -> int | None:
        if (index := self.seek_slot(value)) is not None:
            self.slots[index] = value
            return index
        return None

    def find(self, value) -> int | None:
        index = self.hash_fun(value)
        for _ in range(self.size // self.step + 1):
            if self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
        return None
