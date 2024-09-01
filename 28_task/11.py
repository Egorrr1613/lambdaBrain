def BigMinus(input1: str, input2: str) -> str:
    l_s1, l_s2 = len(input1), len(input2)
    s1, s2, *_ = zero_left_padding_str(input1, l_s1, input2, l_s2)
    max_str = find_max(s1, s2)
    if max_str == 0:
        return "0"
    return unpadding_str(
        _minus_(s1, s2, l_s1) if max_str == 1 else _minus_(s2, s1, l_s2)
    )


def zero_left_padding_str(i1: str, l1: int, i2: str, l2: int) -> list[str]:
    if l1 < l2:
        i1 = ((l2 - l1) * "0") + i1
    if l2 < l1:
        i2 = ((l1 - l2) * "0") + i2
    return [i1, i2]


def unpadding_str(input_str: str):
    while len(input_str) > 1:
        if input_str[0] != "0":
            break
        input_str = input_str[1:]
    return input_str


def find_max(s1, s2) -> int:
    for first_s, second_s in zip(enumerate(s1), enumerate(s2)):
        if first_s[1] > second_s[1]:
            return 1
        if first_s[1] < second_s[1]:
            return 2
    return 0


def _minus_(s_max: str, s_min: str, len_strs: int) -> str:
    result, next_int_minus_buffer, current_minus = "", 0, 0

    for i in range(-1, -(len_strs + 1), -1):
        if next_int_minus_buffer == 1:
            current_minus = 1
            next_int_minus_buffer = 0
        if int(s_max[i]) - int(s_min[i]) < 0:
            next_int_minus_buffer = 1
        raznost = str(
            (10 * next_int_minus_buffer + int(s_max[i]) - current_minus) - int(s_min[i])
        )
        current_minus = 0
        result = raznost + result
    return result


def test():
    assert BigMinus("99999999999999999", "19999999999999991") == "80000000000000008"
    assert BigMinus("99999999999999999", "99999999999999998") == "1"
    assert BigMinus("1234567891", "1") == "1234567890"
    assert BigMinus("1", "321") == "320"
    assert BigMinus("8", "15") == "7"
    assert BigMinus("15", "7") == "8"
    assert BigMinus("5", "3") == "2"
    assert zero_left_padding_str("12345678", 8, "123", 3) == ["12345678", "00000123"]
    assert zero_left_padding_str("123", 3, "12345678", 8) == ["00000123", "12345678"]
    assert zero_left_padding_str("1", 1, "2", 1) == ["1", "2"]

