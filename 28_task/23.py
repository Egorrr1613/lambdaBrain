def TreeOfLife(h: int, w: int, n: int, tree: list[str]) -> list[str]:
    tree_map = wrap(h, w, n, tree)
    result = ["".join(list(map(lambda x: "+" if x > 0 else ".", i))) for i in tree_map]
    return result


def wrap(h: int, w: int, n: int, tree: list[str]) -> list[list[int]]:
    tree_map = [[0 if j == "." else 1 for j in tree[i]] for i in range(h)]
    for year in range(n):
        tree_map = [[j + 1 for j in i] for i in tree_map]
        if year > 0 and year % 2 > 0:
            dead_coordinate = collect_dead_coordinate(tree_map, h, w)
            for d in dead_coordinate:
                tree_map[d[0]][d[1]] = 0
    return tree_map


def collect_dead_coordinate(tree_map: list[list[int]], h: int, w: int) -> list[tuple]:
    result = set()
    for k1, v1 in enumerate(tree_map):
        for k2, v2 in enumerate(v1):
            if v2 > 2:
                result.add((k1, k2))

                if k1 > 0:
                    result.add((k1 - 1, k2))
                if k2 > 0:
                    result.add((k1, k2 - 1))
                if k2 < w - 1:
                    result.add((k1, k2 + 1))
                if k1 < h - 1:
                    result.add((k1 + 1, k2))
    return list(result)


def test():
    assert TreeOfLife(1, 1, 1, ["."]) == ["+"]
    assert TreeOfLife(1, 1, 2, ["."]) == ["+"]
    assert TreeOfLife(1, 1, 3, ["."]) == ["+"]
    assert TreeOfLife(1, 1, 4, ["."]) == ["."]

    assert TreeOfLife(1, 1, 1, ["+"]) == ["+"]
    assert TreeOfLife(1, 1, 2, ["+"]) == ["."]
    assert TreeOfLife(1, 1, 3, ["+"]) == ["+"]

    assert TreeOfLife(1, 4, 1, ["+..+"]) == ["++++"]
    assert TreeOfLife(1, 4, 2, ["+..+"]) == ["...."]

    assert TreeOfLife(3, 4, 1, [".+..", "..+.", ".+.."]) == ["++++", "++++", "++++"]
    assert TreeOfLife(3, 4, 2, [".+..", "..+.", ".+.."]) == ["...+", "+...", "...+"]
    assert TreeOfLife(3, 4, 4, [".+..", "..+.", ".+.."]) == [".+..", "..+.", ".+.."]
    assert TreeOfLife(3, 4, 5, [".+..", "..+.", ".+.."]) == ["++++", "++++", "++++"]
    assert TreeOfLife(3, 4, 12, [".+..", "..+.", ".+.."]) == [".+..", "..+.", ".+.."]

    assert wrap(3, 4, 1, [".+..", "..+.", ".+.."]) == [
        [1, 2, 1, 1],
        [1, 1, 2, 1],
        [1, 2, 1, 1],
    ]
    assert wrap(3, 4, 2, [".+..", "..+.", ".+.."]) == [
        [0, 0, 0, 2],
        [2, 0, 0, 0],
        [0, 0, 0, 2],
    ]

    assert sorted(
        collect_dead_coordinate([[2, 3, 2, 2], [2, 2, 3, 2], [2, 3, 2, 2]], 3, 4)
    ) == sorted(
        [(0, 1), (0, 0), (0, 2), (1, 1), (1, 2), (1, 3), (2, 2), (2, 0), (2, 1)]
    )
    assert sorted(collect_dead_coordinate([[1, 1], [3, 1], [1, 1]], 3, 2)) == sorted(
        [(0, 0), (1, 0), (1, 1), (2, 0)]
    )

