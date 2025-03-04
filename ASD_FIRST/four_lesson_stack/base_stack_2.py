from ASD_FIRST.four_lesson_stack.base_stack import Stack


def is_balance(input_str: str):
    stack = Stack()
    for i in input_str:
        if i == '(':
            stack.push('i')
            continue
        if i == ')' and stack.size() > 0:
            stack.pop()
            continue
        return False

    if stack.size() == 0:
        return True
    return False



def test_is_balance():
    assert is_balance(input_str="()") is True
    assert is_balance(input_str="(())") is True
    assert is_balance(input_str="(()((())()))") is True
    assert is_balance(input_str="(()((())()))") is True
    assert is_balance(input_str="(()()(()") is False
    assert is_balance(input_str="())") is False
    assert is_balance(input_str="))") is False
    assert is_balance(input_str="") is True
    assert is_balance(input_str="(") is False

