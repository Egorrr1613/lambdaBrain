def digits_sum(a: int):
    if a == 0 or a == 1:
        return a
    return a + digits_sum(a - 1)


def test():
    assert digits_sum(0) == 0
    assert digits_sum(1) == 1
    assert digits_sum(2) == 3
    assert digits_sum(4) == 10
