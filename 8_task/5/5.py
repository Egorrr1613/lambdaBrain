def massdriver(activate: list[int]) -> int:
    first_duplicate_index = -1
    index_and_count_duplicate_dict: dict[int: list[int: int]] = {}
    for i, v in enumerate(activate):

        find_duplicate_num = False
        buffer_data = index_and_count_duplicate_dict.get(v)
        if buffer_data is None:
            index_and_count_duplicate_dict[v] = [i, 0]
            continue

        if buffer_data[1] == 0:
            index_and_count_duplicate_dict[v] = [index_and_count_duplicate_dict[v][0], i]
            find_duplicate_num = True

        if find_duplicate_num and first_duplicate_index == -1:
            first_duplicate_index = v
            continue

        if find_duplicate_num:
            first_duplicate_index = v if index_and_count_duplicate_dict[v][0] < index_and_count_duplicate_dict[first_duplicate_index][0] else first_duplicate_index

    if first_duplicate_index == -1:
        return first_duplicate_index
    return index_and_count_duplicate_dict[first_duplicate_index][0]


def test():
    assert massdriver([1, 2]) == -1
    assert massdriver([1, 1, 1]) == 0
    assert massdriver([1, 2, 3, 1, 2, 3, 4]) == 0
    assert massdriver([1, 2, 3, 4, 5, 6, 7]) == -1
    assert massdriver([1, 2, 3, 4, 3, 4, 2]) == 1
    assert massdriver([9, 1, 2, 3, 4, 3, 4, 2, 9]) == 0
    assert massdriver([1, 2, 3, 4, 5, 6, 7, 7]) == 6
