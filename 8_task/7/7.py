def matrix(n: int, m: int, input_matrix: list[list[int]]) -> list[int]:
    return recursion(n, m, input_matrix, 0, 0, [])


def recursion(
    n: int,
    m: int,
    input_matrix: list[list[int]],
    start_point_m: int,
    start_point_n: int,
    result: list[int],
):
    if n == 1 and m == 1:
        result.append(input_matrix[start_point_m][start_point_n])
        return result

    for i in range(n * m):
        if i < n:
            result.append(input_matrix[start_point_m][i + start_point_n])
            continue

        if i + 1 < n + m:
            result.append(
                input_matrix[i - (n - 1) + start_point_m][n - 1 + start_point_n]
            )
            continue

        if i + 1 <= m - 2 + 2 * n:
            result.append(
                input_matrix[m - 1 + start_point_m][
                    (m - 2 + 2 * n) - i - 1 + start_point_n
                ]
            )
            continue

        if i + 1 <= 2 * (m - 2) + 2 * n:
            result.append(
                input_matrix[(2 * (m - 2) + 2 * n) - i + start_point_m][start_point_n]
            )
            continue

        return recursion(
            n - 2, m - 2, input_matrix, start_point_m + 1, start_point_n + 1, result
        )

    return result


def test():
    assert matrix(1, 1, [[1]]) == [1]

    assert matrix(3, 1, [[1, 2, 3]]) == [1, 2, 3]

    assert matrix(1, 3, [[1], [2], [3]]) == [1, 2, 3]

    assert matrix(2, 2, [[1, 2], [3, 4]]) == [1, 2, 4, 3]

    assert matrix(2, 3, [[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]

    assert matrix(3, 2, [[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]

    assert matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]

    assert matrix(4, 3, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]

    assert matrix(3, 4, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == [
        1,
        2,
        3,
        6,
        9,
        12,
        11,
        10,
        7,
        4,
        5,
        8,
    ]

    assert matrix(
        4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    ) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    assert matrix(
        5,
        5,
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ],
    ) == [
        1,
        2,
        3,
        4,
        5,
        10,
        15,
        20,
        25,
        24,
        23,
        22,
        21,
        16,
        11,
        6,
        7,
        8,
        9,
        14,
        19,
        18,
        17,
        12,
        13,
    ]

    assert matrix(
        6,
        6,
        [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35, 36],
        ],
    ) == [
        1,
        2,
        3,
        4,
        5,
        6,
        12,
        18,
        24,
        30,
        36,
        35,
        34,
        33,
        32,
        31,
        25,
        19,
        13,
        7,
        8,
        9,
        10,
        11,
        17,
        23,
        29,
        28,
        27,
        26,
        20,
        14,
        15,
        16,
        22,
        21,
    ]
