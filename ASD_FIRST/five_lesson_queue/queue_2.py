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
