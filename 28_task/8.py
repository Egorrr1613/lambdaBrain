def SumOfThe(n: int, data: list[int]) -> int:
    return recursion_score(n, 0, data)


def recursion_score(n: int, current_index: int, data: list[int]):
    buffer, data[current_index] = data[current_index], 0
    if recursion_sum(0, data, n, 0) == buffer:
        return buffer
    data[current_index] = buffer
    return recursion_score(n, current_index + 1, data)


def recursion_sum(index: int, data: list[int], l_data: int, buffer_sum: int) -> int:
    if index == l_data:
        return buffer_sum
    return recursion_sum(index + 1, data, l_data, buffer_sum + data[index])


def test():
    assert SumOfThe(5, [5, -25, 10, -35, -45]) == -45
    assert SumOfThe(7, [100, -50, 10, -25, 90, -35, 90]) == +90
    assert SumOfThe(4, [100, -50, 90, 60]) == 100
    assert SumOfThe(4, [35, -50, 90, 75]) == 75
    assert SumOfThe(3, [1, 3, 2]) == 3
    assert SumOfThe(2, [1, 1]) == 1
    assert SumOfThe(3, [1, 0, 1]) == 1

    assert recursion_sum(0, [1, 2, 3, 10, -5], 5, 0) == 11
    assert recursion_sum(0, [5], 1, 0) == 5
    assert recursion_sum(0, [5, 5], 2, 0) == 10
