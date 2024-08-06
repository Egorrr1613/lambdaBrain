def ConquestCampaign(n: int, m: int, l: int, battalion: list[int]) -> int:
    battlefield = [[]] * n
    for i in range(n):
        battlefield[i] = [0] * m

    drop_coordinate_index_a, drop_coordinate_index_b = 0, 1
    for group in range(l):
        battlefield[battalion[drop_coordinate_index_a] - 1][
            battalion[drop_coordinate_index_b] - 1
        ] = 1
        drop_coordinate_index_a += 2
        drop_coordinate_index_b += 2

    return recursion(battlefield)


def recursion(battlefield: list[[int]]) -> int:
    n, m = len(battlefield), len(battlefield[0])
    i, j, all_capture = 0, 0, True
    while i < n:
        while j < m:
            if battlefield[i][j] == 1:
                battlefield[i][j] = 2
            if all_capture and battlefield[i][j] == 0:
                all_capture = False
            j += 1
        j = 0
        i += 1

    if all_capture:
        return 1

    i, j = 0, 0
    while i < n:
        while j < m:
            if battlefield[i][j] < 2 and (
                (i + 1 < n and battlefield[i + 1][j] == 2)
                or (j + 1 < m and battlefield[i][j + 1] == 2)
                or (i - 1 > -1 and battlefield[i - 1][j] == 2)
                or (j - 1 > -1 and battlefield[i][j - 1] == 2)
            ):
                battlefield[i][j] = 1
            j += 1
        j = 0
        i += 1

    return 1 + recursion(battlefield)


def test():
    assert ConquestCampaign(1, 1, 1, [1, 1]) == 1
    assert ConquestCampaign(3, 4, 2, [2, 2, 3, 4]) == 3
    assert ConquestCampaign(2, 2, 1, [1, 1]) == 3

