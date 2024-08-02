def squirrel(n: int) -> int:
    if n == 0:
        return 0
    return int(str(fact(n))[0])


def fact(input_int: int) -> int:
    if input_int == 1:
        return 1
    else:
        return input_int * (fact(input_int - 1))


def test():
    assert squirrel(0) == 0
    assert squirrel(1) == 1
    assert squirrel(4) == 2
    assert squirrel(14) == 8

