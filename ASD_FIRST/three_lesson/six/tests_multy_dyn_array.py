"""Тесты для многомерного массива"""

import pytest

from ASD_FIRST.three_lesson.six.multy_dyn_array import DynMultyArray, ValueKeepListClass


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
    assert isinstance(da0.array, ValueKeepListClass)

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
        * Проверка поведения при созданнии пустого массива размером 2х3
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
    assert len(da0) == 4
    assert da0.elements_count == 2
    assert da0[1] == "yyy"


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
    assert da0[0][0] == "zzz"

    da0.increment_dimension()
    assert da0.dim_count == 3
    assert len(da0) == 20
    assert da0.elements_count == 1
    assert da0[0][0][0] == "zzz"

    da0.increment_dimension()
    assert da0.dim_count == 4
    assert len(da0) == 40
    assert da0.elements_count == 1
    assert da0[0][0][0][0] == "zzz"

    da0.increment_dimension()
    assert da0.dim_count == 5
    assert len(da0) == 80
    assert da0.elements_count == 1
    assert da0[0][0][0][0][0] == "zzz"
    assert da0[0][0][0][0][1] is None


def test_find_el_by_absolute_index():
    """
    1) da1:
        * Создаем одномерный массив
        * Проверяем работу поиска координат элемента

    2) da2:
        * Создаем двухмерный массив
        * Проверяем работу поиска координат элемента

    3) da3:
        * Создаем трехмерный массив
        * Проверяем работу поиска координат элемента
    """
    da1 = DynMultyArray(dim_count=1, dim_size=[4])
    assert da1.get_coordinate_arr_by_element_index(2) == [2]
    with pytest.raises(IndexError):
        _ = da1.get_coordinate_arr_by_element_index(4)
    with pytest.raises(IndexError):
        _ = da1.get_coordinate_arr_by_element_index(5)

    da2 = DynMultyArray(dim_count=2, dim_size=[2, 4])
    assert da2.get_coordinate_arr_by_element_index(0) == [0]
    assert da2.get_coordinate_arr_by_element_index(1) == [0]
    assert da2.get_coordinate_arr_by_element_index(2) == [0]
    assert da2.get_coordinate_arr_by_element_index(3) == [0]
    assert da2.get_coordinate_arr_by_element_index(4) == [1]
    assert da2.get_coordinate_arr_by_element_index(7) == [1]
    with pytest.raises(IndexError):
        _ = da2.get_coordinate_arr_by_element_index(8)

    da3 = DynMultyArray(dim_count=3, dim_size=[2, 4, 3])
    assert da3.get_coordinate_arr_by_element_index(0) == [0, 0]
    assert da3.get_coordinate_arr_by_element_index(1) == [0, 0]
    assert da3.get_coordinate_arr_by_element_index(2) == [0, 0]
    assert da3.get_coordinate_arr_by_element_index(3) == [0, 1]
    assert da3.get_coordinate_arr_by_element_index(4) == [0, 1]
    assert da3.get_coordinate_arr_by_element_index(5) == [0, 1]
    assert da3.get_coordinate_arr_by_element_index(6) == [0, 2]
    assert da3.get_coordinate_arr_by_element_index(8) == [0, 2]
    assert da3.get_coordinate_arr_by_element_index(9) == [0, 3]
    assert da3.get_coordinate_arr_by_element_index(10) == [0, 3]
    assert da3.get_coordinate_arr_by_element_index(11) == [0, 3]
    assert da3.get_coordinate_arr_by_element_index(12) == [1, 0]
    assert da3.get_coordinate_arr_by_element_index(13) == [1, 0]
    assert da3.get_coordinate_arr_by_element_index(14) == [1, 0]
    assert da3.get_coordinate_arr_by_element_index(15) == [1, 1]
    assert da3.get_coordinate_arr_by_element_index(17) == [1, 1]
    assert da3.get_coordinate_arr_by_element_index(18) == [1, 2]
    assert da3.get_coordinate_arr_by_element_index(20) == [1, 2]
    assert da3.get_coordinate_arr_by_element_index(21) == [1, 3]
    assert da3.get_coordinate_arr_by_element_index(23) == [1, 3]
    with pytest.raises(IndexError):
        _ = da3.get_coordinate_arr_by_element_index(24)
    with pytest.raises(IndexError):
        _ = da3.get_coordinate_arr_by_element_index(-1)

    da4 = DynMultyArray(dim_count=4, dim_size=[2, 4, 3, 5])
    assert da4.get_coordinate_arr_by_element_index(1) == [0, 0, 0]
    assert da4.get_coordinate_arr_by_element_index(0) == [0, 0, 0]
    assert da4.get_coordinate_arr_by_element_index(18) == [0, 1, 0]
    assert da4.get_coordinate_arr_by_element_index(89) == [1, 1, 2]
    assert da4.get_coordinate_arr_by_element_index(90) == [1, 2, 0]
    assert da4.get_coordinate_arr_by_element_index(94) == [1, 2, 0]
    assert da4.get_coordinate_arr_by_element_index(95) == [1, 2, 1]
    assert da4.get_coordinate_arr_by_element_index(114) == [1, 3, 1]
    assert da4.get_coordinate_arr_by_element_index(119) == [1, 3, 2]


def test_array_relocation():
    """
    1) da0:
        * Создаем одномерный массив
        * Вставляем ему в несколько элементов, проверяя корректность реолокации одномерного массива
        * Масштабируем массив до двумерного
        * Вставляем ему в несколько элементов, проверяя корректность реолокации двумерного массива
        * Масштабируем массив до трехмерного
        * Вставляем ему в несколько элементов, проверяя корректность реолокации трехмерного массива
    """
    da0 = DynMultyArray(dim_count=1, dim_size=[4])
    pass


























# def test_last_element_coordinate():
# Решил отказаться от переменной "последнего заполненного индекса"

#     """
#     1) da0:
#         * Создаем одномерный массив
#         * Проверяем координату крайнего элемента
#         * Добавляем элемент, не превышая доступный размер массива
#         * Проверяем координату крайнего элемента
#         * Добавляем элементы, превышая доступный размер массива для вызова релокации
#         * Проверяем координату крайнего элемента
#
#         * Увеличиваем размерность массива до двухмерного
#         * Проверяем координату крайнего элемента
#         * Добавляем элемент, не превышая доступный размер массива
#         * Проверяем координату крайнего элемента
#         * Добавляем элементы, превышая доступный размер массива для вызова релокации
#
#     """
#     da0 = DynMultyArray(dim_count=1, dim_size=[3])
#     assert da0.last_element_coordinate == [0]
#
#     da0.append_val('000')
#     assert da0.last_element_coordinate == [1]
#
#     da0.append_val('000')
#     assert da0.last_element_coordinate == [1]
#
#     da0.append_val('000')
#     assert da0.last_element_coordinate == [2]
#
#     da0.append_val('000')
#     assert da0.last_element_coordinate == [3]