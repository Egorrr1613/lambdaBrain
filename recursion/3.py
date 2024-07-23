def len_list(input_list: list):
    if len(input_list) == 0:
        return 0
    input_list.pop()
    return 1 + len_list(input_list)


def test():
    assert len_list([]) == 0
    assert len_list([0]) == 1
    assert len_list([1, 2, 3]) == 3
