from ASD_FIRST.lesson_11_bloom.bloom_filter import BloomFilter
from ASD_FIRST.three_lesson.six.multy_dyn_array import DynMultyArray


def sum_any_blume(blume_list: list[BloomFilter]) -> BloomFilter:
    """
    Задание: №11
    Номер задачи из задания: №2
    Краткое название: "Слияние нескольких фильтров Блюма"
    Сложность: size - O(n) / time - O(n)

    Рефлексия: Вероятность ложного срабатывания для итогового фильтра возрастает,
        так как объединение ведет к повышению заполненных битов.
        При этом объем памяти для фильтра не увеличивается.

        Самостоятельно решил через использование оператора ИЛИ.
        Такой же вариант приводился в рекомендуемом решении.
    """
    result = BloomFilter(blume_list[0].filter_len)
    for i_filter in blume_list:
        result.byte_array |= i_filter.byte_array
    return result


class BloomFilterWithDelete:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.byte_array = bytearray(self.filter_len)

    def _base_hash_fun_(self, hash_const: int, value: str) -> int:
        result = 0
        for char in value:
            result = (result * hash_const + ord(char)) % self.filter_len
        return result

    def hash1(self, value) -> int:
        hash_const = 17
        return self._base_hash_fun_(hash_const=hash_const, value=value)

    def hash2(self, value) -> int:
        hash_const = 223
        return self._base_hash_fun_(hash_const=hash_const, value=value)

    def add(self, value: str) -> None:
        self.byte_array[self.hash1(value)] += 1
        self.byte_array[self.hash2(value)] += 1

    def is_value(self, value: str) -> bool:
        return ((self.byte_array[self.hash1(value)] > 0)
                and (self.byte_array[self.hash2(value)] > 0))

    def delete(self, value: str) -> bool:
        """
        Задание: №11
        Номер задачи из задания: №3
        Краткое название: "Фильтр Блюма с удалением"
        Сложность: size - O(1) / time - O(k), где k это длинна value

        Рефлексия: Для реализации удаления решил использовать счетчики добавления каждого индекса.
        Пришлось отказаться от использования int для поля byte_array.
        Вместо этого взял байтовый массив (bytearray), где каждый индекс содержит количество вхождений.
        Кажется такой вариант совпадает с рекомендованным решением.
        """
        if not self.is_value(value):
            return False
        self.byte_array[self.hash1(value)] -= 1
        self.byte_array[self.hash2(value)] -= 1
        return True


END_UNICODE_INDEX = 122  # Всего юникод включает 1114111 символов. Для теста поставил значение меньше.


def get_str_by_unicode_index(unicode_index: list[int]) -> str:
    return "".join([chr(i) for i in unicode_index])


def decode_bloom_filter(b_filter: BloomFilter, expected_data_len: int) -> list[str]:
    """
    Задание: №11
    Номер задачи из задания: №4
    Краткое название: "Восстановление оригинального множества элементов"
    Сложность:
        size - O(m^n)
        time - O(m^n)
        Где m - это размер алфавита и количество символов,
                доступных для использования в зашифрованном слове,
            n - это предполагаемая длинна зашифрованного слова.

    Рефлексия:
        Для восстановления данных самостоятельно придумал только вариант с брутфорсом.
        При реализации брутфорса пришлось немного подумать.
        Основная сложность возникла в реализации генерации строк для перебора.
        Необходимо было получить все комбинации символов для произвольной длинны строки.
        Сначала попытался реализовать "в лоб", однако алгоритм получался довольно сложный.

        Посчитав, как растет количество значений в зависимости от ожидаемой длинны строки,
            я заметил структуру, крайне похожую на многомерный динамический массив.
        Понял что количество возможных вариаций строки зависит от длинны строки в таком же отношении,
            как и количество элементов многомерного массива от числа его измерений.
        По сути многомерным массивом можно моделировать все те комбинации строк, которые необходимы для брутфорса.
        Динамический многомерный массив я реализовывал в рамках дополнительного задания к третьему уроку.
        В реализацию этой структуры я заложил логику получения "координат" элемента в массиве из его индекса.

        Далее алгоритм брутфорса получался тривиальным.
        0) Создать многомерный массив, где количество измерений равно ожидаемому количеству символов в подбираемой строке
        1) Посчитать все возможные комбинации строк, в зависимости от длинны строки и размер алфавита.
            Размер строки задается от 1 до n параметром.
            Размер алфавита регулируется переменной END_UNICODE_INDEX.
        2) В цикле от 0 до N-1, где N это количество всех комбинаций строк для заданной длинны:
            2.1) Раскладываем итерационный индекс на список индексов символов через многомерный массив
            2.2) Из списка индексов символов формируем очередную проверяемую строку
            2.3) Проверяем вхождение строки в декодируемый фильтр
            2.4) В случае вхождения добавляем строку в результирующий список
        3) Возвращаем результирующий список
    """
    data_buffer = DynMultyArray(dim_count=expected_data_len,
                                dim_size=[END_UNICODE_INDEX for _ in range(expected_data_len)])
    correct_value_data = []
    for iter_i in range(0, END_UNICODE_INDEX ** expected_data_len):
        check_data = get_str_by_unicode_index(data_buffer.get_coordinate_by_element_index(iter_i))
        if b_filter.is_value(check_data):
            correct_value_data.append(check_data)
    return correct_value_data
