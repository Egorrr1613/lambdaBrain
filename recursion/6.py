def print_only_not_even_index(input_list: list, print_index=1):
    if len(input_list) > 0 and print_index < len(input_list):
        print(input_list[print_index])
        print_only_not_even_index(input_list, print_index + 2)


def test(capsys):
    print_only_not_even_index([])
    captured = capsys.readouterr()
    assert captured.out == ""

    print_only_not_even_index([1])
    captured = capsys.readouterr()
    assert captured.out == ""

    print_only_not_even_index([2, 3, 2])
    captured = capsys.readouterr()
    assert captured.out == "3\n"

    print_only_not_even_index([0, 1, 2, 3, 4, 5])
    captured = capsys.readouterr()
    assert captured.out == "1\n3\n5\n"

    print_only_not_even_index([0, 1, 2, 3, 4, 5, 6])
    captured = capsys.readouterr()
    assert captured.out == "1\n3\n5\n"
