from ASD_FIRST.five_lesson_queue.queue_2 import CycleBufferQueue


def test_cycle_buffer_queue_0():
    q = CycleBufferQueue(1)
    assert q.size() == 1
    assert q.get_free_el() == 1
    assert q.is_full() is False
    assert q.head_index is None
    assert q.tail_index is None
    assert q.dequeue() is None
    q.enqueue(95)
    q.enqueue(96)
    q.enqueue(97)
    assert q.is_full() is True
    assert q.head_index == 0
    assert q.tail_index == 0
    assert q.get_free_el() == 0
    assert q.dequeue() == 95
    assert q.is_full() is False
    assert q.head_index is None
    assert q.tail_index is None
    assert q.get_free_el() == 1


def test_cycle_buffer_queue():
    q = CycleBufferQueue(5)
    assert q.size() == 5
    assert q.get_free_el() == 5
    assert q.head_index is None
    assert q.tail_index is None
    assert q.is_full() is False

    q.enqueue(99)
    assert q.tail_index == 0
    assert q.head_index == 0
    assert q.get_free_el() == 4
    assert q.is_full() is False

    q.enqueue(98)
    assert q.tail_index == 0
    assert q.head_index == 1
    assert q.get_free_el() == 3

    assert q.dequeue() == 99
    assert q.head_index == 1
    assert q.tail_index == 1
    assert q.get_free_el() == 4

    q.enqueue(97)
    assert q.tail_index == 1
    assert q.head_index == 2

    q.enqueue(96)
    assert q.tail_index == 1
    assert q.head_index == 3

    q.enqueue(95)
    assert q.tail_index == 1
    assert q.head_index == 4

    q.enqueue(94)
    assert q.tail_index == 1
    assert q.head_index == 0
    assert q.get_free_el() == 0
    assert q.is_full() is True

    assert q.dequeue() == 98
    assert q.dequeue() == 97
