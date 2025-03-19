from ASD_FIRST.seven_lesson_sort_list.ordered_list import OrderedStringList


def test_order_list_add_one_el():
    o = OrderedStringList(asc=True)
    o.add("4")
    assert o.get_all_v2() == [(None, "4", None)]
    assert o.len() == 1


def test_order_list_add_in_head_0():
    o = OrderedStringList(asc=True)
    o.add("10")
    o.add("1")
    assert o.get_all_v2() == [(None, "1", "10"), ("1", "10", None)]
    assert o.len() == 2

    o = OrderedStringList(asc=False)
    o.add("10")
    o.add("1")
    assert o.get_all_v2() == [(None, "10", "1"), ("10", "1", None)]
    assert o.len() == 2


def test_order_list_add_in_head_1():
    o = OrderedStringList(asc=True)
    o.add("5")
    o.add("10")
    o.add("1")
    assert o.get_all_v2() == [(None, "1", "10"), ("1", "10", "5"), ("10", "5", None)]
    assert o.len() == 3

    o = OrderedStringList(asc=False)
    o.add("5")
    o.add("10")
    o.add("1")
    assert o.get_all_v2() == [(None, "5", "10"), ("5", "10", "1"), ("10", "1", None)]
    assert o.len() == 3


def test_order_list_add_in_tail_0():
    o = OrderedStringList(asc=True)
    o.add("10")
    o.add("11")
    assert o.get_all_v2() == [(None, "10", "11"), ("10", "11", None)]
    assert o.len() == 2

    o = OrderedStringList(asc=False)
    o.add("10")
    o.add("11")
    assert o.get_all_v2() == [(None, "11", "10"), ("11", "10", None)]
    assert o.len() == 2


def test_order_list_add_in_tail_1():
    o = OrderedStringList(asc=True)
    o.add("5")
    o.add("10")
    o.add("11")
    assert o.get_all_v2() == [(None, "10", "11"), ("10", "11", "5"), ("11", "5", None)]
    assert o.len() == 3

    o = OrderedStringList(asc=False)
    o.add("5")
    o.add("10")
    o.add("11")
    assert o.get_all_v2() == [(None, "5", "11"), ("5", "11", "10"), ("11", "10", None)]
    assert o.len() == 3


def test_order_list_add_1():
    o = OrderedStringList(asc=True)
    o.add("1")
    o.add("2")
    o.add("3")

    assert o.get_all_v2() == [(None, "1", "2"), ("1", "2", "3"), ("2", "3", None)]
    assert o.len() == 3

    o = OrderedStringList(asc=False)
    o.add("1")
    o.add("2")
    o.add("3")

    assert o.get_all_v2() == [(None, "3", "2"), ("3", "2", "1"), ("2", "1", None)]
    assert o.len() == 3

    o = OrderedStringList(asc=True)
    o.add("3")
    o.add("2")
    o.add("1")

    assert o.get_all_v2() == [(None, "1", "2"), ("1", "2", "3"), ("2", "3", None)]
    assert o.len() == 3

    o = OrderedStringList(asc=False)
    o.add("3")
    o.add("2")
    o.add("1")

    assert o.get_all_v2() == [(None, "3", "2"), ("3", "2", "1"), ("2", "1", None)]
    assert o.len() == 3


def test_order_add_elements_in_mid():
    o = OrderedStringList(asc=True)
    o.add("1")
    o.add("20")
    assert o.get_all_v2() == [(None, "1", "20"), ("1", "20", None)]

    o.add("3")
    assert o.get_all_v2() == [(None, "1", "20"), ("1", "20", "3"), ("20", "3", None)]
    assert o.len() == 3

    o.add("5")
    o.add("14")
    assert o.get_all_v2() == [
        (None, "1", "14"),
        ("1", "14", "20"),
        ("14", "20", "3"),
        ("20", "3", "5"),
        ("3", "5", None),
    ]
    assert o.len() == 5


def test_order_add_elements_in_mid_reverse_asc():
    o = OrderedStringList(asc=False)
    o.add("1")
    o.add("20")
    assert o.get_all_v2() == [(None, "20", "1"), ("20", "1", None)]

    o.add("3")
    assert o.get_all_v2() == [(None, "3", "20"), ("3", "20", "1"), ("20", "1", None)]
    assert o.len() == 3

    o.add("5")
    o.add("14")
    assert o.get_all_v2() == [
        (None, "5", "3"),
        ("5", "3", "20"),
        ("3", "20", "14"),
        ("20", "14", "1"),
        ("14", "1", None),
    ]
    assert o.len() == 5


def test_del_0_elements():
    o = OrderedStringList(asc=True)
    o.delete("55")
    assert not o.get_all()
    assert o.len() == 0

    o.add("33")
    assert o.get_all() == ["33"]

    o.delete("23")
    assert o.get_all() == ["33"]

    o.delete("33")
    assert not o.get_all()
    assert o.len() == 0


def test_del_1():
    o = OrderedStringList(asc=True)
    o.add("1")
    o.add("20")
    o.add("3")
    o.add("5")
    o.add("14")
    assert o.get_all_v2() == [
        (None, "1", "14"),
        ("1", "14", "20"),
        ("14", "20", "3"),
        ("20", "3", "5"),
        ("3", "5", None),
    ]
    assert o.len() == 5

    o.delete("1")
    assert o.get_all_v2() == [
        (None, "14", "20"),
        ("14", "20", "3"),
        ("20", "3", "5"),
        ("3", "5", None),
    ]
    assert o.len() == 4

    o.delete("5")
    assert o.get_all_v2() == [(None, "14", "20"), ("14", "20", "3"), ("20", "3", None)]
    assert o.len() == 3

    o.delete("20")
    assert o.get_all_v2() == [(None, "14", "3"), ("14", "3", None)]
    assert o.len() == 2


def test_del_1_asc_false():
    o = OrderedStringList(asc=False)
    o.add("1")
    o.add("20")
    o.add("3")
    o.add("5")
    o.add("14")
    assert o.get_all_v2() == [
        (None, "5", "3"),
        ("5", "3", "20"),
        ("3", "20", "14"),
        ("20", "14", "1"),
        ("14", "1", None),
    ]
    assert o.len() == 5

    o.delete("1")
    assert o.get_all_v2() == [
        (None, "5", "3"),
        ("5", "3", "20"),
        ("3", "20", "14"),
        ("20", "14", None),
    ]
    assert o.len() == 4

    o.delete("5")
    assert o.get_all_v2() == [(None, "3", "20"), ("3", "20", "14"), ("20", "14", None)]
    assert o.len() == 3

    o.delete("20")
    assert o.get_all_v2() == [(None, "3", "14"), ("3", "14", None)]
    assert o.len() == 2


def test_clean():
    o = OrderedStringList(asc=False)

    o.clean(asc=True)
    o.add("1")
    o.add("20")
    o.add("3")
    o.add("5")
    o.add("14")
    assert o.get_all_v2() == [
        (None, "1", "14"),
        ("1", "14", "20"),
        ("14", "20", "3"),
        ("20", "3", "5"),
        ("3", "5", None),
    ]
    assert o.get_all() == ["1", "14", "20", "3", "5"]
    assert o.len() == 5

    o.clean(asc=False)
    assert not o.get_all_v2()
    assert not o.get_all()
    assert o.len() == 0
    o.add("1")
    o.add("20")
    o.add("3")
    o.add("5")
    o.add("14")
    assert o.get_all_v2() == [
        (None, "5", "3"),
        ("5", "3", "20"),
        ("3", "20", "14"),
        ("20", "14", "1"),
        ("14", "1", None),
    ]
    assert o.get_all() == ["5", "3", "20", "14", "1"]
    assert o.len() == 5


def test_upper_case():
    o = OrderedStringList(asc=True)
    o.add("rr")
    o.add("Rr")
    o.add("zz")
    assert o.get_all() == ["Rr", "rr", "zz"]
