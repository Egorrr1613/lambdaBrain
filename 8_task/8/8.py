def army_communication_matrix(n: int, input_matrix: list[list[int]]):
    prefix_matrix: list[list[int]] = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            prefix_matrix[i][j] = input_matrix[i][j]
            if i > 0:
                prefix_matrix[i][j] += prefix_matrix[i - 1][j]
            if j > 0:
                prefix_matrix[i][j] += prefix_matrix[i][j - 1]
            if i > 0 and j > 0:
                prefix_matrix[i][j] -= prefix_matrix[i - 1][j - 1]

    max_sum = float("-inf")
    max_top_left = (0, 0, 0)

    for i in range(n - 1):
        for j in range(n - 1):
            for m in range(1, n - 1):

                if j + m >= n or i + m >= n:
                    continue

                total = prefix_matrix[i + m][j + m]
                if i > 0:
                    total -= prefix_matrix[i - 1][j + m]
                if j > 0:
                    total -= prefix_matrix[i + m][j - 1]
                if i > 0 and j > 0:
                    total += prefix_matrix[i - 1][j - 1]

                if total > max_sum:
                    max_sum = total
                    max_top_left = (j, i, m + 1)

    return " ".join([str(i) for i in max_top_left])


def test():
    assert army_communication_matrix(3, [[1, 2, 3],
                                         [4, 5, 6],
                                         [7, 8, 9]]) == "1 1 2"
    assert (
        army_communication_matrix(
            4, [[1, 9, 2, 3],
                [4, 8, 5, 6],
                [0, 7, 1, 2],
                [0, 0, 0, 0]]
        )
        == "1 0 3"
    )
    assert (
        army_communication_matrix(
            4, [[1000, 9, 2, 3],
                [4, 8, -5000, 6],
                [0, -5000, 1, 2],
                [0, 0, 0, 100]]
        )
        == "0 0 2"
    )
    assert (
        army_communication_matrix(
            4, [[1, -900, 2, 3],
                [4, 8, -500, 6],
                [0, 7, 1, 2],
                [0, 0, 0, 100]]
        )
        == "2 2 2"
    )

