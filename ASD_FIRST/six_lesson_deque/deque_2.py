from ASD_FIRST.six_lesson_deque.deque import Deque


def is_palindrome(checked_str: str) -> bool:
    """Решение 3 дополнительного задания"""
    if len(checked_str) < 2:
        return True
    d = Deque()
    for ch in checked_str:
        if ch == " ":
            continue
        d.addTail(ch.lower())

    while d.size() != 0:
        left = d.removeFront()
        right = d.removeTail()
        if left is not None and right is None and d.size() == 0:
            return True
        if left != right:
            return False
    return True