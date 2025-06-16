BYTE_SIZE = 8


def artificial_muscle_fibers(arr: list[int]) -> int:
    size_local_buffer_in_bytes = 32000
    half_bytes = size_local_buffer_in_bytes // 2
    buffer, unique_duplicate_count = bytearray(size_local_buffer_in_bytes), 0

    for i in arr:
        i_byte = (i // BYTE_SIZE) - 1 if i % BYTE_SIZE == 0 else i // BYTE_SIZE
        i_bite = BYTE_SIZE - (BYTE_SIZE * (i_byte + 1) - i) - 1
        bites_with_meet_number_first_time = buffer[i_byte]

        is_number_meet_first_time = (bites_with_meet_number_first_time ^ (
                bites_with_meet_number_first_time | 1 << i_bite)) != 0
        if is_number_meet_first_time:
            buffer[i_byte] = bites_with_meet_number_first_time | 1 << i_bite
            continue

        is_number_meet_second_time = ((bites_with_meet_number_first_time >> i_bite) & 0b000001) ^ (
                (buffer[i_byte + half_bytes] >> i_bite) & 0b000001
        ) != 0
        if is_number_meet_second_time:
            unique_duplicate_count += 1
            buffer[i_byte + half_bytes] = buffer[i_byte + half_bytes] | 1 << i_bite
    return unique_duplicate_count


def test():
    assert artificial_muscle_fibers([1]) == 0
    assert artificial_muscle_fibers([1, 1]) == 1
    assert artificial_muscle_fibers([1, 2]) == 0
    assert artificial_muscle_fibers([1, 1, 1]) == 1
    assert artificial_muscle_fibers([1, 1, 2]) == 1
    assert artificial_muscle_fibers([1, 2, 1, 2]) == 2
    assert artificial_muscle_fibers([1, 1, 2, 2]) == 2
    assert artificial_muscle_fibers([1, 3, 10, 13]) == 0
    assert artificial_muscle_fibers([1, 2, 3, 4, 5]) == 0
    assert artificial_muscle_fibers([1, 2, 3, 2, 1]) == 2
    assert artificial_muscle_fibers([1, 2, 6, 2, 2, 1]) == 2
    assert artificial_muscle_fibers([39, 40, 2, 3, 2, 1]) == 1
    assert artificial_muscle_fibers([1, 2, 3, 2, 1, 2, 4, 2, 1]) == 2
    assert (
            artificial_muscle_fibers([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17, 18])
            == 0
    )
    assert (
            artificial_muscle_fibers(
                [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17, 18, 18]
            )
            == 1
    )
