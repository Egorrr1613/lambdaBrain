def white_walkers(village: str) -> bool:
    peasants_and_walkers = []  # O(1)
    for _, v in enumerate(village):  # O(n)
        if v.isdigit() or v == "=":  # O(1)
            peasants_and_walkers.append(v)  # O(1)

    if len(peasants_and_walkers) < 5:  # O(1)
        return False

    neighboring_walkers = []  # O(1)
    for entity_index, peasant_or_walker in enumerate(peasants_and_walkers):  # O(n)
        if peasant_or_walker.isdigit():  # O(1)
            neighboring_walkers.append((entity_index, int(peasant_or_walker)))  # O(1)
        if (
            len(neighboring_walkers) >= 2
            and (neighboring_walkers[-1][1] + neighboring_walkers[-2][1]) == 10
            and (neighboring_walkers[-1][0] - neighboring_walkers[-2][0]) != 4
        ):  # O(1)
            return False

    return len(neighboring_walkers) >= 2  # O(1)


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

