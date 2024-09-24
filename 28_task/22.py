def SherlockValidString(s: str) -> bool:
    d_char_count: dict[str, int] = {}
    for char in s:
        if d_char_count.get(char) is None:
            d_char_count[char] = 0
        d_char_count[char] += 1

    d_value_char: dict[int, list[str]] = {}
    for k, v in d_char_count.items():
        if d_value_char.get(v) is None:
            d_value_char[v] = []
        d_value_char[v].append(k)

    d_count_value_len = len(d_value_char)
    if d_count_value_len == 1:
        return True
    if d_count_value_len != 2:
        return False

    items = list(d_value_char.items())
    if len(items[0][1]) > len(items[1][1]):
        key_max, key_min = items[0][0], items[1][0]
    else:
        key_max, key_min = items[1][0], items[0][0]

    if (
        len(d_value_char[key_min]) == 1
        and d_char_count[d_value_char[key_min][0]] - 1
        == d_char_count[d_value_char[key_max][0]]
    ):
        return True
    if (
        len(d_value_char[key_max]) == 1
        and d_char_count[d_value_char[key_max][0]] - 1
        == d_char_count[d_value_char[key_min][0]]
    ):
        return True

    if (
        len(d_value_char[key_min]) == 1
        and d_char_count[d_value_char[key_min][0]] - 1 == 0
    ) or (
        len(d_value_char[key_max]) == 1
        and d_char_count[d_value_char[key_max][0]] - 1 == 0
    ):
        return True

    return False


def test():
    assert SherlockValidString("xyz") is True
    assert SherlockValidString("xx") is True
    assert SherlockValidString("xxyx") is True
    assert SherlockValidString("xy") is True
    assert SherlockValidString("xyzz") is True
    assert SherlockValidString("xyyzz") is True
    assert SherlockValidString("xyzzz") is False
    assert SherlockValidString("xxyyzz") is True
    assert SherlockValidString("xxxyyzz") is True
    assert SherlockValidString("xxxyyzzz") is False
    assert SherlockValidString("xxxyyzzzzzz") is False
    assert SherlockValidString("zzzzzz") is True
    assert SherlockValidString("zzzzzzx") is True
    assert SherlockValidString("xxyyza") is False
    assert SherlockValidString("xxyyy") is True
    assert SherlockValidString("xxxyy") is True
    assert SherlockValidString("xxxxxyyyyyy") is True

