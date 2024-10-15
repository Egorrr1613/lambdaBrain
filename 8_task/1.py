def white_walkers(village: str) -> bool:
    if len(village) < 5:
        return False
    int_indexes = [(k, int(v)) for k, v in enumerate(village) if v.isdigit()]
    len_indexes = len(int_indexes)

    if not len_indexes:
        return False

    pair_int_sum_ten: set[tuple[int, int]] = set()
    find_pair_ten(int_indexes, len_indexes - 1, pair_int_sum_ten)

    if not pair_int_sum_ten:
        return False

    for start, end in pair_int_sum_ten:
        sl_village = village[start : end + 1]
        if find_equal_count(sl_village, len(sl_village), 0) != 3:
            return False

    return True


def find_pair_ten(
    input_l: list[tuple[int, int]], index: int, result: set[tuple[int, int]]
) -> None:
    if index == 0:
        return
    if input_l[index][1] + input_l[index - 1][1] == 10:
        result.add((input_l[index - 1][0], input_l[index][0]))
    find_pair_ten(input_l, index - 1, result)


def find_equal_count(s: str, n: int, i: int) -> int:
    if i == n:
        return 0
    return int(s[i] == "=") + find_equal_count(s, n, i + 1)


def test():
    assert white_walkers("axxb6===4xaf5===eee5")
    assert white_walkers("5==ooooooo=5=5") is False
    assert white_walkers("5==ooooooo=5==5") is False
    assert white_walkers("5==ooooooo=5===5") is True
    assert white_walkers("abc=7==hdjs=3gg1=======5")
    assert white_walkers("abc=7==hdjs=3gg5=======5") is False
    assert white_walkers("aaS=8") is False
    assert white_walkers("9===1===9===1===9")
    assert white_walkers("1===1===9===1===9")
    assert white_walkers("1===1==9===1===9") is False

    assert white_walkers("") is False
    assert white_walkers("=") is False
    assert white_walkers("==") is False
    assert white_walkers("===") is False
    assert white_walkers("4===6")
    assert white_walkers("======") is False
    assert white_walkers("===1==9===") is False
    assert white_walkers("===1===9===")
    assert white_walkers("=1===9=")

    assert find_equal_count("==,124214214sdgsdg=", 19, 0) == 3
    assert find_equal_count("==", 2, 0) == 2
    assert find_equal_count("=", 1, 0) == 1
    assert find_equal_count("", 0, 0) == 0

