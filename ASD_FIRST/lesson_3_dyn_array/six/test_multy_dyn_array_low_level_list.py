"""Тесты на структуру, хранящую конечные элементы многомерного массива"""

import pytest

from ASD_FIRST.lesson_3_dyn_array.six.multy_dyn_array import DynMultyArray, FixedCapacityList


def test_value_keep_list_has_element_by_index_method():
    va = FixedCapacityList(capacity=5, parent=DynMultyArray(dim_count=1, dim_size=[1]))

    va[1] = "44"

    assert va[1] == "44"
    assert va.has_element_by_index(0) == 0
    assert va.has_element_by_index(1) == 1
    assert va.has_element_by_index(-1) == -1
    assert va.has_element_by_index(4) == 0
    assert va.has_element_by_index(5) == -1
    assert va[1] == "44"
    assert va[0] is None
    assert va[4] is None

    with pytest.raises(IndexError):
        _ = va[5]


def test_list_value_keep():
    list_with_data = FixedCapacityList(
        capacity=3, parent=DynMultyArray(dim_count=1, dim_size=[1])
    )
    assert len(list_with_data) == 0

    list_with_data[0] = 5
    list_with_data[2] = 9

    assert len(list_with_data) == 2

    with pytest.raises(IndexError):
        list_with_data[3] = 12
    assert list_with_data.count_elements == 2

    assert list_with_data[0] == 5
    assert list_with_data[2] == 9
    assert list_with_data[1] is None
