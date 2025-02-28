"""
Модуль с тестами на динамический массив с банковским методом.
Вариант релокации: 'Когда достигается граница накопленных монет'

ЧАСТЬ ТЕСТОВ НЕ РАБОТАЕТ! - решил сделать альтернативную реализацию
"""
import pytest

from ASD_FIRST.three_lesson.five.bank_dyn_array import DynArray


def prepare_test_data(len_array: int) -> DynArray:
    da = DynArray()
    for i in range(len_array):
        da.append(i)
    return da


def test_insert():
    da = prepare_test_data(len_array=8)
    da.insert(i=4, itm=99)

    assert len(da) == 9
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 1, 2, 3, 99, 4, 5, 6, 7]


def test_insert_resize():
    da = prepare_test_data(len_array=15)
    da.insert(i=4, itm=15)
    da.insert(i=4, itm=16)
    da.insert(i=4, itm=17)
    da.insert(i=4, itm=18)
    da.insert(i=4, itm=19)

    assert len(da) == 20
    assert da.capacity == 32
    assert da.get_list_elements() == [
        0,
        1,
        2,
        3,
        19,
        18,
        17,
        16,
        15,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]


def test_insert_incorrect_index():
    da = prepare_test_data(len_array=2)
    with pytest.raises(IndexError):
        da.insert(i=-1, itm=99)

    with pytest.raises(IndexError):
        da.insert(i=3, itm=99)

    assert len(da) == 2
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 1]


def test_insert_bound_index():
    da = prepare_test_data(len_array=2)
    da.insert(i=0, itm=99)
    da.insert(i=2, itm=98)

    assert len(da) == 4
    assert da.capacity == 16
    assert da.get_list_elements() == [99, 0, 98, 1]


def test_insert_to_empty_list():
    da = DynArray()

    da.insert(i=0, itm=99)
    assert len(da) == 1
    assert da.capacity == 16
    assert da.get_list_elements() == [99]

    da.insert(i=1, itm=98)
    assert len(da) == 2
    assert da.capacity == 16
    assert da.get_list_elements() == [99, 98]


def test_insert_if_i_eq_count():
    da = prepare_test_data(len_array=8)
    da.insert(i=8, itm=88)

    assert len(da) == 9
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 1, 2, 3, 4, 5, 6, 7, 88]


def test_delete():
    da = prepare_test_data(3)
    da.delete(1)
    # da.array[0] = None
    # da.array[1] = None
    # x = da.array
    # print(x)
    # array = (ctypes.py_object * 5)()

    # # Заполнение массива различными объектами
    # array[0] = 42  # Число
    # array[0] = None  # Число
    # array[1] = "Hello"  # Строка
    # array[2] = [1, 2, 3]  # Список
    # array[3] = {"key": "value"}  # Словарь
    # array[4] = None  # None
    #
    # array[3] = None  # Словарь

    # for i in range(5):
    #     print(array[i])
    assert len(da) == 2
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 2]


def test_delete_empty_array():
    da = DynArray()
    with pytest.raises(IndexError):
        da.delete(0)

    assert len(da) == 0
    assert da.capacity == 16
    assert da.array._objects is None


def test_delete_incorrect_index():
    da = prepare_test_data(9)
    with pytest.raises(IndexError):
        da.delete(14)

    assert len(da) == 9
    assert da.capacity == 16


def test_delete_resize():
    da = prepare_test_data(len_array=17)
    assert len(da) == 17
    assert da.capacity == 32

    da.delete(8)
    assert len(da) == 16
    assert da.capacity == 32

    da.delete(8)
    assert len(da) == 15
    assert da.capacity == 21

    for _ in range(4):
        da.delete(1)
    assert len(da) == 11
    assert da.capacity == 21

    da.delete(1)
    assert len(da) == 10
    assert da.capacity == 21

    da.delete(1)
    assert len(da) == 9
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 7, 10, 11, 12, 13, 14, 15, 16]


def test_insert_2():
    da = prepare_test_data(len_array=8)
    da.insert(i=4, itm=99)
    da.insert(i=4, itm=99)

    assert len(da) == 10
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 1, 2, 3, 99, 99, 4, 5, 6, 7]


def test_bank_array_state_add_and_del():
    da = DynArray()

    da.append(itm=0)
    assert len(da) == 1
    assert da.coin_count_in_bank == 2
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    da.delete(i=0)
    assert len(da) == 0
    assert da.coin_count_in_bank == 3
    assert da.capacity == 16
    assert da.price_to_next_resize == 32


def test_bank_array_state():
    da = DynArray()
    assert len(da) == 0
    assert da.coin_count_in_bank == 0
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    da.append(itm=0)
    da.append(itm=1)
    da.append(itm=2)
    da.append(itm=3)
    da.append(itm=4)
    assert len(da) == 5
    assert da.coin_count_in_bank == 15
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    da.delete(4)
    assert len(da) == 4
    assert da.coin_count_in_bank == 13
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    da.append(88)
    assert len(da) == 5
    assert da.coin_count_in_bank == 16
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    for i in range(5):
        da.append(str(i))

    assert len(da) == 10
    assert da.coin_count_in_bank == 30
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    da.insert(8, "abdc")
    assert len(da) == 11
    assert da.coin_count_in_bank == 33
    assert da.capacity == 32
    assert da.price_to_next_resize == 64

    da.delete(i=0)
    assert len(da) == 10
    assert da.coin_count_in_bank == 30
    assert da.capacity == 21
    assert da.price_to_next_resize == 32


def test_del_to_empty():
    da = prepare_test_data(3)
    da.delete(0)
    da.delete(0)
    da.delete(0)

    assert len(da) == 0
    assert da.coin_count_in_bank == 3


"""new test:"""
def test_init_state_and_after_append_state():
    da = DynArray()

    "Состояние массива после инициализации"
    assert len(da) == 0
    assert da.coin_count_in_bank == 0
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    "Состояние массива после добавления первого элемента в хвост"
    da.append(99)
    assert len(da) == 1
    assert da.coin_count_in_bank == 2
    assert da.capacity == 16
    assert da.price_to_next_resize == 32


def test_append_with_resize_state():
    da = DynArray()

    for _ in range(15):
        da.append("xxx")

    assert len(da) == 15
    assert da.coin_count_in_bank == 30
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    da.append("yyy")
    assert len(da) == 16
    assert da.coin_count_in_bank == 32
    assert da.capacity == 16
    assert da.price_to_next_resize == 32

    da.append("zzz")
    assert len(da) == 17
    assert da.coin_count_in_bank == 18
    assert da.capacity == 32
    assert da.price_to_next_resize == 64

    for _ in range(14):
        da.append("nnn")

    da.append('xyz')