def is_palindrome(out_str: str):
    out_str = out_str.lower().replace(" ", "")
    start_index, end_index = 0, len(out_str) - 1

    def recursion(inner_str: str, start, end):
        if start >= end:
            return True
        if inner_str[start] != inner_str[end]:
            return False
        return recursion(inner_str, start + 1, end - 1)

    return recursion(out_str, start_index, end_index)


def test():
    assert is_palindrome("a") is True
    assert is_palindrome("aaaa") is True
    assert is_palindrome("aabaaa") is False
    assert is_palindrome("abc") is False
    assert is_palindrome("Я иду с мечем судия") is True
    assert is_palindrome("Я иду с меем судия") is True
    assert is_palindrome("Я иду с мечом судия") is False
