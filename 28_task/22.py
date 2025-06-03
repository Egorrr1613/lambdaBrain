def SherlockValidString(s: str) -> bool:
    symbol_counter_as_dict: dict[str, int] = {}
    for symbol in s:
        if symbol_counter_as_dict.get(symbol) is None:
            symbol_counter_as_dict[symbol] = 0
        symbol_counter_as_dict[symbol] += 1

    frequency_symbols: dict[int, list[str]] = {}
    for symbol, symbol_count in symbol_counter_as_dict.items():
        if frequency_symbols.get(symbol_count) is None:
            frequency_symbols[symbol_count] = []
        frequency_symbols[symbol_count].append(symbol)

    frequency_symbols_len = len(frequency_symbols)
    if frequency_symbols_len == 1:
        return True
    if frequency_symbols_len != 2:
        return False

    items = list(frequency_symbols.items())
    if len(items[0][1]) > len(items[1][1]):
        key_max, key_min = items[0][0], items[1][0]
    else:
        key_max, key_min = items[1][0], items[0][0]

    if (
        len(frequency_symbols[key_min]) == 1
        and symbol_counter_as_dict[frequency_symbols[key_min][0]] - 1
        == symbol_counter_as_dict[frequency_symbols[key_max][0]]
    ):
        return True
    if (
        len(frequency_symbols[key_max]) == 1
        and symbol_counter_as_dict[frequency_symbols[key_max][0]] - 1
        == symbol_counter_as_dict[frequency_symbols[key_min][0]]
    ):
        return True

    if (
        len(frequency_symbols[key_min]) == 1
        and symbol_counter_as_dict[frequency_symbols[key_min][0]] - 1 == 0
    ) or (
        len(frequency_symbols[key_max]) == 1
        and symbol_counter_as_dict[frequency_symbols[key_max][0]] - 1 == 0
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

