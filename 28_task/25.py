def TransformTransform(a: list[int], _: int) -> bool:
    b = transform(a)
    b_after_first_transform = transform(b)
    s = get_sum(b_after_first_transform, 0, len(b_after_first_transform))
    return True if s == 0 else True if s % 2 == 0 else False


def transform(a):
    b = []
    for i, _ in enumerate(a):
        if (len(a) - i - 1) <= 0:
            b.append(i)
        for j in range(len(a) - i - 1):
            k = i + j
            if j > k:
                b.append(j)
                continue
            b.append(k)
    return b


def get_sum(list_l: list[int], index: int, n: int):
    if index == n - 1:
        return list_l[index]
    return list_l[index] + get_sum(list_l, index + 1, n)


def test():
    assert get_sum([1, 2, 3], 0, 3) == 6
    assert get_sum([1], 0, 1) == 1
    assert TransformTransform([9, 9, 9, 9, 9, 9, 9, 9, 9], 9)
    assert TransformTransform([2, 3, 4, 5, 6, 7, 8, 9], 8)
    assert transform([3, 3]) == [0, 1]
    assert TransformTransform([3, 3], 2) is False

