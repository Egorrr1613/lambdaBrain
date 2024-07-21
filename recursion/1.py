def exponentiation(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    ss = exponentiation(n, m - 1)
    res = n * ss
    return res


def test():
    assert exponentiation(3, 3) == 27
    assert exponentiation(3, 0) == 1
    assert exponentiation(3, 1) == 3
