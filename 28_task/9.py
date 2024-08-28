def TheRabbitsFoot(s: str, encode: bool) -> str:
    strip_s = s.replace(" ", "")
    row, colum, *_ = calculate_matrix_border(len(strip_s))
    coded_list: list = [[]] * row
    for i in range(row):
        coded_list[i] = [""] * colum

    if encode:
        _code_(list(strip_s), coded_list)
    else:
        _decode_(s.split(" "), coded_list)
    res = ""
    for i in range(row):
        for j in range(colum):
            res += coded_list[i][j]
        if encode:
            res += " "
    res = res.strip()
    return res


def _code_(source_list: list[str], code_list: list) -> None:
    x, y, *_ = [len(code_list[0]), len(code_list)]
    for i_x in range(x):
        for i_y in range(y):
            if len(source_list) == 0:
                return
            code_list[i_y][i_x] = source_list.pop(0)


def _decode_(source_list: list[str], code_list: list) -> None:
    buffer = 1
    x, y = 0, 0
    for i, sublist in enumerate(code_list):
        for j, _ in enumerate(sublist):
            if x > len(source_list[y]) - 1:
                break
            code_list[i][j] = source_list[y][x]
            if y < len(source_list) - 1:
                y += 1
            else:
                y, x = 0, buffer
                buffer += 1


def calculate_matrix_border(matrix_len: int) -> list[int]:
    sqrt = matrix_len**0.5
    row, column = int(sqrt), school_round(sqrt)
    if row * column < matrix_len:
        row += 1
    return [row, column]


def school_round(input_f: float) -> int:
    decimal_list = list(str(input_f).split(".")[1])
    decimal_list_l = len(decimal_list)

    if decimal_list_l > 0:
        return int(input_f) + recursion_dec_round(decimal_list, decimal_list_l, 0)
    return int(input_f)


def recursion_dec_round(dec_list: list[str], dec_len: int, index) -> int:
    if int(dec_list[index]) < 4:
        return 0
    if index >= dec_len - 1:
        return 0 if int(dec_list[index]) < 5 else 1
    return (
        0
        if int(dec_list[index]) + recursion_dec_round(dec_list, dec_len, index + 1) < 5
        else 1
    )


def test():
    assert calculate_matrix_border(21) == [5, 5]
    assert calculate_matrix_border(16) == [4, 4]
    assert calculate_matrix_border(20) == [4, 5]

    assert school_round(15.4571) == 16
    assert school_round(15.4471) == 16
    assert school_round(15.4441) == 15
    assert school_round(15.3441) == 15
    assert school_round(15.4241) == 15
    assert school_round(15.9) == 16
    assert school_round(15.0) == 15
    assert school_round(15.09) == 15
    assert school_round(15.99) == 16

    assert (
        TheRabbitsFoot("отдай мою кроличью лапку", True) == "омоюу толл дюиа акчп йрьк"
    )
    assert TheRabbitsFoot("отдай мою кроличью лапк", True) == "ойкил тмрча дооьп аюлюк"
    assert TheRabbitsFoot("омоюу толл дюиа акчп йрьк", False) == "отдаймоюкроличьюлапку"
    assert TheRabbitsFoot("ойкил тмрча дооьп аюлюк", False) == "отдаймоюкроличьюлапк"
    assert TheRabbitsFoot("дай манку", True) == "дмк аау йн"
    assert TheRabbitsFoot("дмк аау йн", False) == "дайманку"
    assert TheRabbitsFoot("мы он", True) == "мо ын"
    assert TheRabbitsFoot("мо ын", False) == "мыон"
    assert TheRabbitsFoot("солнце ясный день", True) == "сцне оеын ляйь нсд"
    assert TheRabbitsFoot("сцне оеын ляйь нсд", False) == "солнцеясныйдень"

