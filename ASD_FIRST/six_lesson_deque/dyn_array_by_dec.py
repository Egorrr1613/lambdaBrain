import ctypes


class DynArrayByDec:
    """
    Реализация динамического массива с применением банковского метода

    Реаллокация происходит по достижению предела заполнения массива
    Изменена логика переноса элементов при релокации

    Новый массив заполняется из середины,
        чтобы в дальнейшем обеспечить вставку элементов в начало массива
        без необходимости переноса
    """

    def __init__(self):
        self.elements_count = 0
        self.capacity = 4
        self.array = self.make_array(self.capacity)
        self.coin_count_in_bank = 0
        self.head_index = 0

    def __len__(self):
        return self.elements_count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.capacity:
            raise IndexError("Index is out of bounds")

        try:
            self.array[i]
        except ValueError:
            return None

        return self.array[i]

    def __setitem__(self, key, value):
        if key < 0 or key >= self.capacity:
            raise IndexError("Incorrect index")

        self.array[key] = value
        self.elements_count += 1

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)

        for i in range(self.elements_count):
            self.coin_count_in_bank -= 1
            new_array[i] = self.array[(i + self.head_index) % self.capacity]

        self.array = new_array
        self.capacity = new_capacity
        self.head_index = 0

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
        if i < 0 or i > self.capacity:
            raise IndexError("Incorrect index")

        if i is self.capacity:
            self.append(itm=itm)
            return

        self.coin_count_in_bank += 2

        if self.elements_count == self.capacity:
            self.resize(2 * self.capacity)

        for i_range in range(self.elements_count, i, -1):
            self.array[i_range] = self.array[i_range - 1]
            self.coin_count_in_bank -= 1
        self.array[i] = itm
        self.elements_count += 1

    def delete(self, i):
        """
        Цена удаления: 2 монеты. 1 платим, 1 в банк

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
        _ = self[i]

        for loop_i in range(i, self.elements_count - 1):
            self.coin_count_in_bank -= 1
            try:
                next_val = self.array[loop_i + 1]
            except ValueError:
                self.coin_count_in_bank += 1
                next_val = None
            self.array[loop_i] = next_val

        last_key = list(self.array._objects.keys())[-1]
        self.array._objects.pop(last_key)

        self.elements_count -= 1
        self.coin_count_in_bank += 1

    def get_list_elements(self):
        return list(self.array._objects.values())
