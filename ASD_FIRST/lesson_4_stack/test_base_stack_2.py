from ASD_FIRST.lesson_4_stack.base_stack_2 import (
    is_balance,
    ExpandedStack,
    calculate_math_expression,
)


def test_is_balance():
    assert is_balance(input_str="()") is True
    assert is_balance(input_str="()()") is True
    assert is_balance(input_str="(())") is True
    assert is_balance(input_str="(()((())()))") is True
    assert is_balance(input_str="(()((())()))") is True
    assert is_balance(input_str="[]({})") is True
    assert is_balance(input_str="") is True

    assert is_balance(input_str="(()()(()") is False
    assert is_balance(input_str="())") is False
    assert is_balance(input_str="(()") is False
    assert is_balance(input_str="())") is False
    assert is_balance(input_str="))") is False
    assert is_balance(input_str="(") is False
    assert is_balance(input_str="))((") is False
    assert is_balance(input_str="(()()(()") is False
    assert is_balance(input_str="(())}{(") is False
    assert is_balance(input_str="(())}{") is False


def test_is_balance_v2():
    assert is_balance(input_str="({})") is True
    assert is_balance(input_str="({[]})") is True
    assert is_balance(input_str="[(]{})") is False

    assert is_balance(input_str="{(})") is False
    assert is_balance(input_str="([})") is False


def test_expanded_stack():
    s = ExpandedStack()
    s.push(1)
    s.push(2)
    s.push(3)

    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_get_min_element():
    s = ExpandedStack()
    s.push(66)
    s.push(66)
    s.push(77)
    assert s.get_min_el() == 66

    s.push(17)
    assert s.get_min_el() == 17

    assert s.pop() == 17
    assert s.get_min_el() == 66

    assert s.pop() == 77
    assert s.get_min_el() == 66

    s.pop()
    assert s.get_min_el() == 66

    s.pop()
    assert s.get_min_el() is None

    s0 = ExpandedStack()
    assert s0.get_min_el() is None

    s0.push(1)
    assert s0.get_min_el() == 1

    s0.push(2)
    assert s0.get_min_el() == 1

    s0.push(-2)
    assert s0.get_min_el() == -2


def test_avg():
    s = ExpandedStack()

    assert s.get_avg() == 0

    s.push(55)
    assert s.get_avg() == 55

    s.push(45)
    assert s.get_avg() == 50

    s.push(1)
    assert s.get_avg() == 33

    s.pop()
    assert s.get_avg() == 50

    s.pop()
    assert s.get_avg() == 55

    s.pop()
    assert s.get_avg() == 0


def test_calculate_math_expression():
    input_stack = ExpandedStack()
    input_stack.push("*")
    input_stack.push("3")
    input_stack.push("+")
    input_stack.push("2")
    input_stack.push("1")
    assert calculate_math_expression(input_stack) == 9

    input_stack = ExpandedStack()
    input_stack.push("=")
    input_stack.push("+")
    input_stack.push("9")
    input_stack.push("*")
    input_stack.push("5")
    input_stack.push("+")
    input_stack.push("8")
    input_stack.push("2")
    assert calculate_math_expression(input_stack) == 59

    input_stack = ExpandedStack()
    input_stack.push("=")
    input_stack.push("*")
    input_stack.push("2")
    input_stack.push("3")
    assert calculate_math_expression(input_stack) == 6

    input_stack = ExpandedStack()
    input_stack.push("*")
    input_stack.push("2")
    input_stack.push("3")
    assert calculate_math_expression(input_stack) == 6

    input_stack = ExpandedStack()
    input_stack.push("=")
    input_stack.push("+")
    input_stack.push("1000")
    input_stack.push("*")
    input_stack.push("3")
    input_stack.push("44")
    assert calculate_math_expression(input_stack) == 1132
