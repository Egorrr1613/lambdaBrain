def WordSearch(len_sep: int, s: str, subs: str) -> list[int]:
    sep_str: str = separate_string(list(s), len_sep, 0)
    return find_word(sep_str, subs)


def separate_string(
    input_arr: list[str], separator_len: int, start_iter_index: int
) -> str:
    end_iter_index, go_next_iter = start_iter_index + (separator_len - 1), False
    if end_iter_index >= len(input_arr):
        return "".join(input_arr)
    if input_arr[end_iter_index + 1] == " ":
        input_arr[end_iter_index + 1] = "\n"
        go_next_iter = True
        end_iter_index += 1
    while not go_next_iter and end_iter_index >= start_iter_index:
        if input_arr[end_iter_index] == " ":
            input_arr[end_iter_index] = "\n"
            break
        end_iter_index -= 1
    if end_iter_index < start_iter_index:
        input_arr.insert(start_iter_index + separator_len, "\n")
        end_iter_index = start_iter_index + separator_len
    return separate_string(input_arr, separator_len, end_iter_index + 1)


def find_word(s: str, word: str) -> list[int]:
    sep_list, result = s.split("\n"), []
    for i in range(len(sep_list)):
        if is_in_str(sep_list[i], word, 0, 0):
            result.append(1)
        else:
            result.append(0)
    return result


def is_in_str(s: str, word: str, current_index: int, index_word: int) -> bool:
    if index_word == len(word) and (
        current_index > len(s) - 1 or s[current_index] == " "
    ):
        return True
    elif index_word == len(word) or current_index == len(s):
        return False
    if s[current_index] == word[index_word]:
        index_word += 1
    else:
        index_word = 0
    current_index += 1
    return is_in_str(s, word, current_index, index_word)


def test():
    test_str = (
        "1) строка разбивается на набор строк через выравнивание по заданной ширине."
    )
    assert (
        separate_string(list(test_str), 12, 0)
        == "1) строка\nразбивается\nна набор\nстрок через\nвыравнивание\nпо заданной\nширине."
    )
    assert (
        separate_string(list(test_str), 5, 0)
        == "1)\nстрок\nа\nразби\nваетс\nя на\nнабор\nстрок\nчерез\nвырав\nниван\nие по\nзадан\nной\nширин\nе."
    )
    test_str_1, test_str_2, test_str_3 = "1) строка", "на набор", "строк через"
    assert is_in_str(test_str_1, "строк", 0, 0) is False
    assert is_in_str(test_str_2, "строк", 0, 0) is False
    assert is_in_str(test_str_3, "строк", 0, 0) is True

    assert WordSearch(12, test_str, "строк") == [0, 0, 0, 1, 0, 0, 0]
    assert WordSearch(20, test_str, "zzz") == [0, 0, 0, 0, 0]
    assert WordSearch(40, test_str, "1)") == [1, 0]
    assert WordSearch(40, test_str, "по") == [0, 1]
    assert WordSearch(5, test_str, "строк") == [
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]

