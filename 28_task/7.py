def WordSearch(len_sep: int, s: str, word_to_search_in_text: str) -> list[int]:
    str_with_new_line_symbol: str = separate_string(list(s), len_sep, 0)
    return find_word(str_with_new_line_symbol, word_to_search_in_text)


def separate_string(
    symbols_by_text_list: list[str], separator_len: int, start_iter_index: int
) -> str:
    end_iter_index, go_next_iter = start_iter_index + (separator_len - 1), False
    if end_iter_index >= len(symbols_by_text_list):
        return "".join(symbols_by_text_list)
    if symbols_by_text_list[end_iter_index + 1] == " ":
        symbols_by_text_list[end_iter_index + 1] = "\n"
        go_next_iter = True
        end_iter_index += 1
    while not go_next_iter and end_iter_index >= start_iter_index:
        if symbols_by_text_list[end_iter_index] == " ":
            symbols_by_text_list[end_iter_index] = "\n"
            break
        end_iter_index -= 1
    if end_iter_index < start_iter_index:
        symbols_by_text_list.insert(start_iter_index + separator_len, "\n")
        end_iter_index = start_iter_index + separator_len
    return separate_string(symbols_by_text_list, separator_len, end_iter_index + 1)


def find_word(s: str, word: str) -> list[int]:
    list_with_split_words = s.split("\n")
    is_find_word_flag_list = []
    for word_index in range(len(list_with_split_words)):
        if is_in_str(list_with_split_words[word_index], word, 0, 0):
            is_find_word_flag_list.append(1)
        else:
            is_find_word_flag_list.append(0)
    return is_find_word_flag_list


def is_in_str(string_for_search: str, word: str, current_index: int, index_word: int) -> bool:
    if index_word == len(word) and (
            current_index > len(string_for_search) - 1 or string_for_search[current_index] == " "
    ):
        return True
    if index_word == len(word) or current_index == len(string_for_search):
        return False
    if string_for_search[current_index] == word[index_word]:
        index_word += 1
    else:
        index_word = 0
    current_index += 1
    return is_in_str(string_for_search, word, current_index, index_word)


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

