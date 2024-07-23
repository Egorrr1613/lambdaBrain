def is_palindrome(input_str: str):
    input_str = input_str.lower().strip()
    if len(input_str) < 2:
        return True
    if input_str[0] != input_str[-1]:
        return False
    return (input_str[0] == input_str[-1]) and is_palindrome(input_str[1:-1])


def test():
    assert is_palindrome("a") is True
    assert is_palindrome("aaaa") is True
    assert is_palindrome("abc") is False
    assert is_palindrome("Я иду с мечем судия") is True
    assert is_palindrome("Я иду с мечом судия") is False
