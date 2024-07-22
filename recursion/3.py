def len_list(input_list: list):
    if bool(input_list):
        input_list.pop()
        return 1 + len_list(input_list)
    else:
        return 0


def test():
    assert len_list([]) == 0
    assert len_list([0]) == 1
    assert len_list([1, 2, 3]) == 3
