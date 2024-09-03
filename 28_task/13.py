def UFO(n: int, data: list[int], octal: bool) -> list[int]:
    n += 0
    number_system = 8 if octal else 16

    return list(
        map(
            lambda x: convert_to_ten_system(
                str(x), len(str(x)), number_system, len(str(x)) - 1, 0
            ),
            data,
        )
    )


def convert_to_ten_system(
    input_number: str,
    len_input_str: int,
    input_number_system: int,
    raise_power: int,
    current_index: int,
) -> int:
    if current_index == len_input_str:
        return 0
    return (to_int(input_number[current_index])) * (
        input_number_system**raise_power
    ) + convert_to_ten_system(
        input_number,
        len_input_str,
        input_number_system,
        raise_power - 1,
        current_index + 1,
    )


def to_int(i: str) -> int:
    hex_char = "ABCDEF"
    if i in hex_char:
        return hex_char.index(i) + 10
    return int(i)


def test():
    assert UFO(2, [1234, 1777], False) == [4660, 6007]
    assert UFO(2, [1234, 1777], True) == [668, 1023]
    assert to_int("A") == 10
    assert to_int("F") == 15
    assert to_int("D") == 13
    assert convert_to_ten_system("1234", 4, 8, 3, 0) == 668

