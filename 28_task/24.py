def MatrixTurn(matrix: list[str], m: int, n: int, t: int) -> None:
    count_axis = get_count_axis(m, n)
    map_axis_and_coordinate = {}
    for iteration_index in range(count_axis):
        map_axis_and_coordinate[iteration_index] = [
            (iteration_index, iteration_index),
            (m - iteration_index, n - iteration_index),
        ]

    matrix_list = [list(row) for row in matrix]

    for iteration_index in range(t):
        for axis_index in range(count_axis):
            move_one_axis(
                matrix_list,
                map_axis_and_coordinate[axis_index][0],
                map_axis_and_coordinate[axis_index][0],
                map_axis_and_coordinate[axis_index][1],
                None,
                1,
                0,
            )

    matrix_buffer = list(map("".join, matrix_list))
    for k, v in enumerate(matrix_buffer):
        matrix[k] = v


def get_count_axis(m: int, n: int) -> int:
    if m > n:
        return n // 2
    return m // 2


def move_one_axis(
        matrix: list[list[str]],
        axis_i: tuple[int, int],
        start: tuple[int, int],
        end: tuple[int, int],
        init_val: str | None,
        indexing: int,
        iteration: int,
) -> list[str]:
    if init_val is None and iteration == 3:
        return []

    if indexing == 1 and axis_i[indexing] == end[indexing] and iteration == 0:
        return move_one_axis(
            matrix,
            (axis_i[0] + 1, axis_i[1] - 1),
            start,
            end,
            init_val,
            0,
            iteration + 1,
        )

    if indexing == 0 and axis_i[indexing] == end[indexing] and iteration == 1:
        return move_one_axis(
            matrix,
            (axis_i[0] - 1, axis_i[1] - 1),
            start,
            end,
            init_val,
            1,
            iteration + 1,
        )

    if indexing == 1 and axis_i[indexing] == start[indexing] - 1 and iteration == 2:
        return move_one_axis(
            matrix,
            (axis_i[0] - 1, axis_i[1] + 1),
            start,
            end,
            init_val,
            0,
            iteration + 1,
        )

    if indexing == 0 and axis_i[indexing] == start[indexing] - 1 and iteration == 3:
        return move_one_axis(
            matrix,
            (axis_i[0] + 1, axis_i[1] - 1),
            start,
            end,
            init_val,
            1,
            iteration + 1,
        )

    buffer = matrix[axis_i[0]][axis_i[1]]
    matrix[axis_i[0]][axis_i[1]] = init_val

    if iteration == 0:
        next_axis_i = (axis_i[0], axis_i[1] + 1)
    elif iteration == 1:
        next_axis_i = (axis_i[0] + 1, axis_i[1])
    elif iteration == 2:
        next_axis_i = (axis_i[0], axis_i[1] - 1)
    else:
        next_axis_i = (axis_i[0] - 1, axis_i[1])

    return move_one_axis(matrix, next_axis_i, start, end, buffer, indexing, iteration)


def test():
    matrix = ["123", "234", "345"]
    MatrixTurn(matrix, 3, 3, 1)
    assert matrix == ["212", "333", "454"]

    matrix = ["12", "34"]
    MatrixTurn(matrix, 2, 2, 1)
    assert matrix == ["31", "42"]

    matrix = ["12", "34"]
    MatrixTurn(matrix, 2, 2, 2)
    assert matrix == ["43", "21"]

    matrix = ["12", "23", "34", "45"]
    MatrixTurn(matrix, 4, 2, 1)
    assert matrix == ["21", "32", "43", "54"]

    matrix = ["1234", "2345"]
    MatrixTurn(matrix, 2, 4, 1)
    assert matrix == ["2123", "3454"]

    matrix = ["1234", "2345", "3456", "4567"]
    MatrixTurn(matrix, 4, 4, 1)
    assert matrix == ["2123", "3434", "4545", "5676"]

    matrix = ["123456", "234567", "345678", "456789"]
    MatrixTurn(matrix, 4, 6, 1)
    assert matrix == ["212345", "343456", "456767", "567898"]

    matrix = ["123456", "234567", "345678", "456789"]
    MatrixTurn(matrix, 4, 6, 2)
    assert matrix == ["321234", "454345", "567656", "678987"]


def test_get_count_axis():
    assert get_count_axis(2, 2) == 1
    assert get_count_axis(4, 2) == 1
    assert get_count_axis(4, 4) == 2
    assert get_count_axis(4, 4) == 2
    assert get_count_axis(5, 4) == 2

