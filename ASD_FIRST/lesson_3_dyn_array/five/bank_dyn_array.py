import ctypes


class DynArray:
    """
    Реализация динамического массива с применением банковского метода

    Реаллокация происходит, когда количество монеток в банке превышает определенный порог
    """

    def __init__(self):
        self.elements_count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

        self.coin_count_in_bank = 0
        self.price_to_next_resize = self.__get_new_price__()

    def __len__(self):
        return self.elements_count

    def __get_new_price__(self):
        return self.capacity

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
        self.price_to_next_resize = self.__get_new_price__()

    def append(self, itm):
        """
        Учетная стоимость: 3 монеты. 1 платим за операцию, 2 в банк

        Если не влезаем в текущий размер, то:
        Сначала выполняем реаллокацию, потом вставляем новый элемент
        """
        self.coin_count_in_bank += 2

        if self.elements_count == self.capacity:
            self.resize(2 * self.capacity)

        self.array[self.elements_count] = itm
        self.elements_count += 1

    def insert(self, i, itm):
        """
        Учетная стоимость: 3 монеты. 1 платим за операцию, 2 в банк
        Так же платим 1 монету каждый раз, когда сдвигаем элементы после вставки

        Если не влезаем в текущий размер, то:
        Сначала выполняем реаллокацию, потом вставляем элементы с учетом сдвига
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
        """Цена удаления: 2 монеты. 1 платим, 1 в банк"""
        self.__getitem__(i)

        if (self.capacity > 16) and (self.elements_count - 1 < self.capacity // 2):
            self.capacity = max(16, int(self.capacity / 1.5))

        for loop_i in range(i, self.elements_count - 1):
            self.array[loop_i] = self.array[loop_i + 1]

        self.elements_count -= 1
        self.resize(self.capacity)
        self.coin_count_in_bank += 1

    def get_list_elements(self):
        return list(self.array._objects.values())

