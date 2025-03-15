from ASD_FIRST.six_lesson_deque.deque import Deque


def test_dec_0():
    d = Deque()
    assert d.removeTail() is None
    assert d.size() == 0

    assert d.removeFront() is None
    assert d.size() == 0

    d.addFront(5)
    d.addTail(10)
    assert d.size() == 2

    assert d.removeTail() == 10
    assert d.removeFront() == 5
    assert d.size() == 0

    assert d.removeTail() is None
    assert d.removeFront() is None


def test_dec_one_el():
    d = Deque()
    d.addFront(99)
    assert d.size() == 1
    assert d.removeFront() == 99
    assert d.removeFront() is None
    assert d.size() == 0

    d.addFront(99)
    assert d.size() == 1
    assert d.removeTail() == 99
    assert d.removeTail() is None
    assert d.size() == 0

    d.addTail(99)
    assert d.size() == 1
    assert d.removeTail() == 99
    assert d.removeTail() is None
    assert d.size() == 0

    d.addTail(99)
    assert d.size() == 1
    assert d.removeFront() == 99
    assert d.removeFront() is None
    assert d.size() == 0


def test_dec_add_front():
    d = Deque()

    d.addFront(6)
    d.addFront(7)
    d.addFront(8)
    assert d.size() == 3

    assert d.removeFront() == 8
    assert d.removeFront() == 7
    assert d.removeFront() == 6
    assert d.removeFront() is None
    assert d.size() == 0

    d.addFront(6)
    d.addFront(7)
    d.addFront(8)
    assert d.size() == 3

    assert d.removeTail() == 6
    assert d.removeTail() == 7
    assert d.removeTail() == 8
    assert d.removeTail() is None
    assert d.size() == 0


def test_dec_add_tail():
    d = Deque()

    d.addTail(6)
    d.addTail(7)
    d.addTail(8)
    assert d.size() == 3

    assert d.removeFront() == 6
    assert d.removeFront() == 7
    assert d.removeFront() == 8
    assert d.removeFront() is None
    assert d.size() == 0

    d.addTail(6)
    d.addTail(7)
    d.addTail(8)
    assert d.size() == 3

    assert d.removeTail() == 8
    assert d.removeTail() == 7
    assert d.removeTail() == 6
    assert d.removeTail() is None
    assert d.size() == 0

