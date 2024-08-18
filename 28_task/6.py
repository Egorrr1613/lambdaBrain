def PatternUnlock(n: int, hits: list[int]) -> str:
    matrix: list[[int]] = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    result = "".join(
        list(
            filter(
                lambda x: x != "." and x != "0",
                str(round(recursion_score(hits, matrix, 1, n), 5)),
            )
        )
    )
    return result


def recursion_score(
    hits: list[int], matrix: list[[int]], next_index: int, n: int
) -> int:
    if next_index == n:
        return 0
    current_coordinate, next_coordinate, increment_int = (
        find_coordinate(matrix, hits[next_index - 1]),
        find_coordinate(matrix, hits[next_index]),
        1,
    )
    if (
        current_coordinate[0] != next_coordinate[0]
        and current_coordinate[1] != next_coordinate[1]
    ):
        increment_int = 1.4142135623730951
    return increment_int + recursion_score(hits, matrix, next_index + 1, n)


def find_coordinate(matrix: list[[int]], num: int) -> list[int]:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                return [i, j]


def test():
    assert find_coordinate([[1, 2], [3, 4], [5, 6]], 5) == [2, 0]
    assert find_coordinate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [1, 1]
    assert find_coordinate([[6, 1, 9], [5, 2, 8], [4, 3, 7]], 6) == [0, 0]

    assert PatternUnlock(2, [1, 2]) == "1"
    assert PatternUnlock(9, [1, 2, 3, 4, 5, 2, 8, 7, 3]) == "8"
    assert PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]) == "982843"
    assert PatternUnlock(11, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9, 2]) == "1124264"

