def massdriver(activate: list[int]) -> int:
    result = -1
    buffer: dict[int: list[int: int]] = {}
    for i, v in enumerate(activate):

        find_duplicate_num = False
        buffer_data = buffer.get(v)
        if buffer_data is None:
            buffer[v] = [i, 0]
            continue

        if buffer_data[1] == 0:
            buffer[v] = [buffer[v][0], i]
            find_duplicate_num = True

        if find_duplicate_num and result == -1:
            result = v
            continue

        if find_duplicate_num:
            result = v if buffer[v][0] < buffer[result][0] else result

    if result == -1:
        return result
    return buffer[result][0]


def test():
    assert massdriver([1, 2]) == -1
    assert massdriver([1, 1, 1]) == 0
    assert massdriver([1, 2, 3, 1, 2, 3, 4]) == 0
    assert massdriver([1, 2, 3, 4, 5, 6, 7]) == -1
    assert massdriver([1, 2, 3, 4, 3, 4, 2]) == 1
    assert massdriver([9, 1, 2, 3, 4, 3, 4, 2, 9]) == 0
    assert massdriver([1, 2, 3, 4, 5, 6, 7, 7]) == 6
