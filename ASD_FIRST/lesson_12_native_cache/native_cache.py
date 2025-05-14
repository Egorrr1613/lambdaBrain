class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.step = 3

    def __is_key__(self, key: str | None) -> bool:
        return key in self.slots

    def __seek_slot__(self, key: str) -> int | None:
        index = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[index] is None or self.slots[index] == key:
                return index
            index = (index + self.step) % self.size
        return None

    def hash_fun(self, key: str) -> int:
        return sum(i for i in str.encode(key)) % self.size

    def put(self, key: str, value) -> int | None:
        if not self.__is_key__(None):
            index_to_del = self.hits.index(min(self.hits))
            self.hits[index_to_del] = 0
            self.slots[index_to_del] = key
            self.values[index_to_del] = value
            return index_to_del

        index = self.__seek_slot__(key)
        self.slots[index] = key
        self.values[index] = value
        return index

    def get(self, key: str) -> str | None:
        if not self.__is_key__(key):
            return None
        key_index = self.__seek_slot__(key)
        self.hits[key_index] += 1
        return self.values[key_index]

