def LineAnalysis(line: str) -> bool:
    len_line = len(line)
    half_line_index, is_honest_index = len_line // 2, len_line % 2
    is_honest_index = 0 if is_honest_index == 1 else 1
    left_half_of_line = line[:half_line_index]
    right_half_of_line = line[: half_line_index - is_honest_index : -1]
    for left_tuple, right_tuple in zip(enumerate(left_half_of_line), enumerate(right_half_of_line)):
        if not left_tuple[1] == right_tuple[1]:
            return False
    return True


def test():
    assert LineAnalysis("*..*..*..*..*..*..*") is True
    assert LineAnalysis("*..*..*..*..*..*..*..*") is True
    assert LineAnalysis("*..*...*..*..*..*..*") is False
    assert LineAnalysis("*..*..*..*..*..**..*") is False
    assert LineAnalysis("*") is True
    assert LineAnalysis("***") is True
    assert LineAnalysis("*.......*.......*") is True
    assert LineAnalysis("**") is True
    assert LineAnalysis("*.*") is True

