from ASD_FIRST.lesson_5_queue.queue import Queue


def test_1():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)

    assert q.size() == 3

    assert q.dequeue() == 5
    assert q.dequeue() == 6
    assert q.dequeue() == 7
    assert q.size() == 0


def test_2():
    q = Queue()
    assert q.dequeue() is None
    assert q.dequeue() is None
    assert q.size() == 0
