class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc: bool):
        self.head: Node | None = None
        self.tail: Node | None = None

        self.__ascending = asc
        self.count_el = 0

    def compare(self, v1, v2) -> int | tuple[str]:
        if v1 == v2:
            return 0

        if self.__ascending and v1 < v2:
            return -1
        if not self.__ascending and v1 > v2:
            return -1
        if not self.__ascending and v1 < v2:
            return 1
        if self.__ascending and v1 > v2:
            return 1
        assert False, ("Error: Compare error",)

    def add(self, value) -> None | tuple[str]:
        new_node = Node(v=value)

        if self.count_el == 0:
            self.head = new_node
            self.tail = new_node

            self.count_el += 1
            return None

        if self.count_el == 1:
            compare_result = self.compare(v1=self.tail.value[0], v2=new_node.value[0])
            if compare_result in (0, 1):
                self.head = new_node
                new_node.next = self.tail
                self.tail.prev = self.head
            if compare_result == -1:
                self.tail = new_node
                self.head.next = self.tail
                self.tail.prev = self.head
            self.count_el += 1
            return None

        if self.compare(v1=self.tail.value[0], v2=new_node.value[0]) == -1:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            self.count_el += 1
            return None

        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_result = self.compare(iter_node.value[0], new_node.value[0])

            if compare_result in (0, 1):
                new_node.prev = iter_node.prev
                new_node.next = iter_node

                if iter_node is self.head:
                    self.head = new_node
                else:
                    iter_node.prev.next = new_node
                iter_node.prev = new_node
                self.count_el += 1
                return None

            if compare_result == -1:
                iter_node = iter_node.next
                continue

            return ("Error: Incorrect compare result",)
        return ("Error: Incorrect state",)

    def find(self, val) -> None | tuple[str, int]:
        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_res = self.compare(val, iter_node.value[0])
            if compare_res == 0:
                return iter_node.value
            if compare_res == -1:
                return None
            if compare_res == 1:
                iter_node = iter_node.next
                continue
        return None

    def delete(self, val) -> None:
        if self.head is None or self.compare(v1=self.tail.value[0], v2=val) == -1:
            return None

        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_res = self.compare(v1=iter_node.value[0], v2=val)
            if compare_res == 0:

                if iter_node is self.head and iter_node is self.tail:
                    self.head = None
                    self.tail = None
                    self.count_el = 0
                    return None

                if iter_node is self.head:
                    self.head = iter_node.next
                    self.head.prev = None
                    self.count_el -= 1
                    return None

                if iter_node is self.tail:
                    self.tail = iter_node.prev
                    self.tail.next = None
                    self.count_el -= 1
                    return None

                iter_node.prev.next = iter_node.next
                iter_node.next.prev = iter_node.prev

                self.count_el -= 1
                return None
            if compare_res == 1:
                return None
            if compare_res == -1:
                iter_node = iter_node.next
        return None

    def clean(self, asc) -> None:
        self.__ascending = asc
        self.head = None
        self.tail = None
        self.count_el = 0

    def len(self) -> int:
        return self.count_el

    def get_all(self) -> list:
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def get_all_v2(self) -> list:
        node: Node | None = self.head
        res = []
        while isinstance(node, Node):
            if node is self.head:
                prev_node_val = None
            else:
                prev_node_val = node.prev.value
            if node is self.tail:
                next_node_val = None
            else:
                next_node_val = node.next.value
            res.append((prev_node_val, node.value, next_node_val))
            node = node.next
        return res


class NativeDictionaryBySortedList:
    """
    Задание: №9
    Номер задачи из задания: №5
    Краткое название: "Словарь с использованием упорядоченного списка"

    Рефлексия:
        Попробовал реализовать на основе стандартного упорядоченного списка,
        хранящего объекты с полями ключ/значение. Однако для "решения в лоб" скорость поиска была O(N).

        Тогда взял за основу реализацию упорядоченного списка на динамическом массиве с бинарным поиском.
        Соответственно доработал массив, чтобы он хранил объекты типа Node с двумя полями: key/value.
        Оценка сложности получилась такая:
            * put: size - O(1), O(n) при реалокации / time амортизированный - O(log(n))
            * delete: size - O(1), O(n) при реалокации / time амортизированный - O(log(n))
            * find: size - O(1) / time - O(log(n))

        Понял что реализация далеко не идеальная, переделал на решение, которое вы привели в качестве ответа.
        Заметил следующий минус в рекомендованном решении: так как элементы в keys хранят индекс элемента
            то при удалении элемента нужно либо удалить элемент из values и переназначить смещенные индексы в
            объектах упорядоченного списка keys что приведет к увеличению сложность до O(n) ИЛИ не удалять объект
            из values, однако тогда удаленные элементы будут накапливаться без очистки.
        Для решения задания решил выбрать оптимальную сложность и, следовательно, не очищать values.
        Итоговая сложность:
            * put: size - O(1) / time - O(log(n))
            * delete: size - O(1) / time - O(log(n))
            * find: size - O(1) / time - O(log(n))
    """

    def __init__(self):
        self.keys = OrderedList(asc=True)
        self.values = []

    def is_key(self, key: str | None) -> bool:
        return key in self.keys

    def put(self, key: str, value) -> None:
        index = self.keys.find(key)
        if index is None:
            self.keys.add(value=(key, len(self.values)))
            self.values.append(value)
            return
        self.values[index[1]] = value

    def find(self, key: str):
        index = self.keys.find(key)
        return None if index is None else self.values[index[1]]

    def delete(self, key: str):
        self.keys.delete(key)

    def __len__(self):
        return self.keys.len()


class EmptySlot:
    def __init__(self):
        pass


class NativeDictionaryByByteKeys:
    """
    Задание: №9
    Номер задачи из задания: №6
    Краткое название: "Словарь с использованием байтовых строк в качестве ключей"
    Сложность:
            * put: size - O(1) / time - O(1)
            * delete: size - O(1)/ time - O(n)
            * find: size - O(1) / time - O(n)

    Рефлексия: Честно не до конца понял задание. Исходя из текста задания,
    необходимо было с помощью байтовых операций ускорить поиск/вставку/удаление.
    Однако, так как используются байтовые строки в качестве ключей -
    их можно быстро приводить к числовым индексам, которые используются .
    Не до конца понятно, с какой стороны тут нужно подходить и в какой части
    использовать побитовые операции.
    Нужно будет взять индивидуальную консультацию по этому заданию.
    """

    def __init__(self):
        self.key_len = 10

        self.values = [EmptySlot()] * 256

    def _validate_key_(self, key: str):
        if len(key) > self.key_len or len(key) < 3 or key[0:2] != '0b':
            assert False, f"Incorrect key data. Must be 0b... format. Max len: {self.key_len}"

    def _key_to_index_(self, key: str) -> int:
        return int(key, base=2)

    def put(self, key: str, value) -> None:
        self._validate_key_(key)
        index = self._key_to_index_(key)
        self.values[index] = value

    def delete(self, key: str):
        self._validate_key_(key)
        self.values[self._key_to_index_(key)] = EmptySlot()

    def find(self, key: str):
        self._validate_key_(key)
        return self.values[self._key_to_index_(key)]
