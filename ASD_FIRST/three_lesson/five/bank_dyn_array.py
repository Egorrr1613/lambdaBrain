import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

        self.coin_count = 0
        self.price_to_next_resize = self.__get_new_price__()

    def __len__(self):
        return self.count

    def __get_new_price__(self):
        pow_of_two = 1
        new_buffer_size = self.capacity * 2

        while True:
            if 2 ** (pow_of_two + 1) > new_buffer_size:
                return 2 ** pow_of_two
            pow_of_two += 1

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        self.price_to_next_resize = self.__get_new_price__()

    def append(self, itm):
        self.coin_count += 3

        if self.coin_count >= self.price_to_next_resize:
            self.resize(2 * self.capacity)

        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError("Incorrect index")

        if i is self.count:
            self.append(itm=itm)
            return

        self.coin_count += 3

        if self.coin_count >= self.price_to_next_resize:
            self.resize(2 * self.capacity)

        for i_range in range(self.count, i, -1):
            self.array[i_range] = self.array[i_range - 1]
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
        self.coin_count -= 3

    def get_list_elements(self):
        return list(self.array._objects.values())

