from ASD_FIRST.nine_associate_list.native_dict import NativeDictionary


def test_put_empty_dict():
    n = NativeDictionary(9)

    assert n.get("aaa") is None
    assert not n.is_key("aaa")


def test_put_dict():
    n = NativeDictionary(9)

    assert n.hash_fun("zxc") == 8
    assert n.put(key="zxc", value=99) == 8
    assert n.get("zxc") == 99
    assert n.is_key("zxc")

    assert n.put(key="zxc", value=11) == 8
    assert n.get("zxc") == 11


def test_put_more_collision():
    """Заполняем хеш таблицу значениями, для которых хеш сумма равна одному и тому же числу (1)"""
    n = NativeDictionary(sz=17)

    assert n.put(key='4', value=7) == 1
    assert n.put(key='43', value=14) == 4
    assert n.put(key='433', value=21) == 7
    assert n.put(key='4333', value=28) == 10
    assert n.put(key='43333', value=35) == 13
    assert n.put(key='433333', value=42) == 16
    assert n.put(key='4333333', value=49) == 1

    assert n.get("4333333") == 49
