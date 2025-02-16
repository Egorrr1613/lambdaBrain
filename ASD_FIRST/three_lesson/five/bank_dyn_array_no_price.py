import ctypes


class DynArray:

    def __init__(self):
        self.elements_count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

        self.coin_count_in_bank = 0

    def __len__(self):
        return self.elements_count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.elements_count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def resize(self, new_capacity):
        """
        Метод переносит все элементы из существующего массива в новый, заданного размера
        За перенос каждого элемента списывается 1 монетка
        """

        new_array = self.make_array(new_capacity)
        for i in range(self.elements_count):
            self.coin_count_in_bank -= 1
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        """
        Учетная стоимость: 3 монеты. 1 платим за операцию, 2 в бонк

        Если не влезаем в текущйи размер, то:
        Сначала выполняем реоллакацию, потом вставляем новый элемент
        """
        self.coin_count_in_bank += 2

        if self.elements_count == self.capacity:
            self.resize(2 * self.capacity)

        self.array[self.elements_count] = itm
        self.elements_count += 1

    def insert(self, i, itm):
        """
        Учетная стоимость: 3 монеты. 1 платим за операцию, 2 в бонк
        Так же платим 1 монету каждый раз, когда сдвигаем элементы после вставки

        Если не влезаем в текущйи размер, то:
        Сначала выполняем реоллакацию, потом вставляем элементы с учетом сдвига
        """
        if i < 0 or i > self.elements_count:
            raise IndexError("Incorrect index")

        if i is self.elements_count:
            self.append(itm=itm)
            return

        self.coin_count_in_bank += 2

        if self.elements_count == self.capacity:
            self.resize(2 * self.capacity)

        for i_range in range(self.elements_count, i, -1):
            self.array[i_range] = self.array[i_range - 1]
        self.array[i] = itm
        self.elements_count += 1

    def delete(self, i):
        """
        Цена удаления: 2 монеты. 1 платим, 1 в бонк

        Как реализовал удаление:
        1) Сначала отрабатывает цикл, который смещает все элементы "влево",
            на один индекс после удаляемого.
        2) Последний элемент массива удаляется через обращения к словарю _objects,
           находящемуся в объекте self.array

        Почему не использовал другие варианты:
        * Если использовать "self.array[i] = None" для удаления -
            возникает неоднозначность при хранении None
        * При удалении можно пересоздавать массив через self.resize() -
            однако тогда будет довольно высокий расход
            монеток, так как resize требует для выполнения количество монет,
            равное количеству перемещаемых элементов
            (по одной монетке на каждую элементарную операцию вставки)
        """
        self.__getitem__(i)

        if (self.capacity > 16) and (self.elements_count - 1 < self.capacity // 2):
            self.capacity = max(16, int(self.capacity / 1.5))

        for loop_i in range(i, self.elements_count - 1):
            self.array[loop_i] = self.array[loop_i + 1]
            self.coin_count_in_bank -= 1

        last_key = list(self.array._objects.keys())[-1]
        self.array._objects.pop(last_key)

        self.elements_count -= 1
        self.coin_count_in_bank += 1

    def get_list_elements(self):
        return list(self.array._objects.values())
