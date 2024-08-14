def SynchronizingTables(n: int, ids: list[int], salary: list[int]) -> list[int]:
    if n == 1:
        return salary

    recursion_sort_bubble(salary, 0, n - 1)
    ignore_index = []

    while len(ignore_index) < n:
        max_id_index = find_max_ids_index(0, 1, ids, ignore_index)
        max_sal_index = find_max_salary_index(n - 1, n - 1, salary, ignore_index)
        salary[max_id_index], salary[max_sal_index] = (
            salary[max_sal_index],
            salary[max_id_index],
        )
        ignore_index.append(max_id_index)

    return salary


def find_max_salary_index(
    max_salary_index: int, index: int, salary: list[int], ignore_index: list[int]
) -> int:
    if index not in ignore_index and salary[max_salary_index] <= salary[index]:
        max_salary_index = index
    elif (max_salary_index in ignore_index) and (index not in ignore_index):
        max_salary_index = index
    if index == 0:
        return max_salary_index
    return find_max_salary_index(max_salary_index, index - 1, salary, ignore_index)


def find_max_ids_index(
    max_index: int, iter_index: int, ids: list[int], ignore_index_list: list[int]
):
    if iter_index == len(ids):
        return max_index
    if (
        (ids[max_index] <= ids[iter_index]) and (iter_index not in ignore_index_list)
    ) or max_index in ignore_index_list:
        max_index = iter_index
    return find_max_ids_index(max_index, iter_index + 1, ids, ignore_index_list)


def recursion_sort_bubble(
    arr: list[int], start_index: int, tail_index: int
) -> list[int]:
    if start_index == 0 and start_index == tail_index:
        return arr
    next_start_index = start_index + 1
    if start_index == tail_index:
        tail_index -= 1
        next_start_index = 0
    elif arr[start_index] > arr[start_index + 1]:
        buffer = arr[start_index + 1]
        arr[start_index + 1] = arr[start_index]
        arr[start_index] = buffer
    return recursion_sort_bubble(arr, next_start_index, tail_index)


def test():
    assert SynchronizingTables(3, [50, 1, 1024], [20000, 100000, 90000]) == [
        90000,
        20000,
        100000,
    ]
    assert SynchronizingTables(4, [50, 1, 1024, 9], [20000, 100000, 90000, 50]) == [
        90000,
        50,
        100000,
        20000,
    ]

    assert find_max_salary_index(2, 2, [20000, 90000, 100000], [2]) == 1
    assert find_max_salary_index(2, 2, [20000, 90000, 100000], [0, 2]) == 1
    assert find_max_salary_index(2, 2, [20000, 90000, 100000], []) == 2
    assert find_max_salary_index(3, 3, [20000, 90000, 100000, 90000000], [2]) == 3
    assert find_max_salary_index(3, 3, [20000, 90000, 100000, 90000000], [2, 3]) == 1
    assert find_max_salary_index(3, 3, [20000, 90000, 100000, 90000000], [2, 3, 1]) == 0

    assert find_max_ids_index(0, 1, [1, 47, 9, 5], []) == 1
    assert find_max_ids_index(0, 1, [1, 47, 9, 5], [2, 3]) == 1
    assert find_max_ids_index(0, 1, [1, 47, 9, 5], [1, 2]) == 3
    assert find_max_ids_index(0, 1, [1, 47, 9, 5], [1, 2, 3]) == 0
    assert find_max_ids_index(0, 1, [50, 4, 1024], [2, 0]) == 1

