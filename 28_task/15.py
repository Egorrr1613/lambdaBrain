def TankRush(h1: int, w1: int, s1: str, h2: int, w2: int, s2: str) -> bool:
    if h1 < h2 or w1 < w2 or h2 == 0 or w2 == 0:
        return False
    return find_first_in(str_to_arr(s1), h1, w1, str_to_arr(s2), h2, w2)


def str_to_arr(s: str):
    return list(map(list, s.split(" ")))


def check_size(h1, h2, w1, w2, current_sublist_index_1, current_el_index_1):
    if h2 > (h1 - current_sublist_index_1) or w2 > (w1 - current_el_index_1):
        return False
    return True


def find_first_in(
    list_1: list[list[str]], h1: int, w1: int,
        list_2: list[list[str]], h2: int, w2: int
) -> bool:
    for index_sublist_1, sublist in enumerate(list_1):
        for index_element_1, element in enumerate(sublist):
            if (
                element == list_2[0][0]
                and check_size(h1, h2, w1, w2, index_sublist_1, index_element_1)
                and is_full_in(
                    list_1, h1, w1, index_sublist_1, index_element_1, list_2, h2, w2, 0, 0
                )
            ):
                return True
    return False


def is_full_in(
    l1: list[list[str]],
    h1: int,
    w1: int,
    sub_list_index_1: int,
    index_el_1: int,
    l2: list[list[str]],
    h2: int,
    w2: int,
    sub_list_index_2: int,
    index_el_2: int,
):
    if l1[sub_list_index_1][index_el_1] != l2[sub_list_index_2][index_el_2]:
        return False
    if sub_list_index_2 == (h2 - 1) and index_el_2 == (w2 - 1):
        return True
    next_index_sublist_2, next_el_index_2 = sub_list_index_2, index_el_2
    if index_el_2 < (w2 - 1):
        index_el_1 += 1
        next_el_index_2 += 1
    if index_el_2 == (w2 - 1):
        next_index_sublist_2 += 1
        next_el_index_2 = 0
        sub_list_index_1 += 1
        index_el_1 = index_el_1 - (w2 - 1)
    return is_full_in(
        l1,
        h1,
        w1,
        sub_list_index_1,
        index_el_1,
        l2,
        h2,
        w2,
        next_index_sublist_2,
        next_el_index_2,
    )


def test():
    assert str_to_arr("1234 2345 0987") == [
        ["1", "2", "3", "4"],
        ["2", "3", "4", "5"],
        ["0", "9", "8", "7"],
    ]

    assert TankRush(3, 3, "321 694 798", 2, 2, "94 98") is True
    assert TankRush(3, 3, "321 694 798", 2, 2, "69 98") is False
    assert TankRush(3, 4, "1234 2345 0987", 2, 2, "39 98") is False
    assert TankRush(3, 4, "1235 2345 0987", 2, 2, "32 98") is False
    assert TankRush(3, 4, "1235 2345 0987", 3, 2, "23 98 11") is False
    assert TankRush(3, 4, "1235 2345 0987", 4, 2, "23 45 87 12") is False
    assert TankRush(2, 1, "1 1", 2, 1, "0 1") is False
    assert TankRush(3, 1, "1 2 3", 3, 1, "2 3 4") is False
    assert TankRush(2, 1, "1 1", 2, 1, "1 0") is False
    assert TankRush(2, 1, "1 1", 2, 1, "0 0") is False
    assert TankRush(2, 1, "1 1", 2, 1, "1 1") is True
    assert TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98") is True
    assert TankRush(3, 4, "1234 2345 0987", 3, 2, "34 45 87") is True
    assert TankRush(3, 4, "1234 2345 0987", 2, 2, "12 87") is False
    assert TankRush(3, 4, "1234 2345 0987", 3, 4, "1234 2345 0987") is True
    assert TankRush(3, 4, "1234 2345 0987", 3, 4, "1234 2345 0989") is False
    assert TankRush(4, 4, "1234 1234 1235 1234", 1, 1, "5") is True
    assert TankRush(4, 4, "1234 1234 1235 1234", 1, 1, "9") is False
    assert TankRush(1, 1, "1", 1, 1, "2") is False
    assert TankRush(1, 1, "1", 1, 1, "1") is True

