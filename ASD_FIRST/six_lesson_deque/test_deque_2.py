from ASD_FIRST.six_lesson_deque.deque_2 import is_palindrome, DequeWithGetMin


def test_palindrome():
    assert is_palindrome("a") is True
    assert is_palindrome("aaaa") is True
    assert is_palindrome("1111") is True
    assert is_palindrome("11111") is True
    assert is_palindrome("11211") is True
    assert is_palindrome("112111") is False
    assert is_palindrome("3210123") is True
    assert is_palindrome("321123") is True
    assert is_palindrome("aabaaa") is False
    assert is_palindrome("abc") is False
    assert is_palindrome("Я иду с мечем судия") is True
    assert is_palindrome("Я иду с меем судия") is True
    assert is_palindrome("Я иду с мечом судия") is False


def test_deq_min():
    d = DequeWithGetMin()
    assert d.min() is None
    d.addTail(1)
    assert d.min() == 1
    d.addTail(-5)
    assert d.min() == -5
    d.addTail(4)
    assert d.min() == -5
    d.removeTail()
    d.removeTail()
    assert d.min() == 1

def test_deq_min_2():
    d = DequeWithGetMin()
    d.addFront(5)
    d.addTail(6)
    d.addFront(3)
    d.addFront(8)
    d.addFront(9)
    d.removeTail()
    d.removeTail()
    d.removeTail()
    assert d.min() == 8

    d = DequeWithGetMin()
    d.addFront(0)
    d.addFront(0)
    d.addFront(1)
    d.addFront(-5)
    assert d.min() == -5

    d.removeFront()
    assert d.min() == 0

    d.removeTail()
    assert d.min() == 0

    d.removeTail()
    assert d.min() == 1

    d.removeTail()
    assert d.min() is None
