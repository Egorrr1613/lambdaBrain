from ASD_FIRST.seven_lesson_sort_list.ordered_list_2 import OrderedList, join_two_sorted_lists, OrderedListByDynArray


def test_del_duplicate():
    o = OrderedList(asc=True)
    o.add(1)
    o.add(1)
    o.add(3)
    o.add(5)
    o.add(5)
    o.add(14)
    o.add(20)
    o.add(20)

    o.delete_duplicate()
    assert o.get_all_v2() == [(None, 1, 3), (1, 3, 5), (3, 5, 14), (5, 14, 20), (14, 20, None)]


def test_del_duplicate_non_duplicate():
    o = OrderedList(asc=True)
    o.add(1)
    o.add(3)
    o.add(5)
    o.add(14)
    o.add(20)

    o.delete_duplicate()
    assert o.get_all_v2() == [(None, 1, 3), (1, 3, 5), (3, 5, 14), (5, 14, 20), (14, 20, None)]


def test_del_duplicate_two_el():
    o = OrderedList(asc=True)
    o.add(1)
    o.add(1)

    o.delete_duplicate()
    assert o.get_all_v2() == [(None, 1, None)]


def test_del_duplicate_zero_el():
    o = OrderedList(asc=True)

    o.delete_duplicate()
    assert o.get_all_v2() == []


def test_join_list():
    o_1 = OrderedList(asc=True)
    o_1.add(1)
    o_1.add(3)
    o_1.add(5)
    o_1.add(14)
    o_1.add(20)

    o_2 = OrderedList(asc=True)
    o_2.add(2)
    o_2.add(4)
    o_2.add(6)
    o_2.add(15)
    o_2.add(21)

    assert join_two_sorted_lists(first_list=o_1, second_list=o_2,
                                 asc=True).get_all_v2() == [(None, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6),
                                                            (5, 6, 14), (6, 14, 15), (14, 15, 20), (15, 20, 21),
                                                            (20, 21, None)]


def test_has_sublist():
    o = OrderedList(asc=True)

    o.add(1)
    o.add(3)
    o.add(5)
    o.add(14)
    o.add(20)

    o_sub = OrderedList(asc=True)
    o_sub.add(3)
    assert o.has_sub_list(o_sub)

    o_sub.add(5)
    assert o.has_sub_list(o_sub)

    o_sub.add(6)
    assert not o.has_sub_list(o_sub)


def test_has_sublist_1():
    o = OrderedList(asc=True)

    o_sub = OrderedList(asc=True)
    assert o.has_sub_list(o_sub)

    o_sub.add(3)
    assert not o.has_sub_list(o_sub)

    o.add(3)
    assert o.has_sub_list(o_sub)


def test_has_sublist_2():
    o = OrderedList(asc=True)
    o.add(3)
    o.add(4)
    o.add(5)
    o.add(6)
    o.add(8)

    o_sub = OrderedList(asc=True)
    o_sub.add(4)
    o_sub.add(5)
    o_sub.add(6)
    o_sub.add(8)
    assert o.has_sub_list(o_sub)

    o_sub.add(8)
    assert not o.has_sub_list(o_sub)

    o_sub = OrderedList(asc=True)
    o_sub.add(3)
    o_sub.add(4)
    o_sub.add(5)
    o_sub.add(6)
    o_sub.add(8)
    assert o.has_sub_list(o_sub)

    o_sub.add(8)
    assert not o.has_sub_list(o_sub)


def test_has_sublist_3():
    o = OrderedList(asc=True)
    o.add(1)
    o.add(1)
    o.add(1)
    o.add(1)
    o.add(2)
    o.add(2)
    o.add(2)
    o.add(2)
    o.add(3)
    o.add(3)
    o.add(3)
    o.add(4)

    o_sub = OrderedList(asc=True)

    o_sub.add(1)
    assert o.has_sub_list(o_sub)

    o_sub.add(2)
    assert o.has_sub_list(o_sub)

    o_sub.add(3)
    assert not o.has_sub_list(o_sub)

    o_sub_2 = OrderedList(asc=True)
    o_sub_2.add(3)
    assert o.has_sub_list(o_sub_2)
    o_sub_2.add(4)
    assert o.has_sub_list(o_sub_2)
    o_sub_2.add(5)
    assert not o.has_sub_list(o_sub_2)


def test_has_sublist_4():
    o = OrderedList(asc=True)

    o.add(1)
    o.add(3)
    o.add(5)
    o.add(14)
    o.add(20)

    o_sub = OrderedList(asc=True)
    o_sub.add(14)
    assert o.has_sub_list(o_sub)

    o_sub.add(20)
    assert o.has_sub_list(o_sub)

    o_sub.add(21)
    assert not o.has_sub_list(o_sub)

    o_sub_2 = OrderedList(asc=True)
    o_sub_2.add(20)
    assert o.has_sub_list(o_sub_2)
    o_sub_2.add(21)
    assert not o.has_sub_list(o_sub_2)


def test_get_frequent_element_1():
    o = OrderedList(asc=True)
    o.add(3)
    o.add(4)
    o.add(5)
    o.add(6)
    o.add(8)

    assert o.get_frequent_element() == 3

    o.add(6)
    assert o.get_frequent_element() == 6

    o.add(5)
    o.add(5)
    assert o.get_frequent_element() == 5


def test_get_frequent_element_2():
    o = OrderedList(asc=True)
    assert o.get_frequent_element() is None

    o.add(8)
    assert o.get_frequent_element() == 8

    o.add(9)
    assert o.get_frequent_element() == 8

    o.add(8)
    assert o.get_frequent_element() == 8

    o.add(9)
    o.add(9)
    assert o.get_frequent_element() == 9


def test_order_list_by_dyn_arr():
    o = OrderedListByDynArray(asc=True)
    assert o.get_all() == []

    o.add(3)
    assert o.get_all() == [3]

    o.add(1)
    assert o.get_all() == [1, 3]

    o.add(2)
    assert o.get_all() == [1, 2, 3]


def test_order_list_by_dyn_arr_reverse():
    o_reverse = OrderedListByDynArray(asc=False)
    assert o_reverse.get_all() == []

    o_reverse.add(3)
    assert o_reverse.get_all() == [3]

    o_reverse.add(1)
    assert o_reverse.get_all() == [3, 1]

    o_reverse.add(2)
    assert o_reverse.get_all() == [3, 2, 1]


def test_find_in_order_list_by_dyn_arr():
    o = OrderedListByDynArray(asc=True)

    o.add(3)
    assert o.find(3) == 0
    assert o.find(33) is None

    o.add(1)
    assert o.find(1) == 0
    assert o.find(3) == 1

    o.add(2)
    assert o.find(1) == 0
    assert o.find(2) == 1
    assert o.find(3) == 2
    assert o.find(55) is None
