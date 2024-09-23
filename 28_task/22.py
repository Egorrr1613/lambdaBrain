def SherlockValidString(s: str) -> bool:
    d_char_count: dict[str, int] = {}
    for char in s:
        if d_char_count.get(char) is None:
            d_char_count[char] = 0
        d_char_count[char] += 1

    d_count_value: dict[int, list] = {}
    for k, v in d_char_count.items():
        if d_count_value.get(v) is None:
            d_count_value[v] = [0]
        d_count_value[v][0] += 1
        d_count_value[v].append(k)

    d_count_value_len = len(d_count_value)
    if d_count_value_len == 1:
        return True
    if d_count_value_len != 2:
        return False
    items = list(d_count_value.items())
    if items[0][1] > items[1][1]:
        max_key, min_key = items[0], items[1]
    else:
        max_key, min_key = items[1], items[0]
    if min_key[0] - 1 == 0 or min_key[0] - 1 == max_key[0]:
        return True
    return False


def test():
    assert SherlockValidString("xyz") is True
    assert SherlockValidString("xx") is True
    assert SherlockValidString("xxyx") is False
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

