class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 3

    def __seek_slot__(self, value: str) -> int:
        index = self.hash_fun(value)
        for _ in range(self.size // self.step + 1):
            if self.slots[index] is None or self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
        return self.hash_fun(value)

    def hash_fun(self, key: str) -> int:
        return sum(i for i in str.encode(key)) % self.size

    def is_key(self, key: str) -> bool:
        return key in self.slots

    def put(self, key: str, value) -> None | int:
        if None not in self.slots:
            return None
        index = self.__seek_slot__(key)
        self.slots[index] = key
        self.values[index] = value
        return index

    def get(self, key: str):
        if not self.is_key(key):
            return None
        return self.values[self.__seek_slot__(key)]
