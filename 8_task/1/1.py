def white_walkers(village: str) -> bool:
    buffer = []  # O(1)
    for i, v in enumerate(village):  # O(n)
        if v.isdigit() or v == "=":  # O(1)
            buffer.append(v)  # O(1)

    if len(buffer) < 5:  # O(1)
        return False

    buffer_2 = []  # O(1)
    for i, v in enumerate(buffer):  # O(n)
        if v.isdigit():  # O(1)
            buffer_2.append((i, int(v)))  # O(1)
        if (
            len(buffer_2) >= 2
            and (buffer_2[-1][1] + buffer_2[-2][1]) == 10
            and (buffer_2[-1][0] - buffer_2[-2][0]) != 4
        ):  # O(1)
            return False

    return len(buffer_2) >= 2  # O(1)


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

