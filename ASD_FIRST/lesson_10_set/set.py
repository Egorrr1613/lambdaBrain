from __future__ import annotations
from typing import Any


class PowerSet:
    def __init__(self):
        self.capacity = 20_011
        self.slots = [[] for _ in range(self.capacity)]
        self.count_el = 0

    def hash_fun(self, value: str) -> int:
        return sum(i for i in str.encode(value)) % self.capacity

    def size(self) -> int:
        return self.count_el

    def put(self, value: Any) -> None:
        if value in self.slots[index := self.hash_fun(value)]:
            return
        self.slots[index].append(value)
        self.count_el += 1

    def get(self, value: Any) -> bool:
        return value in self.slots[self.hash_fun(value)]

    def remove(self, value: Any) -> bool:
        if value in self.slots[index := self.hash_fun(value)]:
            self.slots[index].remove(value)
            self.count_el -= 1
            return True
        return False

    def intersection(self, set2: PowerSet) -> PowerSet:
        result_set = PowerSet()
        for slot in self.slots:
            for el in slot:
                if set2.get(el):
                    result_set.put(el)
        return result_set

    def union(self, set2: PowerSet) -> PowerSet:
        result_set = set2
        for slot in self.slots:
            for el in slot:
                if not result_set.get(el):
                    result_set.put(el)
        return result_set

    def difference(self, set2: PowerSet) -> PowerSet:
        result_set = PowerSet()
        for slot in self.slots:
            for el in slot:
                if not set2.get(el):
                    result_set.put(el)
        return result_set

    def issubset(self, set2: PowerSet) -> bool:
        for slot in set2.slots:
            for el in slot:
                if not self.get(el):
                    return False
        return True

    def equals(self, set2: PowerSet) -> bool:
        if self.size() != set2.size():
            return False
        for slot in self.slots:
            for el in slot:
                if not set2.get(el):
                    return False
        return True

