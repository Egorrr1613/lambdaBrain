from ASD_FIRST.four_lesson_stack.base_stack import Stack, ReverseStack

def test_base_append_and_del():
    s = Stack()

    s.push(1)

    expect_pop = s.pop()
    expect_pop_2 = s.pop()

    assert expect_pop == 1
    assert expect_pop_2 is None


def test_base_size():
    s = Stack()
    assert s.size() == 0

    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    assert s.size() == 4

    s.pop()
    s.pop()
    s.pop()
    s.pop()
    assert s.size() == 0


def test_base_peek():
    s = Stack()

    s.push(96)
    s.push(97)
    s.push(98)
    s.push(99)
    assert s.peek() == 99

    s.pop()
    assert s.peek() == 98

    s.pop()
    assert s.peek() == 97

    s.pop()
    assert s.peek() == 96

    s.pop()
    assert s.peek() is None

    s.pop()
    assert s.peek() is None

def test_base_pop():
    s = Stack()

    s.push(96)
    s.push(97)
    assert s.size() == 2

    assert s.pop() == 97
    assert s.pop() == 96
    assert s.pop() is None
    assert s.pop() is None



def test_reverse_stack():
    s = ReverseStack()
    assert s.size() == 0
    assert s.peek() is None

    s.push(123)
    assert s.size() == 1

    s.push(456)
    assert s.size() == 2

    s.push(789)
    assert s.size() == 3

    assert s.pop() == 789
    assert s.size() == 2

    assert s.pop() == 456
    assert s.size() == 1

    assert s.pop() == 123
    assert s.size() == 0

    assert s.pop() is None
    assert s.size() == 0
