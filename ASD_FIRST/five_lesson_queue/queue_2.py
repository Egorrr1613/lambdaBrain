import ctypes
from ASD_FIRST.five_lesson_queue.queue import Queue
from ASD_FIRST.four_lesson_stack.base_stack import Stack


def circulation_queue(input_q: Queue, count_element_shift: int) -> None:
    """Решение 3 дополнительного задания"""
    if input_q.size() < 2:
        return
    for _ in range(count_element_shift):
        buffer = input_q.dequeue()
        input_q.enqueue(buffer)


class QueueByTwoStack:
    """Решение 4 дополнительного задания"""

    def __init__(self):
        self._first_stack_ = Stack()
        self._second_stack_ = Stack()
        self.element_count = 0

    def enqueue(self, value) -> None:
        self._first_stack_.push(value)
        self.element_count += 1

    def dequeue(self):
        if self.element_count == 0:
            return None

        if self._second_stack_.size() == 0:
            for _ in range(self._first_stack_.size()):
                self._second_stack_.push(self._first_stack_.pop())
        self.element_count -= 1
        return self._second_stack_.pop()

    def size(self) -> int:
        return self.element_count


def revert_queue(input_queue: Queue) -> Queue:
    """Решение 5 дополнительного задания"""
    buffer_stack = Stack()
    for _ in range(input_queue.size()):
        buffer_stack.push(input_queue.dequeue())

    for _ in range(buffer_stack.size()):
        input_queue.enqueue(buffer_stack.pop())

    return input_queue


class CycleBufferQueue:
    """Решение 6 дополнительного задания"""

    def __init__(self, size):
        if size <= 0:
            raise ValueError(
                'Incorrect value by param "size". Size must be great than 0'
            )
        self.max_count_el = size
        self.array = (self.max_count_el * ctypes.py_object)()
        self.count_free_el = self.max_count_el
        self.tail_index = None
        self.head_index = None

    def enqueue(self, value) -> None | tuple:
        if self.count_free_el == 0:
            return None

        if self.count_free_el == self.max_count_el:
            self.tail_index = 0
            self.head_index = 0
            self.array[self.head_index] = value
            self.count_free_el -= 1
            return None

        if self.count_free_el < 0 or self.count_free_el > self.max_count_el:
            return ("Error. Incorrect state",)

        next_index = self.calculate_next_index(self.head_index)
        if not isinstance(next_index, int):
            return ("Error. Incorrect state",)
        code = self.check_index(next_index)

        if code == 0:
            self.head_index = next_index
            self.array[self.head_index] = value
            self.count_free_el -= 1
            return None
        return ("Error. Incorrect state",)

    def dequeue(self):
        if self.count_free_el == self.max_count_el:
            return None
        result = self.array[self.tail_index]
        self.array[self.tail_index] = None
        self.tail_index = self.calculate_next_index(self.tail_index)
        self.count_free_el += 1
        if self.count_free_el == self.max_count_el:
            self.head_index = None
            self.tail_index = None
        return result

    def size(self) -> int:
        return self.max_count_el

    def get_free_el(self) -> int:
        return self.count_free_el

    def is_full(self):
        return self.count_free_el == 0

    def calculate_next_index(self, index: int) -> int | tuple:
        if index >= self.max_count_el:
            return ("Error state",)
        next_index = index + 1
        if next_index >= self.max_count_el:
            next_index = next_index - self.max_count_el
        return next_index

    def check_index(self, index_to_check: int) -> int:
        """
        Метод проверки использования индекса
        Коды ответа:
            0 - пусто
            1 - заполнено
            -1 = вне массива
        """
        if index_to_check >= self.max_count_el:
            return -1
        try:
            value_in_next_index = self.array[index_to_check]
        except ValueError:
            return 0
        if value_in_next_index is not None:
            return 1
        return 0
