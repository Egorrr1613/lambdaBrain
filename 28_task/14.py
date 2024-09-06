def Unmanned(len_road: int, n: int, track: list[list[int]]) -> int:
    road: list[list] = [[]] * len_road
    for light_index in range(n):
        if len_road <= track[light_index][0]:
            continue
        road[track[light_index][0]] = track[light_index]
    time = lets_go(road, len_road, 0, 0)
    return time


def get_time_after_light(current_time: int, periods: list[int]) -> int:
    light_cycle = periods[1] + periods[2]
    if current_time < periods[1]:
        return current_time + (periods[1] - current_time)
    if periods[1] < current_time < light_cycle:
        return current_time

    count_cycle = current_time // light_cycle
    current_light_time = current_time - (count_cycle * light_cycle)
    if current_light_time >= periods[1]:
        return current_time
    return current_time + (periods[1] - current_light_time)


def lets_go(road: list[list], road_len: int, time: int, position_index: int) -> int:
    if position_index == road_len:
        return time
    if road[position_index]:
        time = get_time_after_light(time, road[position_index])
    return lets_go(road, road_len, time + 1, position_index + 1)


def test():
    assert Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]) == 12
    assert Unmanned(5, 1, [[3, 6, 6]]) == 8
    assert Unmanned(5, 1, [[3, 10, 10]]) == 12
    assert Unmanned(10, 2, [[11, 5, 5], [15, 2, 2]]) == 10
    assert Unmanned(5, 2, [[5, 6, 6], [15, 2, 2]]) == 5
    assert get_time_after_light(3, [3, 5, 5]) == 5
    assert get_time_after_light(7, [0, 5, 5]) == 7
    assert get_time_after_light(14, [0, 3, 3]) == 15
    assert get_time_after_light(15, [0, 3, 3]) == 15
    assert get_time_after_light(13, [0, 3, 3]) == 15
    assert get_time_after_light(12, [0, 3, 3]) == 15
    assert get_time_after_light(10, [0, 3, 3]) == 10
    assert get_time_after_light(9, [0, 3, 3]) == 9
    assert get_time_after_light(7, [0, 3, 3]) == 9
    assert get_time_after_light(6, [0, 3, 3]) == 9
    assert get_time_after_light(5, [0, 3, 3]) == 5
    assert get_time_after_light(3, [0, 3, 3]) == 3
