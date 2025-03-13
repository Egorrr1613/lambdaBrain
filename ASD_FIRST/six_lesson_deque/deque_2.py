
from ASD_FIRST.six_lesson_deque.deque import Deque


def is_palindrome(checked_str: str) -> bool:
    """Решение 3 дополнительного задания"""
    if len(checked_str) < 2:
        return True
    d = Deque()
    for ch in checked_str:
        if ch == " ":
            continue
        d.addTail(ch.lower())

    while d.size() != 0:
        left = d.removeFront()
        right = d.removeTail()
        if left is not None and right is None and d.size() == 0:
            return True
        if left != right:
            return False
    return True


class DequeWithGetMin:
    """Решение 4 дополнительного задания

        Использую переменную для хранения минимального элемента.
        Если этот элемент удаляется - находим по внутреннему массиву перебором новый элемент
    """

    def __init__(self):
        self.array = []
        self.min_el = None

    def addFront(self, item):
        self.array.insert(0, item)
        self.check_add_element_by_min(item, )

    def addTail(self, item):
        self.array.insert(self.size(), item)
        self.check_add_element_by_min(item, )

    def removeFront(self):
        if self.size() == 0:
            return None
        result = self.array.pop(0)
        self.check_del_element_by_min(result)
        return result

    def removeTail(self):
        if self.size() == 0:
            return None
        result = self.array.pop(self.size() - 1)
        self.check_del_element_by_min(result)
        return result

    def size(self):
        return len(self.array)

    def min(self):
        return self.min_el

    def check_add_element_by_min(self, element):
        if not isinstance(element, int):
            return

        if self.min_el is None:
            self.min_el = element
            return
        if self.min_el > element:
            self.min_el = element

    def check_del_element_by_min(self, element):
        if not isinstance(element, int):
            return
        if element < self.min_el:
            return ('Incorrect state',)
        if self.size() == 0:
            self.min_el = None
            return
        if element == self.min_el:
            self.min_el = self.find_min_el()

    def find_min_el(self):
        res = self.array[0]
        for i in range(self.size()):
            if self.array[i] < res:
                res = self.array[i]
        return res
