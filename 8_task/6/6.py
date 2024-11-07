def TRC_sort(trc: list[int]) -> list[int]:
    l0, mid, h_i = -1, 0, len(trc) - 1
    return recursion_sort(trc, l0, mid, h_i)


def recursion_sort(input_arr: list[int], l0: int, mid: int, hi: int) -> list[int]:
    if mid > hi:
        return input_arr
    if input_arr[mid] == 0:
        input_arr[mid], input_arr[l0 + 1] = input_arr[l0 + 1], input_arr[mid]
        l0 += 1
        mid += 1
    elif input_arr[mid] == 1:
        mid += 1
    else:
        input_arr[mid], input_arr[hi] = input_arr[hi], input_arr[mid]
        hi -= 1
    return recursion_sort(input_arr, l0, mid, hi)


def test():
    assert TRC_sort([2, 1, 0]) == [0, 1, 2]
    assert TRC_sort([0, 0, 0]) == [0, 0, 0]
    assert TRC_sort([0, 1, 2, 1, 0, 2]) == [0, 0, 1, 1, 2, 2]
