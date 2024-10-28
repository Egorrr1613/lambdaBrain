def EEC_help(arr1: list[int], arr2: list[int]) -> bool:
    l1 = len(arr1)
    if l1 != len(arr2):
        return False

    store: dict[int, int] = {}
    for i in range(l1):
        if store.get(arr1[i]):
            store[arr1[i]] += 1
        else:
            store[arr1[i]] = 1
        if store.get(arr2[i]):
            store[arr2[i]] -= 1
        else:
            store[arr2[i]] = -1

        if store[arr1[i]] == 0:
            store.pop(arr1[i])
        if store.get(arr2[i]) is not None and store[arr2[i]] == 0:
            store.pop(arr2[i])

    return len(store) == 0


def test():
    assert EEC_help([1, 2, 3], [1, 2, 3, 4]) is False
    assert EEC_help([1, 2, 3], [1, 2, 3])
    assert EEC_help([1, 3, 2], [1, 2, 3])
    assert EEC_help([1, 3, 2, 3], [1, 2, 2, 3]) is False
    assert EEC_help([1, 1], [1, 1])

