"""Тесты для многомерного массива"""

import pytest

from ASD_FIRST.lesson_3_dyn_array.six.multy_dyn_array import DynMultyArray, FixedCapacityList


def test_create_multy_array():
    """
    1) da0:
        * Проверка поведения при созданнии пустого массива размером 1х1
        * Проверка поведения при попытке доступа к индексам, находящимся за пределами

    2) da1:
        * Проверка поведения при доступе к пустому элементу
        * Проверка поведения при добавлении значения и сохранения значения в элементе массива

    3) da2:
        * Создаем двумерный массив и частично заполняем его
        * Проверяем корректное сохранение данных в массиве
    """
    da0 = DynMultyArray(dim_count=1, dim_size=[1])
    assert len(da0) == 1
    assert isinstance(da0.array, FixedCapacityList)

    with pytest.raises(IndexError):
        da0[1] = "789"
    with pytest.raises(IndexError):
        _ = da0[1]

    da1 = DynMultyArray(dim_count=1, dim_size=[1])
    assert da1[0] is None
    assert len(da1) == 1

    da1[0] = "123"
    assert da1[0] == "123"
    assert len(da1) == 1

    da2 = DynMultyArray(dim_count=2, dim_size=[2, 3])
    da2[0][0] = 3
    da2[0][1] = 4
    da2[1][2] = 5
    assert da2[0][0] == 3
    assert da2[0][1] == 4
    assert da2[1][2] == 5
    assert da2[1][0] is None
    assert da2[0][2] is None
    assert len(da2) == 6


def test_create_multy_array_2():
    """
    1) da0:
        * Проверка поведения при созданнии пустого массива размером 2х3
        * Проверка сохранения значений в двумерном массиве
    """
    da0 = DynMultyArray(dim_count=2, dim_size=[2, 3])
    assert len(da0) == 6
    assert da0.elements_count == 0
    assert da0.dim_count == 2
    assert da0.dim_size == [2, 3]

    da0[0][0] = 3
    da0[0][1] = 4
    da0[1][2] = 5
    assert len(da0) == 6
    assert da0[0][0] == 3
    assert da0[0][1] == 4
    assert da0[0][2] is None
    assert da0[1][2] == 5
    assert da0[1][0] is None
    assert da0[0][2] is None


def test_resize_multy_dyn_array():
    """
    1) da0:
        * Проверка поведения при создании пустого массива размером 1х1
        * Проверка добавления элемента в конец массива без реаллокации
        * Проверка добавления элемента в конец массива с реаллокацией
    2) da1:
        * Проверка поведения при создании пустого массива размером 2х3
        * Проверка сохранения значений в двумерном массиве
    """
    da0 = DynMultyArray(dim_count=1, dim_size=[1])
    assert da0.elements_count == 0
    assert len(da0) == 1

    da0.append_val("xxx")
    assert len(da0) == 1
    assert da0[0] == "xxx"
    assert da0.elements_count == 1

    da0.append_val("yyy")
    assert len(da0) == 2
    assert da0.elements_count == 2
    assert da0[0] == "xxx"
    assert da0[1] == "yyy"

    da0.append_val("zzz")
    assert len(da0) == 4
    assert da0.elements_count == 3
    assert da0[0] == "xxx"
    assert da0[1] == "yyy"
    assert da0[3] == "zzz"

    da0.append_val("aaa")
    assert len(da0) == 8
    assert da0.elements_count == 4
    assert da0[0] == "xxx"
    assert da0[1] == "yyy"
    assert da0[3] == "zzz"
    assert da0[7] == "aaa"


def test_scaling_array():
    """
    1) da0:
        * Создаем массив, размером 1х5
        * Добавляем в массив элемент
        * Масштабируем массив до 5 измерения
        * Проверяем наличие данных в ячейке
    """
    da0 = DynMultyArray(dim_count=1, dim_size=[5])
    assert da0.dim_count == 1
    assert len(da0) == 5
    assert da0.elements_count == 0

    da0.append_val("zzz")
    da0.increment_dimension()
    assert da0.dim_count == 2
    assert len(da0) == 10
    assert da0.elements_count == 1
    assert da0[0][4] == "zzz"

    da0.increment_dimension()
    assert da0.dim_count == 3
    assert len(da0) == 20
    assert da0.elements_count == 1
    assert da0[0][0][4] == "zzz"

    da0.increment_dimension()
    assert da0.dim_count == 4
    assert len(da0) == 40
    assert da0.elements_count == 1
    assert da0[0][0][0][4] == "zzz"

    da0.increment_dimension()
    assert da0.dim_count == 5
    assert len(da0) == 80
    assert da0.elements_count == 1
    assert da0[0][0][0][0][4] == "zzz"
    assert da0[0][0][0][0][1] is None


def test_find_el_by_absolute_index():
    """
    1) da1:
        * Создаем одномерный массив.
        * Проверяем работу поиска координат элемента

    2) da2:
        * Создаем двухмерный массив
        * Проверяем работу поиска координат элемента

    3) da3:
        * Создаем трехмерный массив
        * Проверяем работу поиска координат элемента
    """
    da1 = DynMultyArray(dim_count=1, dim_size=[4])
    assert da1.get_coordinate_by_element_index(2) == [2]
    with pytest.raises(IndexError):
        _ = da1.get_coordinate_by_element_index(4)
    with pytest.raises(IndexError):
        _ = da1.get_coordinate_by_element_index(5)

    da2 = DynMultyArray(dim_count=2, dim_size=[2, 4])
    assert da2.get_coordinate_by_element_index(0) == [0, 0]
    assert da2.get_coordinate_by_element_index(1) == [0, 1]
    assert da2.get_coordinate_by_element_index(2) == [0, 2]
    assert da2.get_coordinate_by_element_index(3) == [0, 3]
    assert da2.get_coordinate_by_element_index(4) == [1, 0]
    assert da2.get_coordinate_by_element_index(7) == [1, 3]
    with pytest.raises(IndexError):
        _ = da2.get_coordinate_by_element_index(8)

    da3 = DynMultyArray(dim_count=3, dim_size=[2, 4, 3])
    assert da3.get_coordinate_by_element_index(0) == [0, 0, 0]
    assert da3.get_coordinate_by_element_index(1) == [0, 0, 1]
    assert da3.get_coordinate_by_element_index(2) == [0, 0, 2]
    assert da3.get_coordinate_by_element_index(3) == [0, 1, 0]
    assert da3.get_coordinate_by_element_index(4) == [0, 1, 1]
    assert da3.get_coordinate_by_element_index(5) == [0, 1, 2]
    assert da3.get_coordinate_by_element_index(6) == [0, 2, 0]
    assert da3.get_coordinate_by_element_index(7) == [0, 2, 1]
    assert da3.get_coordinate_by_element_index(8) == [0, 2, 2]
    assert da3.get_coordinate_by_element_index(9) == [0, 3, 0]
    assert da3.get_coordinate_by_element_index(10) == [0, 3, 1]
    assert da3.get_coordinate_by_element_index(11) == [0, 3, 2]
    assert da3.get_coordinate_by_element_index(12) == [1, 0, 0]
    assert da3.get_coordinate_by_element_index(13) == [1, 0, 1]
    assert da3.get_coordinate_by_element_index(14) == [1, 0, 2]
    assert da3.get_coordinate_by_element_index(15) == [1, 1, 0]
    assert da3.get_coordinate_by_element_index(17) == [1, 1, 2]
    assert da3.get_coordinate_by_element_index(18) == [1, 2, 0]
    assert da3.get_coordinate_by_element_index(20) == [1, 2, 2]
    assert da3.get_coordinate_by_element_index(21) == [1, 3, 0]
    assert da3.get_coordinate_by_element_index(23) == [1, 3, 2]
    with pytest.raises(IndexError):
        _ = da3.get_coordinate_by_element_index(24)
    with pytest.raises(IndexError):
        _ = da3.get_coordinate_by_element_index(-1)

    da4 = DynMultyArray(dim_count=4, dim_size=[2, 4, 3, 5])
    assert da4.get_coordinate_by_element_index(0) == [0, 0, 0, 0]
    assert da4.get_coordinate_by_element_index(1) == [0, 0, 0, 1]
    assert da4.get_coordinate_by_element_index(18) == [0, 1, 0, 3]
    assert da4.get_coordinate_by_element_index(89) == [1, 1, 2, 4]
    assert da4.get_coordinate_by_element_index(90) == [1, 2, 0, 0]
    assert da4.get_coordinate_by_element_index(92) == [1, 2, 0, 2]
    assert da4.get_coordinate_by_element_index(94) == [1, 2, 0, 4]
    assert da4.get_coordinate_by_element_index(95) == [1, 2, 1, 0]
    assert da4.get_coordinate_by_element_index(114) == [1, 3, 1, 4]
    assert da4.get_coordinate_by_element_index(119) == [1, 3, 2, 4]


def test_get_link_to_last_array():
    """
    1) da1:
        * Проверка получения последнего массива нижнего уровня для одномерного массива
    2) da2:
        * Проверка получения последнего массива нижнего уровня для двухмерного массива
    3) da4:
        * Проверка получения последнего массива нижнего уровня для четырехмерного массива

    :return:
    """
    da1 = DynMultyArray(dim_count=1, dim_size=[5])
    da1[4] = 77
    test_arr = da1.get_link_to_last_array()
    assert test_arr[4] == 77

    da2 = DynMultyArray(dim_count=2, dim_size=[2, 4])
    da2[1][3] = 77
    test_arr = da2.get_link_to_last_array()
    assert test_arr[3] == 77

    da4 = DynMultyArray(dim_count=4, dim_size=[2, 4, 3, 5])
    da4[1][3][2][4] = 77
    test_arr = da4.get_link_to_last_array()
    assert test_arr[4] == 77


def test_array_relocation():
    """
    1) da0:
        * Создаем одномерный массив
        * Вставляем ему в несколько элементов, проверяя корректность реаллокации одномерного массива
        * Масштабируем массив до двумерного
        * Вставляем ему в несколько элементов, проверяя корректность реаллокации двумерного массива
        * Масштабируем массив до трехмерного
        * Вставляем ему в несколько элементов, проверяя корректность реаллокации трехмерного массива
    """
    da0 = DynMultyArray(dim_count=1, dim_size=[4])
    da0[2] = 55
    da0[0] = (77,)
    da0[3] = True
    da0.append_val("xxx")

    assert da0[0] == (77,)
    assert da0[1] is None
    assert da0[2] == 55
    assert da0[3] is True
    assert da0[7] == "xxx"
    assert len(da0) == 8
    assert da0.elements_count == 4

    da0.increment_dimension()
    da0[0][6] = "xxxx"
    da0[1][0] = "aaaa"
    da0[1][2] = "zzzz"
    da0[1][7] = (88, 33)
    assert da0[0][0] == (77,)
    assert da0[0][1] is None
    assert da0[0][2] == 55
    assert da0[0][3] is True
    assert da0[0][6] == "xxxx"
    assert da0[0][7] == "xxx"
    assert da0[1][0] == "aaaa"
    assert da0[1][2] == "zzzz"
    assert da0[1][7] == (88, 33)
    assert len(da0) == 16
    assert da0.elements_count == 8

    da0.increment_dimension()
    da0.append_val(777)
    assert da0[0][0][0] == (77,)
    assert da0[0][0][1] is None
    assert da0[0][0][2] == 55
    assert da0[0][0][3] is True
    assert da0[0][0][6] == "xxxx"
    assert da0[0][0][7] == "xxx"
    assert da0[0][1][0] == "aaaa"
    assert da0[0][1][2] == "zzzz"
    assert da0[0][1][7] == (88, 33)
    assert da0.elements_count == 9

    da0.append_val(888)
    assert da0[0][0][0] == (77,)
    assert da0[0][0][1] is None
    assert da0[0][0][2] == 55
    assert da0[0][0][3] is True
    assert da0[0][0][6] == "xxxx"
    assert da0[0][0][7] == "xxx"
    assert da0[0][0][8] == "aaaa"
    assert da0[0][1][1] == "zzzz"
    assert da0[0][1][6] == (88, 33)
    assert len(da0) == 81
    assert da0.elements_count == 10
