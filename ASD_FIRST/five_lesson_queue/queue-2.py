import ctypes
from ASD_FIRST.five_lesson_queue.queue import Queue
from ASD_FIRST.four_lesson_stack.base_stack import Stack


def circulation_queue(input_q: Queue, count_element_shift: int) -> None:
    """
    Задание: №5
    Номер задачи из задания: №3
    Краткое название: "Функция вращения очереди на N элементов"
    Сложность: size - O(1)/time - O(n)

    Рефлексия: Быстро решил задание,
        предварительно смоделировав на бумаге как должно выглядеть вращение очереди.
    """
    if input_q.size() < 2:
        return
    for _ in range(count_element_shift):
        buffer = input_q.dequeue()
        input_q.enqueue(buffer)


class QueueByTwoStack:
    """
    Задание: №5
    Номер задачи из задания: №4
    Краткое название: "Очередь с помощью двух стеков"
    Сложность:
        enqueue: size - O(1)/time - O(1)
        dequeue: size - O(1)/time - O(n), в среднем случае близкое к o(1)

    Рефлексия: Над этим заданием пришлось подумать.
        Признаюсь, не смог сам дойти до того, как реализовать удаление элемента из очереди.
        Хотя сейчас это кажется очевидным решением. Когда осознал,
        что при удалении нужно перегонять элементы во второй стек - решил без проблем.
    """

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
    """
    Задание: №5
    Номер задачи из задания: №5
    Краткое название: "Функция обращающая все элементы в очереди в обратном порядке"
    Сложность: size - O(n)/time - O(n)

    Рефлексия: Решил сам. Очень быстро понял как можно развернуть очередь через стек
        и так же быстро написал решение.
    """
    buffer_stack = Stack()
    for _ in range(input_queue.size()):
        buffer_stack.push(input_queue.dequeue())

    for _ in range(buffer_stack.size()):
        input_queue.enqueue(buffer_stack.pop())

    return input_queue


class CycleBufferQueue:
    """
    Задание: №5
    Номер задачи из задания: №6
    Краткое название: "Циклическая очередь, реализованная массивом фиксированного размера"
    Сложность: size - O(n)/time - O(n)

    Рефлексия: Решил сам, однако пришлось подумать над задачей.
        После проанализировал свое решение и предлагаемый вами алгоритм.
        Отметил несколько черт, характерных для моего кода:
            * Ввожу новые состояния и завязываю на них логику, например переменная count_free_el.
                Я использую ее, чтобы поверять состояние, когда очередь заполнена или пуста.
                Ваш алгоритм использует для этого сравнение ссылок head/tail.
                Кажется что мое решение более интуитивно понятное, однако ваше более надежное и в итоге более простое.
            * Кажется, что я слишком увлекаюсь использованием дополнительных проверок в методах.
                Например, в методе enqueue() использую 5 if для обработки разных состояний,
                хотя логика метода довольно не хитрая и может быть реализована проще.
                Стараюсь предварительно продумывать дизайн алгоритмов, схематично рисовать их на бумаге.
                Такой подход помогает не делать совсем плохо, но как мне кажется, работает не очень системно.
                Кажется что должны быть какие-то эвристики, которыми можно проверять себя.
                Очень надеюсь в этом плане на ваш курс "Ясный код".

                P.S. Подумал и сформулировал для себя такое правило:
                "Завязываться на явно выделенное состояние, а не косвенные признаки".
                Кажется эта та эвристика, которая может мне помочь сейчас улучшить свой код.

                P.P.S Реализовал очередь, согласно вашему алгоритму в классе CycleBufferQueue2.
                Честно говоря, заворожен тем, на сколько короче и проще можно описать одну и ту же логику.
                Искренне надеюсь овладеть таким мастерством мысли.
    """

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


class CycleBufferQueue2:
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError(
                'Incorrect value by param "size". Size must be great than 0'
            )
        self.size = size + 1
        self.array = (self.size * ctypes.py_object)()
        self.count_el = 0
        self.head_index = 0
        self.tail_index = 0

    def enqueue(self, value) -> None:
        next_tail_index = (self.tail_index + 1) % self.size
        if next_tail_index == self.head_index:
            return
        self.array[self.tail_index] = value
        self.tail_index = next_tail_index
        self.count_el += 1

    def dequeue(self):
        if self.head_index == self.tail_index:
            return None
        result = self.array[self.head_index]
        self.array[self.head_index] = None
        self.head_index = (self.head_index + 1) % self.size
        self.count_el -= 1
        return result

    def is_full(self) -> bool:
        return (self.tail_index + 1) % self.size == self.head_index
