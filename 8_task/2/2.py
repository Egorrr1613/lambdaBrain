def digital_rain(col: str) -> str:
    l_col = len(col)
    if l_col < 2:
        return ""

    current_len_res, current_index_end_res = 0, 0
    last_len_res, last_index_end_res = 0, 0
    biggest_len_res, biggest_index_end_res = 0, 0

    stack, loop_index = [], -2

    stack.append(col[-1])
    while loop_index >= -l_col:

        is_pop_stack = False
        if len(stack) > 0 and col[loop_index] == stack[-1]:
            stack.append(col[loop_index])

        if len(stack) > 0 and col[loop_index] != stack[-1]:
            stack.pop()
            current_len_res += 1
            current_index_end_res = loop_index
            is_pop_stack = True
        if is_pop_stack and len(stack) == 0:
            if (
                current_index_end_res + 2 < 0
                and current_index_end_res + current_len_res * 2 == last_index_end_res
            ):
                current_len_res = current_len_res + last_len_res

            if current_len_res > biggest_len_res:
                biggest_len_res, biggest_index_end_res = (
                    current_len_res,
                    current_index_end_res,
                )

            last_index_end_res = current_index_end_res
            last_len_res = current_len_res

            current_len_res = 0
            current_index_end_res = loop_index
        if not is_pop_stack and len(stack) == 0:
            stack.append(col[loop_index])

        loop_index -= 1

    if len(stack) == l_col:
        return ""

    if not biggest_len_res or current_len_res > biggest_len_res:
        return col[
            current_index_end_res : (
                current_index_end_res + (current_len_res * 2)
                if current_index_end_res + (current_len_res * 2) != 0
                else None
            )
        ]

    return col[
        biggest_index_end_res : (
            biggest_index_end_res + (biggest_len_res * 2)
            if biggest_index_end_res + (biggest_len_res * 2) != 0
            else None
        )
    ]


def test():
    assert digital_rain("1") == ""
    assert digital_rain("111") == ""
    assert digital_rain("01") == "01"
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
    assert digital_rain("01001010") == "1010"
    assert digital_rain("0101001011100010") == "1011100010"
    assert digital_rain("01010000001011100010") == "1011100010"
