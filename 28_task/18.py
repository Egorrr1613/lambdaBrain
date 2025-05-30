def MisterRobot(n: int, data: list[int]) -> bool:
    return find_inversion(n, data, 0, 1) % 2 == 0


def find_inversion(n: int, data: list[int], current_index: int, compared_index: int) -> int:
    if current_index == n - 2 and compared_index == n:
        return 0
    if compared_index == n:
        current_index += 1
        compared_index = current_index + 1

    return int(data[current_index] > data[compared_index]) + find_inversion(
        n, data, current_index, compared_index + 1
    )


def test():
    assert MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]) is True
    assert MisterRobot(7, [1, 3, 4, 6, 5, 2, 7]) is False
    assert MisterRobot(7, [1, 3, 4, 5, 2, 7, 6]) is True
    assert MisterRobot(5, [1, 3, 2, 5, 4]) is True
    assert MisterRobot(5, [1, 3, 4, 5, 2]) is False
    assert MisterRobot(7, [1, 3, 4, 5, 6, 7, 2]) is False

