def digital_rain(col: str) -> str:
    diff = {0: -1}
    count_0, count_1 = 0, 0
    max_len, max_start, max_end = 1, 0, 1
    for i, ch in enumerate(col):
        if ch == "0":
            count_0 += 1
        else:
            count_1 += 1

        current_diff = count_0 - count_1

        if diff.get(current_diff) is None:
            diff[current_diff] = i
        else:
            current_diff_len = i - diff.get(current_diff)
            is_current_more_then_max = current_diff_len >= max_len
            if is_current_more_then_max:
                max_len = current_diff_len
                max_start = diff.get(current_diff) + 1
                max_end = i

    if len(col) in {count_0, count_1}:
        return ""
    return col[max_start: max_end + 1]


def test():
    assert digital_rain("01") == "01"
    assert digital_rain("010101") == "010101"
    assert digital_rain("011") == "01"
    assert digital_rain("01011") == "0101"
    assert digital_rain("0000010") == "10"
    assert digital_rain("1") == ""
    assert digital_rain("111") == ""
    assert digital_rain("010") == "10"
    assert digital_rain("0110") == "0110"
    assert digital_rain("01110") == "10"
    assert digital_rain("011100") == "011100"
    assert digital_rain("1111000") == "111000"
    assert digital_rain("011111") == "01"
    assert digital_rain("01010101") == "01010101"
    assert digital_rain("01111100") == "1100"
    assert digital_rain("01010000001011100001") == "1011100001"
    assert digital_rain("11101001") == "101001"
    assert digital_rain("1111001000") == "1111001000"
    assert digital_rain("11101000") == "11101000"
    assert digital_rain("111001000") == "11100100"
    assert digital_rain("011111110") == "10"
    assert digital_rain("11111111") == ""
    assert digital_rain("0101000000101110001") == "0101110001"
    assert digital_rain("0101010") == "101010"
    assert digital_rain("01001010") == "100101"
    assert digital_rain("0101001011100010") == "10100101110001"
    assert digital_rain("01010000001011100010") == "1011100010"
    assert digital_rain("00001101100100100000") == "110110010010"

