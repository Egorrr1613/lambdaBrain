def TankRush(h1: int, w1: int, s1: str, h2: int, w2: int, s2: str) -> bool:
    if h1 < h2 or w1 < w2 or h2 == 0 or w2 == 0:
        return False
    return is_in(str_to_arr(s1), str_to_arr(s2), h2, w2)


def str_to_arr(s: str):
    return list(map(list, s.split(" ")))


def is_in(l1: list[list[str]], l2: list[list[str]], h2: int, w2: int) -> bool:
    count_occurrences, i2, j2 = 0, 0, 0
    for _, sublist in enumerate(l1):
        for _, element in enumerate(sublist):
            if element == l2[i2][j2]:
                count_occurrences += 1
                j2 += 1
            if count_occurrences == w2:
                i2 += 1
                break

        if i2 == h2 and j2 == w2:
            return True
        count_occurrences, j2 = 0, 0
    return False


def test():
    assert TankRush(3, 4, "1234 2345 0987", 2, 2, "39 98") is False
    assert TankRush(3, 4, "1235 2345 0987", 2, 2, "32 98") is False
    assert TankRush(3, 4, "1235 2345 0987", 3, 2, "23 98 11") is False
    assert TankRush(3, 4, "1235 2345 0987", 4, 2, "23 45 87 12") is False
    assert TankRush(2, 1, "1 1", 2, 1, "0 1") is False
    assert TankRush(2, 1, "1 1", 2, 1, "1 0") is False
    assert TankRush(2, 1, "1 1", 2, 1, "0 0") is False
    assert TankRush(2, 1, "1 1", 2, 1, "1 1") is True
    assert TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98") is True
    assert TankRush(3, 4, "1234 2345 0987", 3, 2, "34 45 98") is True
    assert TankRush(3, 4, "1234 2345 0987", 2, 2, "12 87") is True
    assert TankRush(3, 4, "1234 2345 0987", 3, 4, "1234 2345 0987") is True
    assert TankRush(3, 4, "1234 2345 0987", 3, 4, "1234 2345 0989") is False
    assert TankRush(4, 4, "1234 1234 1235 1234", 1, 1, "5") is True
    assert TankRush(4, 4, "1234 1234 1235 1234", 1, 1, "9") is False
    assert TankRush(1, 1, "1", 1, 1, "2") is False
    assert TankRush(1, 1, "1", 1, 1, "1") is True
    assert str_to_arr("1234 2345 0987") == [
        ["1", "2", "3", "4"],
        ["2", "3", "4", "5"],
        ["0", "9", "8", "7"],
    ]
