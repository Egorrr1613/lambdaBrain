from ASD_FIRST.four_lesson_stack.base_stack import Stack
from ASD_FIRST.six_lesson_deque.deque import Deque
from ASD_FIRST.six_lesson_deque.dyn_array_by_dec import DynArrayByDec


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


class DequeByDynArray:
    """Решение 5 дополнительного задания
    Реализовал через циклическую работу с индексами динамического массива,
        с учетом расширения и релокации при заполнении доступного пространства"""

    def __init__(self):
        self.array = DynArrayByDec()
        self.head_index = 0
        self.tail_index = 0

    def addFront(self, item):
        if self.size() == 0:
            self.head_index = 0
            self.tail_index = 0
            self.array[self.head_index] = item
            return

        if self.size() == self.array.capacity:
            self.array.head_index = self.head_index
            self.array.insert(i=0, itm=item)
            self.head_index = 0
            self.tail_index = self.size() - 1
            return

        if self.size() >= 1:
            next_head_index = self.array.capacity - 1 if self.head_index - 1 < 0 else self.head_index - 1
            self.array[next_head_index] = item
            self.head_index = next_head_index

    def addTail(self, item):
        if self.size() == 0:
            self.head_index = 0
            self.tail_index = 0
            self.array[self.tail_index] = item
            return

        if self.size() == self.array.capacity:
            self.array.head_index = self.head_index
            self.array.insert(i=self.array.capacity, itm=item)
            self.head_index = 0
            self.tail_index = self.size()
            return

        if self.size() >= 1:
            next_tail_index = 0 if self.tail_index + 1 == self.array.capacity else self.tail_index + 1
            self.array.insert(i=next_tail_index, itm=item)
            self.tail_index = next_tail_index

    def removeFront(self):
        if self.size() == 0:
            return None
        if self.size() == 1:
            result = self.array[self.head_index]
            self.array.delete(self.head_index)
            self.head_index = 0
            self.tail_index = 0
            return result
        if self.size() > 1:
            result = self.array[self.head_index]
            self.array.delete(self.head_index)
            if self.head_index > self.tail_index:
                self.head_index = 0 if self.head_index + 1 >= self.array.capacity else self.head_index + 1
            else:
                self.head_index = 0
                self.tail_index -= 1
            return result
        return ('Error',)

    def removeTail(self):
        if self.size() == 0:
            return None
        if self.size() == 1:
            result = self.array[self.tail_index]
            self.array.delete(self.tail_index)
            self.head_index = 0
            self.tail_index = 0
            return result
        if self.size() > 1:
            result = self.array[self.tail_index]
            self.array.delete(self.tail_index)
            self.tail_index = self.array.capacity - 1 if self.tail_index - 1 < 0 else self.tail_index - 1
            return result
        return ('Error',)

    def size(self):
        return len(self.array)


def is_balance(input_str: str):
    """Решение 6 дополнительного задания.

    Это задание ранее уже встречалось на курсе.
    Задавалось в 4 уроке по теме "Стек", доп задание 4.5 и 4.6
    Ниже продублировал старое решение"""

    stack = Stack()
    reverse_symbol = {")": "(", "}": "{", "]": "["}
    for i in input_str:
        if i in ["(", "{", "["]:
            stack.push(i)
            continue
        if i in [")", "}", "]"] and stack.size() > 0:
            rm_symbol = stack.pop()
            if rm_symbol != reverse_symbol[i]:
                return False
            continue
        return False

    if stack.size() == 0:
        return True
    return False
