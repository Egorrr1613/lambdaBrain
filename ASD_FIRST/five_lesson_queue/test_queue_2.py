from ASD_FIRST.five_lesson_queue.queue import Queue
from ASD_FIRST.five_lesson_queue.queue_2 import (
    circulation_queue,
    QueueByTwoStack,
    revert_queue,
)


def test_circulation_0():
    q = Queue()
    circulation_queue(input_q=q, count_element_shift=99)
    assert not q.get_all_nodes()

    q.enqueue(88)
    circulation_queue(input_q=q, count_element_shift=4)
    assert q.get_all_nodes() == [88]


def test_circulation_1():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    assert q.get_all_nodes() == [5, 6, 7]

    circulation_queue(input_q=q, count_element_shift=1)
    assert q.get_all_nodes() == [6, 7, 5]

    circulation_queue(input_q=q, count_element_shift=1)
    assert q.get_all_nodes() == [7, 5, 6]

    circulation_queue(input_q=q, count_element_shift=1)
    assert q.get_all_nodes() == [5, 6, 7]


def test_circulation_2():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    assert q.get_all_nodes() == [5, 6, 7]

    circulation_queue(input_q=q, count_element_shift=2)
    assert q.get_all_nodes() == [7, 5, 6]

    circulation_queue(input_q=q, count_element_shift=2)
    assert q.get_all_nodes() == [6, 7, 5]

    circulation_queue(input_q=q, count_element_shift=2)
    assert q.get_all_nodes() == [5, 6, 7]


def test_circulation_3():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    assert q.get_all_nodes() == [5, 6, 7, 8, 9]

    circulation_queue(input_q=q, count_element_shift=5)
    assert q.get_all_nodes() == [5, 6, 7, 8, 9]

    circulation_queue(input_q=q, count_element_shift=10)
    assert q.get_all_nodes() == [5, 6, 7, 8, 9]

    circulation_queue(input_q=q, count_element_shift=11)
    assert q.get_all_nodes() == [6, 7, 8, 9, 5]

    circulation_queue(input_q=q, count_element_shift=14)
    assert q.get_all_nodes() == [5, 6, 7, 8, 9]


def test_queue_by_two_stack():
    q = QueueByTwoStack()
    assert q.size() == 0
    assert q.dequeue() is None

    q.enqueue(1)
    assert q.size() == 1

    assert q.dequeue() == 1
    assert q.size() == 0

    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)

    assert q.size() == 3

    assert q.dequeue() == 5
    assert q.dequeue() == 6
    assert q.dequeue() == 7
    assert q.size() == 0


def test_revert_queue():
    q = Queue()
    assert not revert_queue(q).get_all_nodes()

    q = Queue()
    q.enqueue(1)
    assert revert_queue(q).get_all_nodes() == [1]

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert revert_queue(q).get_all_nodes() == [3, 2, 1]

    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    assert revert_queue(q).get_all_nodes() == [9, 8, 7, 6, 5]
