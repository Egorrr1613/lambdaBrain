from ASD_FIRST.lesson_4_stack.base_stack import Stack
from ASD_FIRST.lesson_6_deque.deque import Deque
from ASD_FIRST.lesson_6_deque.dyn_array_by_dec import DynArrayByDec


def is_palindrome(checked_str: str) -> bool:
    """
    Задание: №6
    Номер задачи из задания: №3
    Краткое название: "Функция, с помощью deque проверяет строку на палиндром"
    Сложность: size - O(n)/time - O(n)

    Рефлексия: Решил сам аналогично алгоритму из ответов.
    """
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
        if (left is not None) and (right is None) and d.size() == 0:
            return True
        if left != right:
            return False
    return True


class DequeWithGetMin:
    """
    Задание: №6
    Номер задачи из задания: №4
    Краткое название: "Минимальный элемент деки за O(1)"
    Сложность: size - O(1)/time - O(1)

    Рефлексия: Сам смог придумать "глупое" решение,
        когда в переменной хранится текущий минимальный элемент.
        Если элемент удаляется - дека перебирается заново в поисках нового минимума.

    Кажется в предлагаемом вами алгоритме есть ошибка.
        Например, добавим "5" в очередь:
            После добавления: main_deq = [5] / min_deq = [5]
        Добавим в очередь "3":
            После добавления: main_deq = [5, 3] / min_deq = [3]
        Выполним pop():
            После удаления: main_deq = [5] / min_deq = []
    """

    def __init__(self):
        self.array = []
        self.min_el = None

    def addFront(self, item):
        self.array.insert(0, item)
        self.check_add_element_by_min(
            item,
        )

    def addTail(self, item):
        self.array.insert(self.size(), item)
        self.check_add_element_by_min(
            item,
        )

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
        self.min_el = min(self.min_el, element)

    def check_del_element_by_min(self, element) -> None | tuple:
        if not isinstance(element, int):
            return None
        if element < self.min_el:
            return ("Incorrect state",)
        if self.size() == 0:
            self.min_el = None
            return None
        if element == self.min_el:
            self.min_el = self.find_min_el()
            return None
        return ("Error",)

    def find_min_el(self):
        res = self.array[0]
        for i in range(self.size()):
            if self.array[i] < res:
                res = self.array[i]
        return res


class DequeByDynArray:
    """
    Задание: №6
    Номер задачи из задания: №5
    Краткое название: "Двусторонняя очередь на базе динамического массива"
    Сложность: без оценки

    Рефлексия: Самостоятельно реализовал через "кольцевую" работу с индексами динамического массива,
        с учетом расширения и релокации при заполнении доступного пространства.
        В отдельный модуль dyn_array_by_dec.py вынес реализацию динамического массива для данной задачи.
        Для реализации оптимальной работы с индексами в динамическом массиве реализовал сдвиг элементов при релокации,
        таким образом, чтобы новый массив заполнялся с head элемента очереди.
    """

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
            next_head_index = (
                self.array.capacity - 1
                if self.head_index - 1 < 0
                else self.head_index - 1
            )
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
            next_tail_index = (
                0 if self.tail_index + 1 == self.array.capacity else self.tail_index + 1
            )
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
                self.head_index = (
                    0
                    if self.head_index + 1 >= self.array.capacity
                    else self.head_index + 1
                )
            else:
                self.head_index = 0
                self.tail_index -= 1
            return result
        return ("Error",)

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
            self.tail_index = (
                self.array.capacity - 1
                if self.tail_index - 1 < 0
                else self.tail_index - 1
            )
            return result
        return ("Error",)

    def size(self):
        return len(self.array)


def is_balance(input_str: str):
    """
    Задание: №6
    Номер задачи из задания: №6
    Краткое название: "Функция для определения сбалансирована ли строка из скобок: (), {}, []"
    Сложность: size - O(n)/time - O(n)

    Рефлексия: Это задание ранее уже встречалось на курсе.
    Задавалось в 4 уроке по теме "Стек", доп задание 4.5 и 4.6
    Ниже продублировал старое решение.
    """

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

