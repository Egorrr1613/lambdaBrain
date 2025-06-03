def odometer(oksana: list) -> int:
    if len(oksana) < 2:
        return 0
    return recursion(oksana, 1)


def recursion(oksana: list, time_index: int) -> int:
    current_time_slot = (
        oksana[time_index]
        if time_index == 1
        else oksana[time_index] - oksana[time_index - 2]
    )

    if time_index == len(oksana) - 1:
        return oksana[time_index - 1] * current_time_slot
    return oksana[time_index - 1] * current_time_slot + recursion(oksana, time_index + 2)


def test():
    assert odometer([1]) == 0
    assert odometer([10, 4]) == 40
    assert odometer([10, 1, 20, 2]) == 30
    assert odometer([10, 1, 20, 5]) == 90
    assert odometer([10, 1, 20, 5, 5, 8]) == 105

