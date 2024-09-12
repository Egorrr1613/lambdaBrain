def LineAnalysis(line: str) -> bool:
    len_line = len(line)
    half_line_index, is_honest_index = len_line // 2, len_line % 2
    is_honest_index = 0 if is_honest_index == 1 else 1
    left, right = line[:half_line_index], line[: half_line_index - is_honest_index : -1]
    for left_tuple, right_tuple in zip(enumerate(left), enumerate(right)):
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

