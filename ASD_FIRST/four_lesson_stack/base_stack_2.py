from ASD_FIRST.four_lesson_stack.base_stack import Stack


def is_balance(input_str: str):
    stack = Stack()
    reverse_symbol = {')': '(', '}': '{', ']': '['}
    for i in input_str:
        if i in ['(', '{', '[']:
            stack.push(i)
            continue
        if i in [')', '}', ']'] and stack.size() > 0:
            rm_symbol = stack.pop()
            if rm_symbol != reverse_symbol[i]:
                return False
            continue
        return False

    if stack.size() == 0:
        return True
    return False


