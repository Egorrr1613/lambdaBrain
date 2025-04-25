import ctypes
import random
import string

from ASD_FIRST.two_lesson.doubly_linked_list import LinkedList2, Node


class EmptyElement:
    def __init__(self):
        pass


class DynArrayByHashTable:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.capacity:
            raise IndexError("Index is out of bounds")
        try:
            return self.array[i]
        except ValueError:
            return EmptyElement()

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        self.array = new_array
        self.capacity = new_capacity
        self.count = 0

    def append(self, itm):
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i is self.count:
            return self.append(itm=itm)

        self.__getitem__(i)

        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        self.__getitem__(i)

        if (self.capacity > 16) and (self.count - 1 < self.capacity // 2):
            self.capacity = max(16, int(self.capacity / 1.5))

        for loop_i in range(i, self.count - 1):
            self.array[loop_i] = self.array[loop_i + 1]

        self.count -= 1
        self.resize(self.capacity)

    def get_list_elements(self):
        return list(self.array._objects.values())


class DynHashTable:
    """
    Задание: №8
    Номер задачи из задания: №3
    Краткое название: "Динамическая хеш таблица"
    Сложность:
        * put: size - O(n) / time - O(n)

    Рефлексия:
        Довольно много времени потратил на это задание. Выбирал структуру, которую можно использовать для решения.
        Приведу здесь свои мысли по некоторым из них.

        * Динамический массив, содержащий связные списки.
            Минусы:
            1) При релокации элементов придется пересчитывать хеш для всех элементов каждого связного списка.
            2) Присутствует вероятность попадания большого числа элементов в один связный список.
            3) При таком подходе слабая логика в части релокации. Если ждать пока 75% массива будет заполнено
                не пустыми связными списками - тогда в момент релокации количество элементов в отдельных связных списках
                может быть очень велико.

            Хорошим вариантом кажется использовать связные списки фиксированной длинны - например 8.
            В таком случае при достижении лимита заполнения связного списка не добавлять данные.

            Сложность по времени при релокаци: O(n).

        * Динамический массив, хранящий элементы, использующий метод последовательных проб.
            Минусы:
            1) При увеличении размера таблицы необходимо перераспределять индексы всех элементов.

            Сложность по времени при релокаци: O(n).

        * Динамический массив, использующий метод согласованного хеширования. Хеш функция не привязана к размеру хранилища.
            Минусы:
            1) Кажется не подходит для решения данной задачи, так как алгоритм работает на изначально большом хранилище.
                Для решения задачи необходим алгоритм, постепенно увеличивающий размер хранилища.
                Основная сложность у меня возникла в том, что не понятно куда распределять элемент,
                если хэш функция отдает индекс, больший, чем текущий размер хранилища.
                    Если вставлять в пространство "крайнего" узла, возникает существенная группировка данных
                    в этом пространстве.
                    Если отображать узлы на Т-токены, то не понятно как распределять Т-токены при увеличении таблицы и
                    как следствие, добавлении новых узлов.
                С учетом необходимости увеличивать размер хранилища и возможно релоцировать элементы,
                не смог придумать адекватного решения.
            2) Так же не придумал хорошей логики для обработки случая, когда пространство определенного сегмента уже
                заполнено и требуется вставить еще один элемент.
                Как вариант - в таком случае просто не выполнять вставку.
            3) Каким выбрать размер сегмента, если наше хранилище при каждой релокации должно увеличиваться в 2 раза?
            Использовать константный размер или динамически увеличивать сегменты?

            Сложность по времени при релокаци:
            O(N) - если все элементы находятся в крайнем сегменте
            o(log N) - если элементы по сегментам распределены равномерно тогда перераспределяются
                только элементы из крайнего сегмента.

        * Динамический массив, использующий хеш функцию, минимизирующую коллизии и не зависимую от размера таблицы.
        Например, упрощенный вариант SHA-256:
            Минусы:
            1) Сложность реализации

    Итог: Решил реализовать вариант динамической хеш таблицы использующий связные списки.
        Вариант с согласованным хешированием давал лучший результат при релокации.
        Однако, кажется он не корректен, так как часто могут допускаться случаи не выполнения вставки элемента.
    """

    def __init__(self):
        self.slots = DynArrayByHashTable()

    def hash_fun(self, value: str) -> int:
        return sum(i for i in str.encode(value)) % self.slots.capacity

    def put(self, value: str) -> int | None:
        index = self.hash_fun(value=value)

        if isinstance(self.slots[index], LinkedList2):
            self.slots[index].add_in_tail(Node(v=value))
            return index
        if isinstance(self.slots[index], EmptyElement):
            new_list = LinkedList2()
            new_list.add_in_tail(Node(v=value))
            self.slots.insert(i=index, itm=new_list)

            if self.slots.count == (self.slots.capacity // 4) * 3:
                self._resize_slots_()

            return index

        assert False, "Некорректное состояние"

    def _resize_slots_(self):
        old_capacity = self.slots.capacity
        old_arr = self.slots.array
        self.slots.resize(2 * self.slots.capacity)

        for i in range(old_capacity):
            try:
                old_arr[i]
            except ValueError:
                continue
            if isinstance(old_arr[i], LinkedList2):
                i_node = old_arr[i].head
                while i_node is not None:
                    value = i_node.value
                    i_node = i_node.next
                    old_arr[i].delete(value)
                    self.put(value)

    def find(self, value) -> int | None:
        index = self.hash_fun(value=value)
        if isinstance(self.slots[index], EmptyElement):
            return None
        if not isinstance(self.slots[index], LinkedList2):
            assert False, f"Некорректное состояние. index: {index}, value: {value}"
        link_list: LinkedList2 = self.slots[index]
        if link_list.find(value) is None:
            return None
        return index


class HashTableTwoHash:
    """
    Задание: №8
    Номер задачи из задания: №4
    Краткое название: "Хеш таблица с двумя хеш функциями"
    Сложность: без оценки

    Рефлексия:
        Сравнивал исходную реализацию хеш таблицы и хеш таблицу с двумя хеш функциями.
        За контрольный размер хеш таблицы взял простое число 101.
        В файле test_hash_table_with_two_hash подготовил необходимый код для замера количества коллизий.

        Провел несколько замеров, ниже привожу результаты количества коллизий:
        +------------+-------------------+----------------------------------+
        | № запуска  | Исходная таблица  | Таблица с двумя хеш-функциями    |
        +============+===================+==================================+
        | 1          | 362               | 194                              |
        +------------+-------------------+----------------------------------+
        | 2          | 352               | 297                              |
        +------------+-------------------+----------------------------------+
        | 3          | 386               | 218                              |
        +------------+-------------------+----------------------------------+
        | 4          | 507               | 237                              |
        +------------+-------------------+----------------------------------+
        | 5          | 426               | 304                              |
        +------------+-------------------+----------------------------------+

        Вывод:
        В среднем использование двух хеш функций позволяет снизить количество коллизий на 30%
        относительно стандартной реализации.
    """

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.collision_count = 0

    def hash_fun_1(self, value: str) -> int:
        return sum(i for i in str.encode(value)) % self.size

    def hash_fun_2(self, value: str) -> int:
        """
        Константы a b - простые числа
        """
        a = 157
        b = 43
        x = sum(i for i in str.encode(value))
        return ((a * x + b) % self.size) % self.size

    def seek_slot(self, value: str) -> int | None:
        index = self.hash_fun_1(value)
        if self.slots[index] is None or self.slots[index] == value:
            return index
        for i in range(1, self.size):
            index = (self.hash_fun_1(value) + i * self.hash_fun_2(value)) % self.size
            if self.slots[index] is None or self.slots[index] == value:
                return index
            self.collision_count += 1
        return None

    def put(self, value: str) -> int | None:
        if (index := self.seek_slot(value)) is not None:
            self.slots[index] = value
            return index
        return None


class HashTableWithSalt:
    """
    Задание: №8
    Номер задачи из задания: №5
    Краткое название: "Хеш таблица с солью"
    Сложность:
        * put: size - O(n) / time - O(n)

    Рефлексия:
        Изучив указанные в уроке ссылки без подсказок сделал рекомендуемое решение с динамической солью.
    """
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.salt_size = 5
        self.salt_dict = {}

    def hash_fun(self, value: str) -> int:
        return sum(i for i in str.encode(value)) % self.size

    def get_salt(self, value) -> str:
        if value not in self.salt_dict:
            self.salt_dict[value] = ''.join(random.choices(string.ascii_letters + string.digits, k=self.salt_size))
        return self.salt_dict[value]

    def seek_slot(self, value: str) -> int | None:
        index = self.hash_fun(value + self.get_salt(value))
        for _ in range(self.size // self.step + 1):
            if self.slots[index] is None or self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
        return None

    def put(self, value: str) -> int | None:
        if (index := self.seek_slot(value)) is not None:
            self.slots[index] = value
            return index
        return None
