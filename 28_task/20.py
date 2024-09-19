result_str: str = ""
buffer, buffer_index = [""], 0


def BastShoe(command: str) -> str:
    com, *arg = command.split(maxsplit=1)
    match com:
        case "1":
            add(arg[0])
        case "2":
            delete(int(arg[0]))
        case "3":
            return get(int(arg[0]))
        case "4":
            undo()
        case "5":
            redo()

    return result_str


def add(added_str: str):
    global result_str, buffer_index, buffer
    if buffer_index < len(buffer) - 1:
        buffer = [result_str]
        buffer_index = 0
    result_str = result_str + added_str
    buffer.append(result_str)
    buffer_index += 1


def delete(n: int):
    global result_str, buffer_index, buffer
    len_res = len(result_str)
    if buffer_index < len(buffer) - 1:
        buffer = [result_str]
        buffer_index = 0
    if n >= len_res:
        result_str = ""
    result_str = result_str[: len_res - n]
    buffer.append(result_str)
    buffer_index += 1


def undo():
    global buffer_index, result_str
    if buffer_index <= 0:
        return
    buffer_index -= 1
    result_str = buffer[buffer_index]


def redo():
    global buffer_index, result_str
    if buffer_index == (len(buffer) - 1):
        return
    buffer_index += 1
    result_str = buffer[buffer_index]


def get(i: int):
    if i > (len(result_str) - 1):
        return ''
    return result_str[i]


def test():
    global result_str, buffer_index, buffer
    assert BastShoe("1 aa") == "aa"
    assert BastShoe("1 aa") == "aaaa"
    assert BastShoe("2 8") == ""
    assert BastShoe("1 abcd") == "abcd"
    assert BastShoe("3 2") == "c"
    assert buffer_index == 4
    assert buffer == ["", "aa", "aaaa", "", "abcd"]
    assert BastShoe("4") == ""
    assert buffer == ["", "aa", "aaaa", "", "abcd"]
    assert buffer_index == 3
    assert BastShoe("4") == "aaaa"
    assert buffer == ["", "aa", "aaaa", "", "abcd"]
    assert buffer_index == 2
    assert BastShoe("1 99") == "aaaa99"
    assert buffer == ["aaaa", "aaaa99"]
    assert buffer_index == 1

    result_str, buffer_index, buffer = "", 0, [""]


def test2():
    global result_str, buffer_index, buffer
    assert BastShoe("1 Привет") == "Привет"
    assert BastShoe("1  , Мир!") == "Привет, Мир!"
    assert BastShoe("1 ++") == "Привет, Мир!++"
    assert BastShoe("2 2") == "Привет, Мир!"
    assert BastShoe("4") == "Привет, Мир!++"
    assert BastShoe("4") == "Привет, Мир!"
    assert BastShoe("1 *") == "Привет, Мир!*"
    assert BastShoe("4") == "Привет, Мир!"
    assert BastShoe("4") == "Привет, Мир!"
    assert BastShoe("4") == "Привет, Мир!"
    assert BastShoe("3 6") == ","
    assert BastShoe("2 100") == ""
    assert BastShoe("1 Привет") == "Привет"
    assert BastShoe("1  , Мир!") == "Привет, Мир!"
    assert BastShoe("1 ++") == "Привет, Мир!++"
    assert BastShoe("4") == "Привет, Мир!"
    assert BastShoe("4") == "Привет"
    assert BastShoe("5") == "Привет, Мир!"
    assert BastShoe("4") == "Привет"
    assert BastShoe("5") == "Привет, Мир!"
    assert BastShoe("5") == "Привет, Мир!++"
    assert BastShoe("5") == "Привет, Мир!++"
    assert BastShoe("5") == "Привет, Мир!++"
    assert BastShoe("4") == "Привет, Мир!"
    assert BastShoe("4") == "Привет"
    assert BastShoe("2 2") == "Прив"
    assert BastShoe("4") == "Привет"
    assert BastShoe("5") == "Прив"
    assert BastShoe("5") == "Прив"
    assert BastShoe("5") == "Прив"
    result_str, buffer_index, buffer = "", 0, [""]


def test3():
    assert BastShoe("4") == ""
    assert BastShoe("4") == ""
    assert BastShoe("4") == ""
    assert buffer == [""]
    assert buffer_index == 0
    assert BastShoe("5") == ""
    assert BastShoe("5") == ""
    assert BastShoe("5") == ""
    assert buffer == [""]
    assert buffer_index == 0
    assert BastShoe("1 xxx") == "xxx"
    assert buffer == ["", "xxx"]
    assert buffer_index == 1
    assert BastShoe('3 10') == ''
    assert BastShoe('3 2') == 'x'
    assert BastShoe('3 3') == ''
