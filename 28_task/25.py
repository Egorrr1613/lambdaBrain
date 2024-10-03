def TransformTransform(a: list[int], _: int) -> bool:
    b = transform(a)
    b_after_first_transform = transform(b)
    s = sum(b_after_first_transform)
    if s % 2 != 0:
        return False
    return True


def transform(a):
    b = []
    for i, _ in enumerate(a):
        for j in range(0, len(a) - i):
            k = i + j
            a_slice = a[j : k + 1]
            max_int = get_max(a_slice, 1, len(a_slice), a[j])
            b.append(max_int)

    return b


def get_max(list_l: list[int], index: int, n: int, result: int) -> int:
    if index == n:
        return result
    if list_l[index] > result:
        result = list_l[index]
    return get_max(list_l, index + 1, n, result)


def test():
    assert TransformTransform([9, 9, 9, 9, 9], 5)
    assert TransformTransform([2, 3, 4, 5, 6, 7, 8, 9], 8)
    long_arr = [1, 2, 1, 7, 2, 4, 3, 1, 5, 1, 2, 1, 6, 1, 2]
    assert TransformTransform(long_arr, len(long_arr)) is False
    assert TransformTransform([3, 3], 2)
    assert transform([3, 3]) == [3, 3, 3]
    a = transform([3, 2, 1])
    aa = transform(a)
    assert sum(aa) == 58
    assert TransformTransform([3, 2, 1], 3)

