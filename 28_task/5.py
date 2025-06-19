def SynchronizingTables(n: int, ids: list[int], salary: list[int]) -> list[int]:
    if n == 1:
        return salary

    ignore_index = []

    while len(ignore_index) < n:
        max_id_index = find_max_ids_index(0, 1, ids, ignore_index)
        max_sal_index = find_max_salary_index(n - 1, n - 1, salary, ignore_index)
        salary[max_id_index], salary[max_sal_index] = (
            salary[max_sal_index],
            salary[max_id_index],
        )
        ignore_index.append(max_id_index)
    ignore_index = None
    return salary


def find_max_salary_index(
        max_salary_index: int, checked_salary_index: int,
        salary: list[int], ignore_index: list[int]
) -> int:
    if checked_salary_index not in ignore_index and salary[max_salary_index] <= salary[checked_salary_index]:
        max_salary_index = checked_salary_index
    elif (max_salary_index in ignore_index) and (checked_salary_index not in ignore_index):
        max_salary_index = checked_salary_index
    if checked_salary_index == 0:
        return max_salary_index
    return find_max_salary_index(max_salary_index, checked_salary_index - 1, salary, ignore_index)


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
    assert SynchronizingTables(
        8, [8, 7, 6, 5, 4, 3, 2, 1], [10, 20, 30, 40, 50, 60, 70, 80]
    ) == [80, 70, 60, 50, 40, 30, 20, 10]
    assert SynchronizingTables(2, [1, 2], [10, 20]) == [10, 20]
    assert SynchronizingTables(1, [100], [200]) == [200]
    assert SynchronizingTables(5, [1, 2, 3, 4, 5], [90, 20, 20, 10, 20]) == [
        10,
        20,
        20,
        20,
        90,
    ]
    assert SynchronizingTables(5, [8, 5, 4, 11, 6], [20, 20, 20, 20, 1]) == [
        20,
        20,
        1,
        20,
        20,
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
