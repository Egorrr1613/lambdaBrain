import ctypes


class FixedCapacityList:
    """
    Класс для хранения конечных данных динамического многомерного массива
    """

    def __init__(self, capacity: int, parent):
        self.capacity = capacity
        self.count_elements = 0
        self.array = (capacity * ctypes.py_object)()
        self.last_insert_index = 0
        self.parent = parent

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

    def __setitem__(self, index, value) -> None:
        response_code = self.has_element_by_index(index)
        if response_code == -1:
            raise IndexError("Index is out of bounds")

        if response_code == 1:
            self.array[index] = value
            return

        if response_code == 0:
            self.array[index] = value
            self.count_elements += 1
            self.parent.elements_count += 1
            return

        raise ValueError(f"Response code {response_code} was not processed")

    def has_element_by_index(self, index: int):
        """
        Метод для проверки доступа к ячейке массива

        :param index: Проверяемый индекс
        :return: Код ответа.
            1 - Ячейка памяти хранит какое-то значение
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


def list_multiplication(list_int: list[int]):
    """
    Принимает лист int и отдает их произведение

    :param list_int: числа для умножения
    :return: произведение
    """
    result = 1
    for x in list_int:
        result *= x
    return result


class DynMultyArray:
    """
    Класс, реализующий многомерный динамический массив

    Структура выглядит так:

    1) Класс обертка DynMultyArray
        а) реализуют логику реаллокации многомерного массива
        б) хранит массив ссылок (list)
        в) реализует логику увеличения размерности (измерения) массива
        г) позволяет получить элемент по "абсолютному" индексу

    2) Массив ссылок (self.array) хранит либо:
        а) ссылки на массивы ссылок. Каждый уровень вложенности - это 1 измерение
        б) ссылки на объект ValueKeepListClass - конечные хранимые значения

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

        self.dim_count = dim_count  # количество измерений массива
        self.dim_size = dim_size  # массив размеров каждого измерения

        self.elements_count: int = 0  # количество добавленных в массив элементов

        self.capacity_value: int = list_multiplication(
            self.dim_size
        )  # количество ячеек для хранения данных

        self.array: list[list] | FixedCapacityList = self.recursive_create_list(
            deep=self.dim_count,
            current_deep_index=0,
            dims_lens=self.dim_size,
            replace_el_index=[-1],
        )

    def __len__(self):
        """
        Возвращает количество ячеек для хранения конечных данных
        """
        return self.capacity_value

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
        if self.dim_count != 1 or not isinstance(self.array, FixedCapacityList):
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
            return
        raise ValueError(f"Incorrect state! \n" f"Key: {key}, value: {value}")

    def recursive_create_list(
        self,
        deep: int,
        current_deep_index: int,
        dims_lens: list[int],
        replace_el_index: list[int],
    ) -> list | FixedCapacityList:
        """
        Рекурсивный метод для создания вложенной структуры массивов по заданным размерам.
        На нижнем уровне для хранения элементов используется тип данных ValueKeepListClass.

        Метод получился чуть сложнее чем планировался изначально,
            однако удалось внедрить не только расширение,
            но и перенос элементов в новый массив, когда это необходимо.
        :param deep:
        :param current_deep_index:
        :param dims_lens:
        :param replace_el_index:
        """
        if deep < 1:
            raise ValueError(
                f"Incorrect value to param `deep`: {deep}. "
                f"Deep cannot be less than 1."
            )

        current_level_list = []
        for _ in range(dims_lens[current_deep_index]):
            if current_deep_index == deep - 1:
                returned_array = self.make_low_level_array(
                    dims_lens[current_deep_index]
                )
                if -1 < replace_el_index[0] < self.capacity_value:
                    for i in range(returned_array.capacity):
                        if replace_el_index[0] >= self.capacity_value:
                            break
                        coordinate_el = self.get_coordinate_by_element_index(
                            replace_el_index[0]
                        )
                        value = self.get_value_by_coordinate(coordinate_el)
                        if value is not None:
                            returned_array[i] = value

                        replace_el_index[0] += 1
                return returned_array

            link_to_sublist = self.recursive_create_list(
                deep=deep,
                current_deep_index=current_deep_index + 1,
                dims_lens=dims_lens,
                replace_el_index=replace_el_index,
            )
            current_level_list.append(link_to_sublist)
        return current_level_list

    def make_low_level_array(self, new_capacity):
        """Создаем массив "нижнего" уровня, в котором будут храниться данные"""
        return FixedCapacityList(capacity=new_capacity, parent=self)

    def resize(self):
        """
        Схема реаллокации выбрана следующая:
            Если количество измерений массива равно 1:
                массив увеличивается в 2 раза
            Если количество измерений массива больше 1:
                массив увеличивается на 1 единицу по всем существующим измерениям
        """
        self.elements_count = 0

        if self.dim_count == 1:
            new_multy_dyn_array_capacity = [i * 2 for i in self.dim_size]
        else:
            new_multy_dyn_array_capacity = [i + 1 for i in self.dim_size]

        new_array = self.recursive_create_list(
            deep=self.dim_count,
            current_deep_index=0,
            dims_lens=new_multy_dyn_array_capacity,
            replace_el_index=[0],
        )

        self.dim_size = new_multy_dyn_array_capacity
        self.capacity_value = list_multiplication(new_multy_dyn_array_capacity)
        self.array = new_array

    def get_link_to_last_array(self):
        """Метод отдает ссылку на последний массив данных"""
        link_to_free_array = self.array
        for i in range(self.dim_count - 1):
            iter_coordinate = self.dim_size[i] - 1
            link_to_free_array = link_to_free_array[iter_coordinate]

        return link_to_free_array

    def get_coordinate_by_element_index(self, index: int) -> list[int]:
        """

        :param index: "Абсолютный индекс" - индекс элемента, если бы массив был одномерным.
        :return: Координаты, по котором находится искомый элемент в многомерном массиве.
        """
        if index >= len(self) or index < 0:
            raise IndexError("Index is out of bounds")
        if self.dim_count == 1:
            return [index]
        coordinate = []

        copy_size = self.dim_size.copy()
        copy_size.pop()

        for k, v in enumerate(copy_size):

            for j in range(1, v + 1):
                is_find_index = False
                x = j * list_multiplication(self.dim_size[k + 1 :])
                if x > index:
                    coordinate.append(j - 1)
                    is_find_index = True
                if j > 1 and is_find_index:
                    index = index - (
                        (j - 1) * list_multiplication(self.dim_size[k + 1 :])
                    )
                if is_find_index:
                    break

        coordinate.append(index)
        if len(coordinate) != self.dim_count:
            raise ValueError("Incorrect state")

        return coordinate

    def append_val(self, itm):
        """
        Метод находит координату крайнего элемента многомерного массива и вставляет туда значение.
        Если элементы заполнили массив или в крайнем элементе массива уже есть значение
            - выполняется расширение и реаллокация массива с последующей вставкой.
        """
        link_to_last_free_array = self.get_link_to_last_array()

        if (
            self.elements_count == self.capacity_value
            or link_to_last_free_array[self.dim_size[-1] - 1] is not None
        ):
            self.resize()

        link_to_last_free_array = self.get_link_to_last_array()
        link_to_last_free_array[self.dim_size[-1] - 1] = itm

    def increment_dimension(self):
        """Метод добавляет массиву 1 измерение"""
        new_data = self.recursive_create_list(
            deep=self.dim_count,
            current_deep_index=0,
            dims_lens=self.dim_size,
            replace_el_index=[-1],
        )
        self.array = [self.array, new_data]
        self.dim_count += 1
        self.dim_size = [2] + self.dim_size
        self.capacity_value = list_multiplication(self.dim_size)

    def get_value_by_coordinate(self, list_coordinate: list[int]):
        """
        Метод отдает значение по координатам многомерного массива
        :param list_coordinate: координаты для поиска
        :return: найденное значение
        """
        current_link = self.array
        for i in list_coordinate:
            current_link = current_link[i]
        return current_link

