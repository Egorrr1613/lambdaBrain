def recursion(inner_list: list, index: int):
    print(inner_list[index])
    if index + 2 < len(inner_list):
        recursion(inner_list, index + 2)


def print_only_even_index(input_list: list):
    if len(input_list) > 0:
        recursion(input_list, 0)


def test(capsys):
    print_only_even_index([])
    captured = capsys.readouterr()
    assert captured.out == ""

    print_only_even_index([1])
    captured = capsys.readouterr()
    assert captured.out == "1\n"

    print_only_even_index([2, 3, 2])
    captured = capsys.readouterr()
    assert captured.out == "2\n2\n"

    print_only_even_index([0, 1, 2, 3, 4, 5])
    captured = capsys.readouterr()
    assert captured.out == "0\n2\n4\n"

    print_only_even_index([0, 1, 2, 3, 4, 5, 6])
    captured = capsys.readouterr()
    assert captured.out == "0\n2\n4\n6\n"

    print_only_even_index([8, 11, 28, 33, 47, 55, 61])
    captured = capsys.readouterr()
    assert captured.out == "8\n28\n47\n61\n"
