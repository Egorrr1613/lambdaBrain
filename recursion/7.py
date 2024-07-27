def find_second_min(input_list: list):
    if len(input_list) < 2:
        return
    return recursion(input_list, 1, input_list[0], input_list[1])


def recursion(input_list: list, index: int, first_max: int, second_max: int):
    if index == len(input_list):
        return second_max
    if first_max <= input_list[index]:
        second_max = first_max
        first_max = input_list[index]
    if first_max > input_list[index] > second_max:
        second_max = input_list[index]
    return recursion(input_list, index + 1, first_max, second_max)


def test():
    assert find_second_min([5, 4, 3, 2, 5]) == 5
    assert find_second_min([0, 1, 2]) == 1
    assert find_second_min([2, 3, 5, 4]) == 4
    assert find_second_min([0, 0, 0, 1]) == 0
    assert find_second_min([0, 0]) == 0
    assert find_second_min([1, 2]) == 1
    assert find_second_min([2, 1]) == 1
    assert find_second_min([1]) is None
    assert find_second_min([]) is None
