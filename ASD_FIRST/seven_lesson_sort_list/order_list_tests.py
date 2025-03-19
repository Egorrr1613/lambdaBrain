from ASD_FIRST.seven_lesson_sort_list.ordered_list import OrderedList


def test_order_list_empty():
    o = OrderedList(asc=True)
    assert o.get_all() == []
    assert o.len() == 0


def test_order_list_add_one_el():
    o = OrderedList(asc=True)
    o.add(1)
    assert o.get_all_v2() == [(None, 1, None)]
    assert o.len() == 1


def test_order_list_add_in_head_0():
    o = OrderedList(asc=True)
    o.add(10)
    o.add(1)
    assert o.get_all_v2() == [(None, 1, 10), (1, 10, None)]
    assert o.len() == 2

    o = OrderedList(asc=False)
    o.add(10)
    o.add(1)
    assert o.get_all_v2() == [(None, 10, 1), (10, 1, None)]
    assert o.len() == 2


def test_order_list_add_in_head_1():
    o = OrderedList(asc=True)
    o.add(5)
    o.add(10)
    o.add(1)
    assert o.get_all_v2() == [(None, 1, 5), (1, 5, 10), (5, 10, None)]
    assert o.len() == 3

    o = OrderedList(asc=False)
    o.add(5)
    o.add(10)
    o.add(1)
    assert o.get_all_v2() == [(None, 10, 5), (10, 5, 1), (5, 1, None)]
    assert o.len() == 3


def test_order_list_add_in_tail_0():
    o = OrderedList(asc=True)
    o.add(10)
    o.add(11)
    assert o.get_all_v2() == [(None, 10, 11), (10, 11, None)]
    assert o.len() == 2

    o = OrderedList(asc=False)
    o.add(10)
    o.add(11)
    assert o.get_all_v2() == [(None, 11, 10), (11, 10, None)]
    assert o.len() == 2


def test_order_list_add_in_tail_1():
    o = OrderedList(asc=True)
    o.add(5)
    o.add(10)
    o.add(11)
    assert o.get_all_v2() == [(None, 5, 10), (5, 10, 11), (10, 11, None)]
    assert o.len() == 3

    o = OrderedList(asc=False)
    o.add(5)
    o.add(10)
    o.add(11)
    assert o.get_all_v2() == [(None, 11, 10), (11, 10, 5), (10, 5, None)]
    assert o.len() == 3


def test_order_list_add_1():
    o = OrderedList(asc=True)
    o.add(1)
    o.add(2)
    o.add(3)

    assert o.get_all_v2() == [(None, 1, 2), (1, 2, 3), (2, 3, None)]
    assert o.len() == 3

    o = OrderedList(asc=False)
    o.add(1)
    o.add(2)
    o.add(3)

    assert o.get_all_v2() == [(None, 3, 2), (3, 2, 1), (2, 1, None)]
    assert o.len() == 3

    o = OrderedList(asc=True)
    o.add(3)
    o.add(2)
    o.add(1)

    assert o.get_all_v2() == [(None, 1, 2), (1, 2, 3), (2, 3, None)]
    assert o.len() == 3

    o = OrderedList(asc=False)
    o.add(3)
    o.add(2)
    o.add(1)

    assert o.get_all_v2() == [(None, 3, 2), (3, 2, 1), (2, 1, None)]
    assert o.len() == 3


def test_order_add_elements_in_mid():
    o = OrderedList(asc=True)
    o.add(1)
    o.add(20)
    assert o.get_all_v2() == [(None, 1, 20), (1, 20, None)]

    o.add(3)
    assert o.get_all_v2() == [(None, 1, 3), (1, 3, 20), (3, 20, None)]
    assert o.len() == 3

    o.add(5)
    o.add(14)
    assert o.get_all_v2() == [
        (None, 1, 3),
        (1, 3, 5),
        (3, 5, 14),
        (5, 14, 20),
        (14, 20, None),
    ]
    assert o.len() == 5


def test_order_add_elements_in_mid_reverse_asc():
    o = OrderedList(asc=False)
    o.add(1)
    o.add(20)
    assert o.get_all_v2() == [(None, 20, 1), (20, 1, None)]

    o.add(3)
    assert o.get_all_v2() == [(None, 20, 3), (20, 3, 1), (3, 1, None)]
    assert o.len() == 3

    o.add(5)
    o.add(14)
    assert o.get_all_v2() == [
        (None, 20, 14),
        (20, 14, 5),
        (14, 5, 3),
        (5, 3, 1),
        (3, 1, None),
    ]
    assert o.len() == 5


def test_del_0_elements():
    o = OrderedList(asc=True)
    o.delete(55)
    assert not o.get_all()
    assert o.len() == 0

    o.add(33)
    assert o.get_all()[0].value == 33

    o.delete(23)
    assert o.get_all()[0].value == 33

    o.delete(33)
    assert not o.get_all()
    assert o.len() == 0


def test_del_1():
    o = OrderedList(asc=True)
    o.add(1)
    o.add(20)
    o.add(3)
    o.add(5)
    o.add(14)
    assert o.get_all_v2() == [
        (None, 1, 3),
        (1, 3, 5),
        (3, 5, 14),
        (5, 14, 20),
        (14, 20, None),
    ]
    assert o.len() == 5

    o.delete(1)
    assert o.get_all_v2() == [(None, 3, 5), (3, 5, 14), (5, 14, 20), (14, 20, None)]
    assert o.len() == 4

    o.delete(20)
    assert o.get_all_v2() == [
        (None, 3, 5),
        (3, 5, 14),
        (5, 14, None),
    ]
    assert o.len() == 3

    o.delete(5)
    assert o.get_all_v2() == [(None, 3, 14), (3, 14, None)]
    assert o.len() == 2


def test_del_1_asc_false():
    o = OrderedList(asc=False)
    o.add(1)
    o.add(20)
    o.add(3)
    o.add(5)
    o.add(14)
    assert o.get_all_v2() == [
        (None, 20, 14),
        (20, 14, 5),
        (14, 5, 3),
        (5, 3, 1),
        (3, 1, None),
    ]
    assert o.len() == 5

    o.delete(1)
    assert o.get_all_v2() == [(None, 20, 14), (20, 14, 5), (14, 5, 3), (5, 3, None)]
    assert o.len() == 4

    o.delete(20)
    assert o.get_all_v2() == [(None, 14, 5), (14, 5, 3), (5, 3, None)]
    assert o.len() == 3

    o.delete(5)
    assert o.get_all_v2() == [(None, 14, 3), (14, 3, None)]
    assert o.len() == 2


def test_clean():
    o = OrderedList(asc=False)

    o.clean(asc=True)
    o.add(1)
    o.add(20)
    o.add(3)
    o.add(5)
    o.add(14)
    assert o.get_all_v2() == [
        (None, 1, 3),
        (1, 3, 5),
        (3, 5, 14),
        (5, 14, 20),
        (14, 20, None),
    ]
    assert [i.value for i in o.get_all()] == [1, 3, 5, 14, 20]
    assert o.len() == 5

    o.clean(asc=False)
    assert not o.get_all_v2()
    assert not o.get_all()
    assert o.len() == 0
    o.add(1)
    o.add(20)
    o.add(3)
    o.add(5)
    o.add(14)
    assert o.get_all_v2() == [
        (None, 20, 14),
        (20, 14, 5),
        (14, 5, 3),
        (5, 3, 1),
        (3, 1, None),
    ]
    assert [i.value for i in o.get_all()] == [20, 14, 5, 3, 1]
    assert o.len() == 5
