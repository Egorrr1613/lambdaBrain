from __future__ import annotations
from typing import Any


class PowerSet:
    def __init__(self):
        self.capacity = 25
        self.slots = [[] for _ in range(self.capacity)]
        self.count_el = 0

    def hash_fun(self, value: Any) -> int:
        return sum(i for i in str.encode(str(value))) % self.capacity

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
        result_set = PowerSet()
        for slot in self.slots:
            for el in slot:
                result_set.put(el)
        for slot in set2.slots:
            for el in slot:
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

    def decart_product(self, set2: PowerSet) -> PowerSet:
        """
        Задание: №10
        Номер задачи из задания: №4
        Краткое название: "Реализуйте декартово произведения множеств"
        Сложность: size - O(n) / time - O(n^2)

        Рефлексия: Реализовал "в лоб", перебором всех значений.
            Мой алгоритм совпал с тем, который был предложен в качестве рекомендованного решения.
            Чуть ниже, в методе decart_product_by_list реализовал расширенный вариант
            для произведения произвольного количества множеств.
        """
        result_set = PowerSet()

        if self.size() == 0 or set2.size() == 0:
            assert (
                False
            ), "Incorrect set size. Current and param set must 1 or more elements"

        for slot in self.slots:
            for el1 in slot:
                for slot2 in set2.slots:
                    for el2 in slot2:
                        if isinstance(el1, str) and isinstance(el2, str):
                            result_set.put((el1, el2))
                            continue
                        if isinstance(el1, str) and isinstance(el2, tuple):
                            result_set.put((el1, *el2))
                            continue
                        assert False, f"Incorrect state. \nel1: {el1}\nel2: {el2}"

        return result_set

    def decart_product_by_list(self, list_sets: list[PowerSet]) -> PowerSet:
        if self.size() == 0 or len(list_sets) == 0:
            assert (
                False
            ), "Incorrect set size. Current and param set must 1 or more elements"

        if len(list_sets) == 1:
            return self.decart_product(list_sets[0])

        list_decart = self._recursion_decart_(result_set=list_sets[0].union(PowerSet()), list_sets=list_sets,
                                              index_set=1)
        return self.decart_product(list_decart)

    def _recursion_decart_(self, result_set: PowerSet, list_sets: list[PowerSet], index_set: int) -> PowerSet:
        if index_set == len(list_sets):
            return result_set
        result_set = result_set.decart_product(list_sets[index_set])
        return self._recursion_decart_(result_set=result_set, list_sets=list_sets, index_set=index_set + 1)

    def multi_intersection(self, sets: list[PowerSet]) -> PowerSet:
        """
        Задание: №10
        Номер задачи из задания: №5
        Краткое название: "Пересечение любого количества множеств"
        Сложность: size - O(n * m) / time - O(m*(n^2)),
            где m - количество элементов в массиве sets

        Рефлексия:
        """
        result_set = PowerSet()
        for i, iteration_set in enumerate(sets):
            if i == 0:
                for slot in self.slots:
                    for el in slot:
                        if sets[0].get(el):
                            result_set.put(el)
                continue

            buffer_set = PowerSet()
            for slot in result_set.slots:
                for el in slot:
                    if iteration_set.get(el):
                        buffer_set.put(el)
            result_set = buffer_set

        return result_set


class Bag:
    """
    Задание: №10
    Номер задачи из задания: №6
    Краткое название: "Множество, в котором каждый элемент может присутствовать несколько раз"
    Сложность:
        * count: size - O(1) / time - O(n)

    Рефлексия: Необходимо было реализовать метод, позволяющий списком получить все элементы и то,
        сколько раз они встречаются.
        Реализовал как хеш таблицу, где каждый элемент хранит значение и свой счетчик.
        После ознакомления с рекомендациями увидел, что мое решение совпадает с рекомендованным.
    """

    def __init__(self):
        self.capacity = 17
        self.slots = [[] for _ in range(self.capacity)]
        self.count_el = 0

    def hash_fun(self, value: str) -> int:
        return sum(i for i in str.encode(value)) % self.capacity

    def size(self) -> int:
        return self.count_el

    def put(self, value: str) -> None:
        if el := self.__get_element__(value):
            el[1] += 1
            self.count_el += 1
            return
        self.slots[self.hash_fun(value)].append([value, 1])
        self.count_el += 1

    def __get_element__(self, value) -> list | None:
        for el in self.slots[self.hash_fun(value)]:
            if el[0] == value:
                return el
        return None

    def get(self, value: str) -> bool:
        if self.__get_element__(value):
            return True
        return False

    def count(self, value: str) -> int:
        for el in self.slots[self.hash_fun(value)]:
            if el[0] == value:
                return el[1]
        return 0

    def remove(self, value: str) -> bool:
        if not (el := self.__get_element__(value)):
            return False
        if el[1] == 1:
            self.slots[self.hash_fun(value)].remove([value, 1])
            self.count_el -= 1
            return True
        if el[1] > 1:
            el[1] -= 1
            self.count_el -= 1
            return True
        assert False, f"Incorrect state, el index: {el[1]} less than 1"

    def get_all_el(self) -> list:
        result = []
        for slot in self.slots:
            for el in slot:
                result.append(el)
        return result

    def intersection(self, set2: Bag) -> Bag:
        result_set = Bag()
        for slot in self.slots:
            for el in slot:
                if set2.get(el[0]):
                    result_set.put(el[0])
        return result_set

    def union(self, set2: Bag) -> Bag:
        result_set = set2
        for slot in self.slots:
            for el in slot:
                if not result_set.get(el[0]):
                    result_set.put(el[0])
        return result_set

    def difference(self, set2: Bag) -> Bag:
        result_set = Bag()
        for slot in self.slots:
            for el in slot:
                if not set2.get(el[0]):
                    result_set.put(el[0])
        return result_set

    def issubset(self, set2: Bag) -> bool:
        for slot in set2.slots:
            for el in slot:
                if not self.get(el[0]):
                    return False
        return True

    def equals(self, set2: Bag) -> bool:
        if self.size() != set2.size():
            return False
        for slot in self.slots:
            for el in slot:
                if not set2.get(el[0]):
                    return False
        return True
