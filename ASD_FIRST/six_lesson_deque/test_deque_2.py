from ASD_FIRST.six_lesson_deque.deque_2 import is_palindrome


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