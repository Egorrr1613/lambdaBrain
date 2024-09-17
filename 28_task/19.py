def ShopOLAP(_: int, items: list[str]) -> list[str]:
    format_input = list(map(lambda x: x.split(), items))
    uniq_position = dict.fromkeys(set(map(lambda x: x[0], format_input)), 0)
    for i in format_input:
        uniq_position[i[0]] = uniq_position[i[0]] + int(i[1])
    concatenate_position = list(
        map(lambda x: f"{x} {str(uniq_position.get(x))}", uniq_position)
    )
    return sorted(
        concatenate_position, key=lambda x: (-int(x.split()[1]), x.split()[0])
    )


def test():
    assert ShopOLAP(1, ["платье1 5"]) == ["платье1 5"]
    assert ShopOLAP(2, ["платье1 5", "платье1 1"]) == ["платье1 6"]
    assert ShopOLAP(
        5, ["платье1 5", "сумка32 2", "платье1 1", "сумка23 2", "сумка128 4"]
    ) == ["платье1 6", "сумка128 4", "сумка23 2", "сумка32 2"]

    assert ShopOLAP(
        5, ["платье1 5", "платье1 1", "сумка23 2", "сумка128 4", "платье12 1"]
    ) == ["платье1 6", "сумка128 4", "сумка23 2", "платье12 1"]

    assert ShopOLAP(
        6,
        [
            "платье1 10",
            "платье2 9",
            "сумка3 20",
            "сумка128 1",
            "платье12 100",
            "сумка3 20",
        ],
    ) == ["платье12 100", "сумка3 40", "платье1 10", "платье2 9", "сумка128 1"]

