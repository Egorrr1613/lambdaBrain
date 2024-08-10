def MadMax(n: int, tele: list[int]) -> list[int]:
    if n == 1:
        return tele
    middle_index = (n - 1) // 2

    result = recursion_sort(tele, 0, n)
    result = reverse_recursion_sort(result, middle_index, n - 1)

    return result


def recursion_sort(tele: list[int], current_index: int, size: int) -> list[int]:
    if current_index == size - 1 and size == 1:
        return tele
    next_index = current_index + 1
    if current_index == size - 1:
        next_index, size = 0, size - 1
    elif tele[current_index] > tele[current_index + 1]:
        buffer = tele[current_index + 1]
        tele[current_index + 1] = tele[current_index]
        tele[current_index] = buffer
    result = recursion_sort(tele, next_index, size)
    return result


def reverse_recursion_sort(
    tele: list[int], current_index: int, last_index: int
) -> list[int]:
    if current_index >= last_index:
        return tele
    if current_index < last_index:
        buffer = tele[current_index]
        tele[current_index] = tele[last_index]
        tele[last_index] = buffer
    return reverse_recursion_sort(tele, current_index + 1, last_index - 1)


def test():
    assert MadMax(1, [55]) == [55]
    assert MadMax(3, [1, 2, 3]) == [1, 3, 2]
    assert MadMax(7, [1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 7, 6, 5, 4]
    assert MadMax(9, [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 9, 8, 7, 6, 5]
    assert MadMax(3, [8, 8, 8]) == [8, 8, 8]
    assert MadMax(3, [8, 8, 7]) == [7, 8, 8]
    assert MadMax(3, [9, 8, 8]) == [8, 9, 8]

