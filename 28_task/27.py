def Football(f: list[int], n: int) -> bool:
    if n == 1:
        return False

    list_min_indexes = get_list_min_indexes_position(f, n)
    dict_index_position = dict(enumerate(list_min_indexes))

    non_sort_position = get_incorrect_position(dict_index_position)
    non_sort_position_len = len(non_sort_position)

    if non_sort_position_len == 0:
        return False
    if non_sort_position_len == 2:
        return True
    checked_list = [dict_index_position[i] for i in non_sort_position]
    checked_list_len = len(checked_list)

    is_sort = check_is_sort(checked_list, checked_list_len, 0, 1)
    is_decrement = check_is_decrement(checked_list, checked_list_len, 0)
    return is_sort and is_decrement


def check_is_sort(checked_list: list[int], n: int, i: int, comp_i: int) -> bool:
    if i + 1 == n:
        return True
    if comp_i == n:
        i = i + 1
        comp_i = i
    if checked_list[i] < checked_list[comp_i]:
        return False
    return check_is_sort(checked_list, n, i, comp_i + 1)


def check_is_decrement(checked_list: list[int], n: int, i: int) -> bool:
    if i + 1 == n:
        return True
    if checked_list[i] != checked_list[i + 1] + 1:
        return False
    return check_is_decrement(checked_list, n, i + 1)


def get_list_min_indexes_position(copy_f: list[int], n) -> list[int]:
    list_min_indexes: list[int] = []

    for _ in range(n):
        min_i = find_first_min_index_not_in_list(list_min_indexes)
        min_iter_index = find_min_index(copy_f, list_min_indexes, len(copy_f), 0, min_i)
        list_min_indexes.append(min_iter_index)

    return list_min_indexes


def find_first_min_index_not_in_list(input_l: list[int]) -> int:
    l_i = len(input_l)
    if l_i == 0:
        return 0
    for i, _ in enumerate(input_l):
        if i not in input_l:
            return i
    return l_i


def find_min_index(
    x: list[int], indexes_list: list[int], n: int, i: int, min_i: int
) -> int:
    i_in_indexes_list = i in indexes_list
    if i == n:
        return min_i

    if not i_in_indexes_list and x[min_i] > x[i]:
        min_i = i
    return find_min_index(x, indexes_list, n, i + 1, min_i)


def get_incorrect_position(d: dict[int, int]) -> list:
    result = [k for k, v in d.items() if k != v]
    return result


def test():
    assert get_list_min_indexes_position([5, 10, 1], 3) == [2, 0, 1]
    assert get_list_min_indexes_position([1, 2], 2) == [0, 1]
    assert get_list_min_indexes_position([10, 5, 1], 3) == [2, 1, 0]
    assert get_list_min_indexes_position([5, 10, 8], 3) == [0, 2, 1]
    assert get_list_min_indexes_position([9, 8, 7], 3) == [2, 1, 0]
    assert get_list_min_indexes_position([10, 5, 1], 3) == [2, 1, 0]

    assert find_first_min_index_not_in_list([0, 1, 3]) == 2
    assert find_first_min_index_not_in_list([]) == 0
    assert find_first_min_index_not_in_list([0, 2]) == 1
    assert find_first_min_index_not_in_list([0, 1]) == 2

    assert find_min_index([1, 2], [0], 2, 0, 0) == 0
    assert find_min_index([1], [], 1, 0, 0) == 0
    assert find_min_index([1, 2], [], 2, 0, 0) == 0
    assert find_min_index([3, 2], [], 2, 0, 0) == 1

    assert Football([9], 1) is False
    assert Football([9, 8], 2)
    assert Football([8, 9], 2) is False
    assert Football([3, 4, 5], 3) is False

    assert Football([1, 3, 2], 3)
    assert Football([3, 2, 1], 3)
    assert Football([1, 7, 5, 3, 9], 5)
    assert Football([1, 4, 3, 2, 5], 5)

    assert Football([9, 5, 3, 7, 1], 5) is False
    assert Football([1, 2, 3, 4, 5], 5) is False
    assert Football([1, 4, 5, 3, 2], 5) is False

    assert Football([1, 5, 4, 3, 2], 5)
    assert Football([101, 104, 105, 103, 102, 106], 6) is False
    assert Football([101, 105, 104, 103, 102, 106], 6)
    assert Football([1, 5, 4, 3, 2, 6], 6)

