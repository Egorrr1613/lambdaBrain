class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.byte_array = 0

    def _base_hash_fun_(self, hash_const: int, value: str) -> int:
        result = 0
        for char in value:
            result = (result * hash_const + ord(char)) % self.filter_len
        return 1 << result

    def hash1(self, str1) -> int:
        hash_const = 17
        return self._base_hash_fun_(hash_const=hash_const, value=str1)

    def hash2(self, str1) -> int:
        hash_const = 223
        return self._base_hash_fun_(hash_const=hash_const, value=str1)

    def add(self, str1):
        add_mask = self.hash1(str1) | self.hash2(str1)
        self.byte_array |= add_mask

    def is_value(self, str1):
        validate_mask = self.hash1(str1) | self.hash2(str1)
        return (self.byte_array & validate_mask) != 0
