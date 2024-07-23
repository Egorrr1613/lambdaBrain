def print_only_even(input_list: list):
    if len(input_list) > 0:
        if input_list[0] % 2 == 0:
            print(input_list[0])
        input_list.pop(0)
        return print_only_even(input_list)


def test(capsys):
    print_only_even([])
    captured = capsys.readouterr()
    assert captured.out == ""

    print_only_even([1, 2, 3, 4, 5, 6])
    captured = capsys.readouterr()
    assert captured.out == "2\n4\n6\n"

    print_only_even([2, 2, 2])
    captured = capsys.readouterr()
    assert captured.out == "2\n2\n2\n"

    print_only_even([1])
    captured = capsys.readouterr()
    assert captured.out == ""
