def artificial_muscle_fibers(arr: list[int]) -> int:
    size_local_buffer_in_bytes = 32000
    half_bytes = size_local_buffer_in_bytes // 2
    buffer, unique_duplicate_count = bytearray(size_local_buffer_in_bytes), 0

    for i in arr:
        i_byte = (i // 8) - 1 if i % 8 == 0 else i // 8
        i_bite = 8 - (8 * (i_byte + 1) - i) - 1
        bites_with_meet_number_first_time = buffer[i_byte]

        if (bites_with_meet_number_first_time ^ (bites_with_meet_number_first_time | 1 << i_bite)) != 0:
            buffer[i_byte] = bites_with_meet_number_first_time | 1 << i_bite
            continue

        if ((bites_with_meet_number_first_time >> i_bite) & 0b000001) ^ (
            (buffer[i_byte + half_bytes] >> i_bite) & 0b000001
        ) != 0:
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
