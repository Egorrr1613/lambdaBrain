import ctypes
import operator
from functools import reduce


class ValueKeepListClass:
    """
    Класс для хранения конечных данных динамического многомерного массива
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count_elements = 0
        self.array = (capacity * ctypes.py_object)()
        self.last_insert_index = 0

    def __getitem__(self, i):
        response_code = self.has_element_by_index(index=i)
        if response_code == -1:
            raise IndexError("Index is out of bounds")
        if response_code == 0:
            return None
        if response_code == 1:
            return self.array[i]

        raise ValueError(f"Response code {response_code} was not processed")

    def __len__(self):
        return self.count_elements

    def __setitem__(self, key, value) -> None:
        response_code = self.has_element_by_index(key)
        if response_code == -1:
            raise IndexError("Index is out of bounds")

        if response_code == 1:
            self.array[key] = value
            return

        if response_code == 0:
            self.array[key] = value
            self.count_elements += 1
            return

        raise ValueError(f"Response code {response_code} was not processed")

    def has_element_by_index(self, index: int):
        """
        Метод для проверки доступа к ячейке массива

        :param index: Проверяемый индекс
        :return: Код ответа.
            1 - Ячейка памяти хранит какое то значение
            0 - Пустая ячейка памяти
            -1 - Выход за пределы массива
        """
        if index < 0 or index >= self.capacity:
            return -1

        try:
            self.array[index]
        except ValueError:
            return 0
        return 1


#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################


class DynMultyArray:
    """
    Класс, реализующий многомерный динамический массив

    Стурктура выглядит так:

    1) Класс обертка DynMultyArray
        а) реализуюет логику реалокации многомерного массива
        б) хранит массив ссылок (list)
        в) реализует логику увеличения размерности (измерения) массива
        г) позволяет получить элемент по "абсолютному" индексу - тоесть без обращения к внутренней структуре

    2) Массив ссылок (self.array) хранит либо:
        а) ссылки на массивы ссылок - т.е. реализует измерения
        б) ссылки на объект ValueKeepListClass - конечные хранимые занчения

    Количество "уровней" вложенности определяет размерность массива
    """

    def __init__(self, dim_count: int, dim_size: list[int]):
        """

        :param dim_count: Количество измерений всего многомерного массива
        :param dim_size: Массив, содержащий размерность каждого измерения
        """
        if dim_count < 1:
            raise ValueError(
                "Incorrect dimension count. Param `dim_count` must be `1` or great"
            )

        if dim_count != len(dim_size):
            raise ValueError("Length dim_size must be equal dim_count")

        for k, v in enumerate(dim_size):
            if v < 1:
                raise ValueError(
                    f"Incorrect dimension size. "
                    f"Param `dim_size` has value {dim_size[k]} in {k} index."
                    f"Value mast be equal `1` or great"
                )

        self.dim_count = dim_count  # количесто измерений массива
        self.dim_size = dim_size  # массив размеров каждого измерения

        self.elements_count: int = 0  # количество добавленных в массив элементов

        self.capacity_value: int = (
            self.product_multiplication(self.dim_size)
        )  # количество ячеек для хранения данных

        self.array: list[list] | list[ValueKeepListClass] = self.recursive_create_list(
            deep=self.dim_count, current_deep_index=0, dims_lens=self.dim_size
        )

    def __len__(self):
        """
        Возвращает количество ячеек для хранения конечных данных
        """
        return self.capacity_value

    def product_multiplication(self, list_int: list[int]):
        """
        Принимает лист int и отдает их произведение

        :param list_int: числа для переменожения
        :return: произведение
        """
        return reduce(operator.mul, list_int)

    def __getitem__(self, i):
        """
        Метод возвращает объект по индексу из своего объекта
        """
        if 0 > i or i >= self.dim_size[0]:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def __setitem__(self, key, value) -> None:
        """
        Метод позволяет изменять значения только если массив одномерный.
        Если в массиве больше измерений - изменение элементов запрещено
        """
        if self.dim_count != 1 or not isinstance(self.array, ValueKeepListClass):
            raise ValueError(
                "You should not change the array of links directly. "
                "You should change only elements in ValueKeepListClass object"
            )

        response_code = self.array.has_element_by_index(index=key)
        if 0 > key or key >= self.dim_size[0] or response_code == -1:
            raise IndexError("Index is out of bounds")

        if response_code == 1:
            self.array[key] = value
            return
        if response_code == 0:
            self.array[key] = value
            self.elements_count += 1
            return
        raise ValueError(f"Incorrect state! \n" f"Key: {key}, value: {value}")

    def recursive_create_list(
            self, deep: int, current_deep_index: int, dims_lens: list[int]
    ) -> list | ValueKeepListClass:
        if deep < 1:
            raise ValueError(
                f"Incorrect value to param `deep`: {deep}. "
                f"Deep cannot be less than 1."
            )

        current_level_list = []
        for _ in range(dims_lens[current_deep_index]):
            if current_deep_index == deep - 1:
                return self.make_low_level_array(dims_lens[current_deep_index])
            link_to_sublist = self.recursive_create_list(
                deep=deep,
                current_deep_index=current_deep_index + 1,
                dims_lens=dims_lens,
            )
            current_level_list.append(link_to_sublist)
        return current_level_list

    def make_low_level_array(self, new_capacity):
        return ValueKeepListClass(capacity=new_capacity)

    def resize(self, new_capacity: int):
        """При реалокации массив увеличивается на 1 по всем измерениям"""
        # TODO реализовать resize для многомерной структуры

        new_multy_dyn_array_capacity = [i + 1 for i in self.dim_size]

        # new_array = self.make_low_level_array(new_capacity)
        # for i in range(self.elements_count):
        #     new_array[i] = self.array[i]
        # self.array = new_array
        # self.dim_size = [new_capacity]
        # self.capacity_value = self.calculate_capacity()

    def get_link_to_last_el(self):
        """Метод отдает ссылку на последний массив данных"""
        link_to_free_array = self.array
        for i in range(self.dim_count - 1):
            iter_coordinate = self.dim_size[i]
            link_to_free_array = link_to_free_array[iter_coordinate]

        return link_to_free_array

    def get_coordinate_arr_by_element_index(self, index: int) -> list[int]:
        """
        Получаем координаты массива, в котором содержится искомое по абсолютному индексу значение
        :param index: "Абсолютный индекс" - индекс элемента из общей вместимости массива
        :return: координаты массива, в котором находится искомый индекс
        """
        if index >= self.__len__() or index < 0:
            raise IndexError("Index is out of bounds")
        if self.dim_count == 1:
            return [index]
        coordinate = []

        copy_size = self.dim_size.copy()
        copy_size.pop()

        for k, v in enumerate(copy_size):

            for j in range(1, v + 1):
                is_find_index = False
                x = j * self.product_multiplication(self.dim_size[k + 1:])
                if x > index:
                    coordinate.append(j - 1)
                    is_find_index = True
                if j > 1 and is_find_index:
                    index = index - ((j - 1) * self.product_multiplication(self.dim_size[k + 1:]))
                if is_find_index:
                    break


        if len(coordinate) != self.dim_count - 1:
            raise ValueError("Incorrect state")

        return coordinate


    def append_val(self, itm):
        """
        Метод находит координату крайнего элемента многомерного массива и вставляет туда значение.
        Если в крайнем элементе массива уже есть значение - выполняется расширение и реолокация массива.
        """

        if self.elements_count == self.capacity_value:
            self.resize(2 * (self.capacity_value + 1))

        link_to_last_free_array = self.get_link_to_last_el()
        link_to_last_free_array[self.dim_size[-1] - 1] = itm

        self.elements_count += 1

    def increment_dimension(self):
        """Метод увеличивает массив на 1 измерение"""
        new_data = self.recursive_create_list(
            deep=self.dim_count, current_deep_index=0, dims_lens=self.dim_size
        )
        self.array = [self.array, new_data]
        self.dim_count += 1
        self.dim_size = [2] + self.dim_size
        self.capacity_value = self.product_multiplication(self.dim_size)

    def expand_array(self):
        pass
