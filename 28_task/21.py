def BiggerGreater(input_str: str) -> str:
    input_list = list(input_str)
    list_combination = get_all_combination(input_list)

    bigger_list = list(
        map(
            "".join,
            filter(lambda x: "".join(x) > input_str, list_combination),
        )
    )

    bigger_len = len(bigger_list)
    if bigger_len == 0:
        return ""
    return find_min(bigger_list, bigger_len, 1, bigger_list[0])


def find_min(input_arr: list[str], len_arr: int, index: int, min_el: str) -> str:
    if index == len_arr:
        return min_el
    compare_res = min_el if input_arr[index] > min_el else input_arr[index]
    return find_min(input_arr, len_arr, index + 1, compare_res)


def get_all_combination(arr):
    res = []

    def permute(sub_arr, remaining_arr):
        if len(remaining_arr) == 0 and sub_arr not in res:
            res.append(sub_arr)
        else:
            for i, c in enumerate(remaining_arr):
                new_remaining = remaining_arr[:i] + remaining_arr[i + 1 :]
                permute(sub_arr + [c], new_remaining)

    permute([], arr)
    return res


def test_combination():
    assert get_all_combination(["a", "b", "c"]) == [
        ["a", "b", "c"],
        ["a", "c", "b"],
        ["b", "a", "c"],
        ["b", "c", "a"],
        ["c", "a", "b"],
        ["c", "b", "a"],
    ]
    assert get_all_combination(["1"]) == [["1"]]


def test():
    assert BiggerGreater("fff") == ""
    assert BiggerGreater("ая") == "яа"
    assert BiggerGreater("abc") == "acb"
    assert BiggerGreater("нклм") == "нкмл"
    assert BiggerGreater("вибк") == "викб"
    assert BiggerGreater("вкиб") == "ибвк"
    assert BiggerGreater("абвг") == "абгв"
    assert BiggerGreater("абвг") == "абгв"
    assert BiggerGreater("гвба") == ""
    assert BiggerGreater("вгба") == "габв"

