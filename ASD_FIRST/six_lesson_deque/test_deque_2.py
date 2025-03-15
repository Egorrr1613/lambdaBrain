from ASD_FIRST.six_lesson_deque.deque_2 import is_palindrome, DequeWithGetMin, DequeByDynArray


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


def test_dec_by_dyn_array_state_one_el():
    d = DequeByDynArray()
    assert d.head_index == 0
    assert d.tail_index == 0
    assert d.size() == 0

    d.addFront(8)
    assert d.head_index == 0
    assert d.tail_index == 0
    assert d.size() == 1

    assert d.removeFront() == 8
    assert d.head_index == 0
    assert d.tail_index == 0
    assert d.size() == 0

    d.addTail(8)
    assert d.head_index == 0
    assert d.tail_index == 0
    assert d.size() == 1

    assert d.removeTail() == 8
    assert d.head_index == 0
    assert d.tail_index == 0
    assert d.size() == 0


def test_dec_by_dyn_array_0():
    d = DequeByDynArray()
    assert d.head_index == 0
    assert d.tail_index == 0

    d.addFront(8)
    assert d.head_index == 0
    assert d.tail_index == 0

    d.addFront(7)
    assert d.head_index == 3
    assert d.tail_index == 0

    d.addFront(6)
    d.addFront(5)

    assert d.head_index == 1
    assert d.tail_index == 0

    d.addFront(4)
    assert d.head_index == 0
    assert d.tail_index == 4

    assert True


def test_dec_by_dyn_array_1():
    d = DequeByDynArray()

    assert d.removeTail() is None
    assert d.size() == 0

    assert d.removeFront() is None
    assert d.size() == 0

    d.addFront(5)
    d.addTail(10)
    assert d.size() == 2
    assert d.head_index == 0
    assert d.tail_index == 1

    assert d.removeTail() == 10
    assert d.size() == 1
    assert d.head_index == 0
    assert d.tail_index == 0

    assert d.removeFront() == 5
    assert d.size() == 0
    assert d.head_index == 0
    assert d.tail_index == 0

    assert d.removeTail() is None
    assert d.removeFront() is None


def test_dec_by_dyn_array_2():
    d = DequeByDynArray()

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


def test_dec_by_dyn_array_3():
    d = DequeByDynArray()

    d.addFront(6)
    d.addFront(7)
    d.addFront(8)
    assert d.head_index == 2
    assert d.tail_index == 0
    assert d.size() == 3

    assert d.removeFront() == 8
    assert d.head_index == 3
    assert d.tail_index == 0
    assert d.size() == 2

    assert d.removeFront() == 7
    assert d.head_index == 0
    assert d.tail_index == 0
    assert d.size() == 1

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


def test_dec_by_dyn_array_4():
    d = DequeByDynArray()

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


def test_dec_by_dyn_array_5():
    d = DequeByDynArray()
    d.addFront(1)
    assert d.head_index == 0
    assert d.tail_index == 0

    d.addFront(2)
    assert d.head_index == 3
    assert d.tail_index == 0

    d.addFront(3)
    assert d.head_index == 2
    assert d.tail_index == 0

    d.addFront(4)
    assert d.head_index == 1
    assert d.tail_index == 0

    d.addFront(5)
    assert d.head_index == 0
    assert d.tail_index == 4

    d.addFront(6)
    assert d.head_index == 7
    assert d.tail_index == 4

    assert d.removeTail() == 1
    assert d.head_index == 7
    assert d.tail_index == 3

    assert d.removeTail() == 2
    assert d.head_index == 7
    assert d.tail_index == 2

    assert d.removeTail() == 3
    assert d.head_index == 7
    assert d.tail_index == 1

    assert d.removeTail() == 4
    assert d.head_index == 7
    assert d.tail_index == 0

    assert d.removeTail() == 5
    assert d.head_index == 7
    assert d.tail_index == 7

    assert d.removeTail() == 6
    assert d.head_index == 0
    assert d.tail_index == 0